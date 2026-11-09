import { z } from 'zod'

export const ProfileSchema = z.object({ id: z.string(), name: z.string(), timezone: z.string() })
export type Profile = z.infer<typeof ProfileSchema>
const ProviderSchema = z.object({ enabled: z.boolean(), provider: z.string(), base_url: z.string(), model: z.string(), voice: z.string(), timeout: z.number() })
export const SettingsSchema = z.object({ daily_goal: z.number().nullable(), show_goal: z.boolean(), furigana: z.enum(['always','unfamiliar','hidden']), romaji: z.boolean(), reduced_motion: z.boolean(), sound: z.boolean(), show_statistics: z.boolean(), practice_batch: z.number(), interests:z.array(z.string()).default([]), preferred_focus:z.enum(['mixed','reading','typing','meaning']).default('mixed'), accent:z.enum(['path','plum']).default('path'), show_quests:z.boolean().default(true), monthly_quest_target:z.number().default(20), show_timer:z.boolean().default(false), show_reminder:z.boolean().default(false), retention:z.number().default(0.9), ai: ProviderSchema, tts: ProviderSchema, stt: ProviderSchema })
export type Settings = z.infer<typeof SettingsSchema>
export const HealthSchema = z.object({ status: z.literal('ok'), database: z.literal('ready'), schema_version: z.string(), features: z.object({lessons:z.boolean(),ai:z.boolean(),tts:z.boolean(),stt:z.boolean()}) })
const StatusSchema = z.enum(['draft','reviewed','published'])
export const SegmentSchema = z.object({surface:z.string(),reading:z.string().nullable().optional(),vocabulary_id:z.string().nullable().optional()})
const LessonMetaSchema = z.object({id:z.string(),title:z.string(),japanese_title:z.string(),objective:z.string(),order:z.number(),status:StatusSchema,preparation:z.array(z.string())})
const StageSchema = z.object({id:z.string(),title:z.string(),release:z.string(),can_do:z.array(z.string()),status:StatusSchema,word_target:z.number(),kanji_target:z.number()})
export const MapSchema = z.object({ id:z.string(),title:z.string(),version:z.string(),description:z.string(),review_note:z.string(),stages:z.array(StageSchema),units:z.array(z.object({id:z.string(),title:z.string(),japanese_title:z.string(),description:z.string(),guide:z.string(),order:z.number(),stage:z.string(),status:StatusSchema,lessons:z.array(LessonMetaSchema.extend({exercise_count:z.number(),available:z.boolean(),study_state:z.enum(['not_started','visited','studied','assisted','skipped'])}))})),inventory:z.object({published_words:z.number(),published_phrases:z.number(),published_kanji:z.number(),published_lessons:z.number(),target_words:z.number(),target_kanji:z.number(),coverage:z.string()}) })
export type CourseMap = z.infer<typeof MapSchema>
export type Unit = CourseMap['units'][number]
export type LessonMeta = Unit['lessons'][number]
const ChoiceSchema = z.object({id:z.string(),text:z.string()})
const ExerciseBase = z.object({id:z.string(),prompt:z.string(),objective:z.string(),concepts:z.array(z.string()),difficulty:z.number(),skill:z.string(),preparation:z.array(z.string()),policy:z.object({script:z.string(),normalization:z.string(),trim:z.boolean(),punctuation:z.string(),case_sensitive:z.boolean(),strategy:z.string(),spacing:z.enum(['preserve','ignore']),hint_policy:z.literal('always_available'),required_distinctions:z.array(z.enum(['voicing','kana_size','vowel_length','target_script']))})})
export const ExerciseSchema = z.discriminatedUnion('type',[
 ExerciseBase.extend({type:z.literal('speaking'),reference_text:z.string(),audio:z.array(z.object({id:z.string(),label:z.string()}))}),
 ExerciseBase.extend({type:z.literal('listening_selection'),choices:z.array(ChoiceSchema),audio:z.array(z.object({id:z.string(),label:z.string()}))}),
 ExerciseBase.extend({type:z.literal('audio_contrast'),choices:z.array(ChoiceSchema),audio:z.array(z.object({id:z.string(),label:z.string()}))}),
 ExerciseBase.extend({type:z.literal('dictation'),audio:z.array(z.object({id:z.string(),label:z.string()}))}),
 ExerciseBase.extend({type:z.literal('multiple_choice'),choices:z.array(ChoiceSchema)}),
 ExerciseBase.extend({type:z.literal('response_selection'),choices:z.array(ChoiceSchema)}),
 ExerciseBase.extend({type:z.literal('dialogue_completion')}),
 ExerciseBase.extend({type:z.literal('constrained_roleplay')}),
 ExerciseBase.extend({type:z.literal('translation')}),
 ExerciseBase.extend({type:z.literal('fill_blank')}),
 ExerciseBase.extend({type:z.literal('sentence_ordering'),tokens:z.array(ChoiceSchema)}),
 ExerciseBase.extend({type:z.literal('matching'),left:z.array(ChoiceSchema),right:z.array(ChoiceSchema)}),
])
export const LessonSchema = LessonMetaSchema.extend({exercises:z.array(ExerciseSchema)})
export type Lesson = z.infer<typeof LessonSchema>
export const LibrarySchema = z.object({concepts:z.array(z.object({id:z.string(),title:z.string(),explanation:z.string()})),vocabulary:z.array(z.object({id:z.string(),surface:z.string(),reading:z.string(),gloss:z.string(),part_of_speech:z.string(),entry_kind:z.enum(['word','phrase']),register:z.string(),example:z.array(SegmentSchema),concepts:z.array(z.string()),stage:z.string(),status:StatusSchema,audio:z.string().nullable()})),writing_tasks:z.array(z.object({id:z.string(),stage:z.string(),genre:z.string(),prompt:z.string(),model:z.string(),alternatives:z.array(z.string()),checklist:z.array(z.string()),status:StatusSchema,rubric_version:z.string()})),licenses:z.array(z.object({id:z.string(),source:z.string(),license:z.string(),attribution:z.string()}))})
export type Library = z.infer<typeof LibrarySchema>
export const CoursesSchema = z.array(z.object({id:z.string(),title:z.string(),language:z.string(),teaching_language:z.string(),description:z.string(),version:z.string()}))

