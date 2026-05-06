-- PM Operating System — Supabase schema
-- Apply once via Supabase dashboard (SQL Editor) or CLI: supabase db push

create table if not exists projects (
  id           uuid primary key default gen_random_uuid(),
  name         text not null,
  project_code text,
  status       text check (status in ('Discovery','Planned','In Progress','Blocked','Done','Archived')),
  business_area text,
  owner        text,
  team         text,
  summary      text,
  created_at   timestamptz default now()
);

create table if not exists teams (
  id         uuid primary key default gen_random_uuid(),
  name       text not null,
  lead       text,
  area       text,
  notes      text,
  created_at timestamptz default now()
);

create table if not exists meetings (
  id           uuid primary key default gen_random_uuid(),
  meeting_id   text unique not null,
  project      text,
  team         text,
  meeting_type text check (meeting_type in ('ASIS','TOBE','Follow-up','Planning','Decision','Risk','Other')),
  meeting_date timestamptz,
  participants text,
  source       text,
  notes        text,
  created_at   timestamptz default now()
);

create table if not exists transcripts (
  id             uuid primary key default gen_random_uuid(),
  transcript_id  text unique not null,
  meeting_id     text references meetings(meeting_id),
  project        text,
  team           text,
  raw_transcript text,
  source_url     text,
  immutable      boolean default true,
  imported_at    timestamptz default now()
);

create table if not exists draft_insights (
  id           uuid primary key default gen_random_uuid(),
  draft_id     text unique not null,
  project      text,
  meeting_id   text,
  draft_type   text check (draft_type in ('Business Context','ASIS','TOBE','Capability','Feature','User Story','Risk','Decision','Summary','Open Question')),
  title        text,
  content      text,
  status       text check (status in ('Draft','In Review','Approved Candidate','Rejected','Archived')) default 'Draft',
  version_hint int,
  created_at   timestamptz default now(),
  updated_at   timestamptz default now()
);

create table if not exists approved_context (
  id               uuid primary key default gen_random_uuid(),
  context_id       text unique not null,
  project          text,
  context_type     text check (context_type in ('Business Context','ASIS','TOBE','Capability','Feature','User Story','Risk','Decision','Operating Rule')),
  title            text,
  approved_content text,
  version          int default 1,
  status           text check (status in ('Active','Superseded','Archived')) default 'Active',
  source_references text,
  approved_by      text,
  approved_at      timestamptz,
  created_at       timestamptz default now()
);

create table if not exists okrs (
  id           uuid primary key default gen_random_uuid(),
  okr_id       text unique not null,
  project      text,
  team         text,
  objective    text,
  key_result   text,
  metric_name  text,
  baseline     numeric,
  target       numeric,
  current_value numeric,
  due_date     timestamptz,
  status       text check (status in ('On Track','At Risk','Off Track','Done')),
  created_at   timestamptz default now()
);

create table if not exists capabilities (
  id             uuid primary key default gen_random_uuid(),
  capability_id  text unique not null,
  project        text,
  name           text,
  purpose        text,
  scope          text,
  expected_outcome text,
  exclusions     text,
  status         text check (status in ('Proposed','Approved','In Progress','Done','Dropped')) default 'Proposed',
  version        text,
  source_references text,
  created_at     timestamptz default now()
);

create table if not exists features (
  id           uuid primary key default gen_random_uuid(),
  feature_id   text unique not null,
  project      text,
  capability   text,
  name         text,
  description  text,
  priority     text check (priority in ('High','Medium','Low')),
  status       text check (status in ('Proposed','Approved','In Progress','Done','Dropped')) default 'Proposed',
  created_at   timestamptz default now()
);

create table if not exists user_stories (
  id                  uuid primary key default gen_random_uuid(),
  story_id            text unique not null,
  project             text,
  feature             text,
  capability_id       text,
  capability_name     text,
  source_epic         text,
  original_key        text,
  title               text,
  type                text,
  narrative           text,
  acceptance_criteria text,
  scope_treatment     text,
  notes               text,
  status              text check (status in ('Draft','Approved','Planned','In Progress','Done','Dropped','Active','Merged','Scope Review','Needs Review')) default 'Draft',
  sort_order          int,
  created_at          timestamptz default now()
);

create table if not exists decisions (
  id            uuid primary key default gen_random_uuid(),
  decision_id   text unique not null,
  project       text,
  title         text,
  decision      text,
  rationale     text,
  decision_date timestamptz,
  status        text check (status in ('Active','Superseded','Rejected')) default 'Active',
  created_at    timestamptz default now()
);

create table if not exists risks (
  id          uuid primary key default gen_random_uuid(),
  risk_id     text unique not null,
  project     text,
  title       text,
  description text,
  impact      text check (impact in ('High','Medium','Low')),
  probability text check (probability in ('High','Medium','Low')),
  mitigation  text,
  status      text check (status in ('Open','Watching','Mitigated','Closed')) default 'Open',
  created_at  timestamptz default now()
);

create table if not exists followups (
  id          uuid primary key default gen_random_uuid(),
  followup_id text unique not null,
  project     text,
  team        text,
  title       text,
  commitment  text,
  owner       text,
  due_date    timestamptz,
  status      text check (status in ('Open','In Progress','Done','Delayed','Cancelled')) default 'Open',
  created_at  timestamptz default now()
);

create table if not exists milestones (
  id           uuid primary key default gen_random_uuid(),
  milestone_id text unique not null,
  project      text,
  name         text,
  description  text,
  target_date  timestamptz,
  status       text check (status in ('Upcoming','On Track','At Risk','Missed','Done')) default 'Upcoming',
  created_at   timestamptz default now()
);
