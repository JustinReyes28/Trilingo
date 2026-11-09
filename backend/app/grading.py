"""Policy-driven authoritative grading. No language-specific course dispatch."""

import re
import unicodedata

from app.content_schema import Exercise, Policy
from app.learning_schemas import Answer
from app.services import DomainError


def normalize_text(value: str, policy: Policy) -> str:
    value = unicodedata.normalize(policy.normalization, value)
    if policy.trim:
        value = value.strip()
    if policy.punctuation == "ignore_terminal":
        value = re.sub(r"[.!?。！？]+$", "", value)
    if policy.spacing == "ignore":
        value = "".join(value.split())
    if not policy.case_sensitive:
        value = value.casefold()
    return value


def script_matches(value: str, policy: Policy) -> bool:
    # Script restrictions are applied after the exercise's explicit normalization.
    letters = [c for c in value if not c.isspace() and not unicodedata.category(c).startswith("P")]
    if policy.script == "hiragana":
        return bool(letters) and all("\u3041" <= c <= "\u309f" for c in letters)
    if policy.script == "katakana":
        return bool(letters) and all("\u30a1" <= c <= "\u30ff" for c in letters)
    return True


def grade(exercise: Exercise, answer: Answer) -> bool:
    invalid = DomainError(422, "answer_shape", "Check the answer format and choose valid options.")
    match exercise.type:
        case "speaking":
            raise DomainError(
                422,
                "speech_unassessed",
                "Use a speaking session for transcript feedback; pronunciation is not graded.",
            )
        case "multiple_choice" | "response_selection" | "listening_selection" | "audio_contrast":
            if not isinstance(answer, str) or answer not in {x.id for x in exercise.choices}:
                raise invalid
            return answer == exercise.answer
        case (
            "translation"
            | "fill_blank"
            | "dialogue_completion"
            | "constrained_roleplay"
            | "dictation"
        ):
            if not isinstance(answer, str) or not answer.strip():
                raise invalid
            value = normalize_text(answer, exercise.policy)
            return script_matches(value, exercise.policy) and any(
                value == normalize_text(expected, exercise.policy) for expected in exercise.answers
            )
        case "sentence_ordering":
            if not isinstance(answer, list) or sorted(answer) != sorted(exercise.answer):
                raise invalid
            return answer == exercise.answer
        case "matching":
            if (
                not isinstance(answer, dict)
                or sorted(answer) != sorted(exercise.answer)
                or sorted(answer.values()) != sorted(exercise.answer.values())
            ):
                raise invalid
            return answer == exercise.answer
    raise DomainError(422, "exercise_type", "This exercise type is not supported.")