export const BackupProfileSchema = z.object({ id: z.string(), name: z.string(), timezone: z.string() })
export const BackupSummarySchema = z.object({
  total_xp: z.number(),
  study_sessions_completed: z.number(),
  study_sessions_total: z.number(),
  review_cards_count: z.number(),
  writing_drafts_count: z.number(),
  writing_revisions_count: z.number(),
  collections_count: z.number(),
  drawing_samples_count: z.number(),
  reading_items_saved: z.number(),
  reading_items_familiar: z.number(),
  audio_deliveries_count: z.number(),
  quests_count: z.number(),
  badges_count: z.number(),
  mistakes_count: z.number(),
})
export type BackupSummary = z.infer<typeof BackupSummarySchema>

export const BackupPreviewSchema = z.object({
  valid: z.boolean(),
  created_at: z.string(),
  app_name: z.string(),
  app_version: z.string(),
  schema_version: z.string(),
  compatible: z.boolean(),
  profile: BackupProfileSchema,
  summary: BackupSummarySchema,
  course_id: z.string().nullable().optional(),
  course_version: z.string().nullable().optional(),
  include_drawing_samples: z.boolean(),
  warning: z.string(),
})
export type BackupPreview = z.infer<typeof BackupPreviewSchema>

export const RestoreResultSchema = z.object({
  restored: z.boolean(),
  created_at: z.string(),
  profile: BackupProfileSchema,
  summary: BackupSummarySchema,
  safety_backup_file: z.string().nullable().optional(),
})
export type RestoreResult = z.infer<typeof RestoreResultSchema>

export const ResetResultSchema = z.object({
  reset: z.boolean(),
  profile: BackupProfileSchema,
  message: z.string(),
  safety_backup_file: z.string().nullable().optional(),
})
export type ResetResult = z.infer<typeof ResetResultSchema>

export const SafetyBackupItemSchema = z.object({
  filename: z.string(),
  size_bytes: z.number(),
  created_at: z.string(),
  kind: z.string(),
})
export const SafetyBackupListSchema = z.object({
  backups: z.array(SafetyBackupItemSchema),
})
export type SafetyBackupItem = z.infer<typeof SafetyBackupItemSchema>

