"""Learner-curated vocabulary collections, independent from assessment and access."""

from datetime import datetime, timezone
from uuid import uuid4

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.content_schema import CourseContent
from app.learning import study_transaction
from app.models import CourseVersion
from app.review_models import CollectionMember, ReviewCard, VocabularyCollection
from app.review_schemas import CollectionRecall
from app.services import DomainError, current_content, local_profile


def collection_out(db: Session, row: VocabularyCollection) -> dict:
    count = (
        db.scalar(
            select(func.count())
            .select_from(CollectionMember)
            .where(CollectionMember.collection_id == row.id)
        )
        or 0
    )
    return {"id": row.id, "name": row.name, "item_count": count, "created_at": row.created_at}


def create(db: Session, course_id: str, request_id: str, name: str) -> dict:
    with study_transaction(db):
        current_content(db, course_id)
        row = db.get(VocabularyCollection, request_id)
        if row:
            if row.course_id != course_id or row.name != name or row.profile_id != "local":
                raise DomainError(
                    409, "collection_conflict", "Use a new ID for a different collection."
                )
        else:
            row = VocabularyCollection(
                id=request_id,
                profile_id="local",
                course_id=course_id,
                name=name,
                created_at=datetime.now(timezone.utc).isoformat(),
            )
            db.add(row)
        return collection_out(db, row)


def listing(db: Session, course_id: str, offset: int, limit: int) -> list[dict]:
    local_profile(db)
    counts = (
        select(CollectionMember.collection_id, func.count().label("total"))
        .group_by(CollectionMember.collection_id)
        .subquery()
    )
    rows = db.execute(
        select(VocabularyCollection, func.coalesce(counts.c.total, 0))
        .outerjoin(counts, counts.c.collection_id == VocabularyCollection.id)
        .where(
            VocabularyCollection.profile_id == "local", VocabularyCollection.course_id == course_id
        )
        .order_by(VocabularyCollection.created_at, VocabularyCollection.id)
        .offset(offset)
        .limit(limit)
    ).all()
    return [
        {"id": row.id, "name": row.name, "item_count": count, "created_at": row.created_at}
        for row, count in rows
    ]


def owner(db: Session, collection_id: str) -> VocabularyCollection:
    row = db.get(VocabularyCollection, collection_id)
    if row is None or row.profile_id != "local":
        raise DomainError(
            404, "collection_missing", "Collection not found. Choose another collection."
        )
    return row


def membership(db: Session, collection_id: str, item_id: str, saved: bool) -> dict:
    with study_transaction(db):
        row = owner(db, collection_id)
        version, content = current_content(db, row.course_id)
        member = db.get(CollectionMember, (row.id, item_id))
        if saved:
            if not any(
                word.id == item_id and word.status == "published" for word in content.vocabulary
            ):
                raise DomainError(404, "collection_word", "Choose a published word.")
            if member is None:
                db.add(
                    CollectionMember(
                        collection_id=row.id, item_id=item_id, course_version_id=version.id
                    )
                )
        elif member:
            db.delete(member)
        db.flush()
        return collection_out(db, row)


def members(db: Session, collection_id: str, offset: int, limit: int) -> dict:
    owner(db, collection_id)
    rows = db.execute(
        select(CollectionMember, CourseVersion)
        .join(CourseVersion, CourseVersion.id == CollectionMember.course_version_id)
        .where(CollectionMember.collection_id == collection_id)
        .order_by(CollectionMember.item_id)
        .offset(offset)
        .limit(limit + 1)
    ).all()
    unique = {snapshot.id: snapshot for _, snapshot in rows}
    snapshots = {
        key: CourseContent.model_validate(snapshot.data) for key, snapshot in unique.items()
    }
    return {
        "items": [
            next(
                word.model_dump()
                for word in snapshots[member.course_version_id].vocabulary
                if word.id == member.item_id
            )
            for member, _ in rows[:limit]
        ],
        "has_more": len(rows) > limit,
        "offset": offset,
    }


def recall(
    db: Session, collection_id: str, body: CollectionRecall, offset: int, limit: int
) -> dict:
    """Prepare unscheduled cards from saved snapshots; existing schedules are untouched."""
    from app.review import card_out, scheduler_config

    with study_transaction(db):
        collection = owner(db, collection_id)
        filters = [CollectionMember.collection_id == collection_id]
        if body.item_id is not None:
            filters.append(CollectionMember.item_id == body.item_id)
        total = db.scalar(select(func.count()).select_from(CollectionMember).where(*filters)) or 0
        if body.item_id is not None and total == 0:
            raise DomainError(404, "collection_word", "Choose a word saved in this collection.")
        members_page = db.scalars(
            select(CollectionMember)
            .where(*filters)
            .order_by(CollectionMember.item_id)
            .offset(offset)
            .limit(limit + 1)
        ).all()
        selected = members_page[:limit]
        existing = {
            row.item_id: row
            for row in db.scalars(
                select(ReviewCard).where(
                    ReviewCard.profile_id == collection.profile_id,
                    ReviewCard.course_id == collection.course_id,
                    ReviewCard.item_kind == "word",
                    ReviewCard.direction == body.direction,
                    ReviewCard.item_id.in_([member.item_id for member in selected]),
                )
            ).all()
        }
        version_ids = {member.course_version_id for member in selected}
        version_ids.update(row.course_version_id for row in existing.values())
        contents = {
            version.id: CourseContent.model_validate(version.data)
            for version in db.scalars(
                select(CourseVersion).where(CourseVersion.id.in_(version_ids))
            )
        }
        config = scheduler_config()
        result = []
        for member in selected:
            row = existing.get(member.item_id)
            if row is None:
                row = ReviewCard(
                    id=str(uuid4()),
                    profile_id=collection.profile_id,
                    course_id=collection.course_id,
                    course_version_id=member.course_version_id,
                    item_id=member.item_id,
                    item_kind="word",
                    direction=body.direction,
                    state={},
                    due=None,
                    revision=0,
                    scheduler=config,
                )
                db.add(row)
            result.append(card_out(db, row, contents[row.course_version_id]))
        db.flush()
        return {
            "cards": result,
            "total": total,
            "offset": offset,
            "has_more": len(members_page) > limit,
        }
