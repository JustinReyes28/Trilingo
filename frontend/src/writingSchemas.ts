import { z } from 'zod'
import { CharacterSchema } from './readingSchemas'
export const WritingTaskSchema=z.object({id:z.string(),stage:z.string(),genre:z.string(),prompt:z.string(),model:z.string(),alternatives:z.array(z.string()),checklist:z.array(z.string()),revision_before:z.string().nullable().optional(),revision_after:z.string().nullable().optional(),revision_note:z.string().nullable().optional(),status:z.enum(['draft','reviewed','published']),rubric_version:z.string(),exercise_ids:z.array(z.string()).default([])})
export const RevisionSchema=z.object({id:z.string(),number:z.number(),text:z.string(),checklist:z.array(z.string()),model_revealed:z.boolean(),created_at:z.string()})
export const DraftSchema=z.object({id:z.string(),course_id:z.string(),content_version:z.string(),task:WritingTaskSchema,current:RevisionSchema,created_at:z.string(),updated_at:z.string(),assessment:z.literal('not_assessed')})
export type WritingDraft=z.infer<typeof DraftSchema>
export const WritingCatalogSchema=z.object({tasks:z.array(WritingTaskSchema),drafts:z.array(z.object({id:z.string(),task_id:z.string(),title:z.string(),content_version:z.string(),updated_at:z.string()})),has_more:z.boolean(),offset:z.number(),includes_drafts:z.boolean(),content_version:z.string()})
export const HistorySchema=z.object({revisions:z.array(RevisionSchema),conflicts:z.array(z.object({id:z.string(),text:z.string(),checklist:z.array(z.string()),model_revealed:z.boolean(),expected_revision_id:z.string(),server_revision_id:z.string(),created_at:z.string()})),has_more_revisions:z.boolean(),has_more_conflicts:z.boolean(),offset:z.number()})
export const SubmissionSchema=z.object({id:z.string(),draft_id:z.string(),revision_id:z.string(),xp_awarded:z.number(),evidence_mode:z.literal('open_writing'),assessment:z.enum(['not_assessed','self_reviewed']),message:z.string()})
export type WritingSubmission=z.infer<typeof SubmissionSchema>
export const PointSchema=z.object({x:z.number().min(0).max(1),y:z.number().min(0).max(1),t:z.number().int().nonnegative()})
export type StrokePoint=z.infer<typeof PointSchema>
export const GuideSchema=z.object({character:CharacterSchema,content_version:z.string(),guide:z.object({id:z.string(),character_id:z.string(),version:z.string(),license_id:z.string(),source:z.string(),status:z.enum(['draft','reviewed']),strokes:z.array(z.object({points:z.array(z.object({x:z.number(),y:z.number()})),instruction:z.string()}))}).nullable(),license:z.object({id:z.string(),source:z.string(),license:z.string(),attribution:z.string()}).nullable(),message:z.string()})
export type FormationGuide=z.infer<typeof GuideSchema>
export const HandwritingResultSchema=z.object({id:z.string(),character_id:z.string(),mode:z.string(),evidence:z.literal('self_reported_practice'),self_rating:z.string(),feedback:z.string(),xp_awarded:z.number(),sample_id:z.string().nullable(),objective_correctness:z.null()})
export const SamplesSchema=z.array(z.object({id:z.string(),character_id:z.string(),mode:z.string(),strokes:z.array(z.array(PointSchema)),created_at:z.string()}))
