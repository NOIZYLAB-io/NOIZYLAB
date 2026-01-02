-- ████████████████████████████████████████████████████████████████████
-- ███                                                              ███
-- ███     NOIZYLAB OS - OMNI-SOVEREIGN DATABASE SCHEMA            ███
-- ███                                                              ███
-- ███  Complete D1 schema for all AI workers and services         ███
-- ███                                                              ███
-- ████████████████████████████████████████████████████████████████████

-- ═══════════════════════════════════════════════════════════════════
-- CORE TABLES (Main Worker)
-- ═══════════════════════════════════════════════════════════════════

-- Users
CREATE TABLE IF NOT EXISTS users (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  password_hash TEXT,
  role TEXT DEFAULT 'user' CHECK(role IN ('admin', 'manager', 'technician', 'user', 'customer')),
  status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'suspended')),
  avatar_url TEXT,
  phone TEXT,
  specializations TEXT DEFAULT '[]', -- JSON array
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now')),
  last_login TEXT
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);

-- API Keys
CREATE TABLE IF NOT EXISTS api_keys (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  key_hash TEXT NOT NULL,
  name TEXT,
  permissions TEXT DEFAULT '[]', -- JSON array
  rate_limit INTEGER DEFAULT 1000,
  expires_at TEXT,
  last_used TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_api_keys_user ON api_keys(user_id);

-- Sessions
CREATE TABLE IF NOT EXISTS sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  token_hash TEXT NOT NULL,
  device_info TEXT,
  ip_address TEXT,
  expires_at TEXT NOT NULL,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_sessions_user ON sessions(user_id);
CREATE INDEX idx_sessions_expires ON sessions(expires_at);

-- ═══════════════════════════════════════════════════════════════════
-- TICKET SYSTEM
-- ═══════════════════════════════════════════════════════════════════

-- Tickets
CREATE TABLE IF NOT EXISTS tickets (
  id TEXT PRIMARY KEY,
  ticket_number TEXT UNIQUE,
  customer_id TEXT REFERENCES users(id),
  customer_name TEXT,
  customer_email TEXT,
  customer_phone TEXT,
  
  -- Device Info
  device_type TEXT,
  device_model TEXT,
  device_serial TEXT,
  device_color TEXT,
  device_condition TEXT,
  
  -- Issue Details
  issue_type TEXT,
  issue_description TEXT,
  symptoms TEXT DEFAULT '[]', -- JSON array
  reported_issues TEXT DEFAULT '[]', -- JSON array
  
  -- Status & Priority
  status TEXT DEFAULT 'pending' CHECK(status IN (
    'pending', 'triaged', 'assigned', 'in_progress', 'waiting_parts',
    'pending_approval', 'on_hold', 'resolved', 'closed', 'cancelled'
  )),
  priority TEXT DEFAULT 'normal' CHECK(priority IN ('low', 'normal', 'high', 'urgent', 'critical')),
  
  -- Assignment
  assigned_to TEXT REFERENCES users(id),
  team_id TEXT,
  
  -- Diagnosis
  ai_diagnosis TEXT, -- JSON object
  technician_diagnosis TEXT,
  root_cause TEXT,
  
  -- Pricing
  estimated_price REAL DEFAULT 0,
  final_price REAL DEFAULT 0,
  parts_cost REAL DEFAULT 0,
  labor_cost REAL DEFAULT 0,
  
  -- Parts
  parts_used TEXT DEFAULT '[]', -- JSON array
  parts_needed TEXT DEFAULT '[]', -- JSON array
  
  -- Tracking
  customer_rating INTEGER CHECK(customer_rating BETWEEN 1 AND 5),
  customer_feedback TEXT,
  
  -- Timestamps
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now')),
  first_response_at TEXT,
  resolved_at TEXT,
  closed_at TEXT,
  
  -- SLA
  sla_due_at TEXT,
  sla_breached INTEGER DEFAULT 0,
  
  -- Metadata
  source TEXT DEFAULT 'web',
  tags TEXT DEFAULT '[]', -- JSON array
  custom_fields TEXT DEFAULT '{}', -- JSON object
  internal_notes TEXT
);

CREATE INDEX idx_tickets_customer ON tickets(customer_id);
CREATE INDEX idx_tickets_assigned ON tickets(assigned_to);
CREATE INDEX idx_tickets_status ON tickets(status);
CREATE INDEX idx_tickets_priority ON tickets(priority);
CREATE INDEX idx_tickets_created ON tickets(created_at);
CREATE INDEX idx_tickets_device ON tickets(device_type, device_model);

-- Ticket Comments
CREATE TABLE IF NOT EXISTS ticket_comments (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id) ON DELETE CASCADE,
  user_id TEXT REFERENCES users(id),
  content TEXT NOT NULL,
  is_internal INTEGER DEFAULT 0,
  attachments TEXT DEFAULT '[]', -- JSON array
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_comments_ticket ON ticket_comments(ticket_id);

-- Ticket Attachments
CREATE TABLE IF NOT EXISTS ticket_attachments (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id) ON DELETE CASCADE,
  filename TEXT NOT NULL,
  file_type TEXT,
  file_size INTEGER,
  storage_key TEXT NOT NULL,
  uploaded_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_attachments_ticket ON ticket_attachments(ticket_id);

-- Ticket History (Audit Log)
CREATE TABLE IF NOT EXISTS ticket_history (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id) ON DELETE CASCADE,
  user_id TEXT REFERENCES users(id),
  action TEXT NOT NULL,
  field_changed TEXT,
  old_value TEXT,
  new_value TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_history_ticket ON ticket_history(ticket_id);
CREATE INDEX idx_history_created ON ticket_history(created_at);

-- ═══════════════════════════════════════════════════════════════════
-- INVENTORY SYSTEM
-- ═══════════════════════════════════════════════════════════════════

-- Parts
CREATE TABLE IF NOT EXISTS parts (
  id TEXT PRIMARY KEY,
  sku TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  category TEXT NOT NULL,
  subcategory TEXT,
  manufacturer TEXT,
  mpn TEXT, -- Manufacturer Part Number
  
  -- Stock
  quantity INTEGER DEFAULT 0,
  reorder_point INTEGER DEFAULT 5,
  optimal_stock INTEGER DEFAULT 20,
  
  -- Pricing
  unit_cost REAL DEFAULT 0,
  
  -- Location
  location TEXT DEFAULT 'UNASSIGNED',
  
  -- Compatibility
  compatible_devices TEXT DEFAULT '[]', -- JSON array
  
  -- Shelf Life
  shelf_life_days INTEGER,
  date_added TEXT DEFAULT (datetime('now')),
  last_used TEXT,
  
  -- Metadata
  notes TEXT,
  image_url TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_parts_sku ON parts(sku);
CREATE INDEX idx_parts_category ON parts(category);
CREATE INDEX idx_parts_location ON parts(location);
CREATE INDEX idx_parts_quantity ON parts(quantity);

-- Part Movements
CREATE TABLE IF NOT EXISTS part_movements (
  id TEXT PRIMARY KEY,
  part_id TEXT REFERENCES parts(id),
  type TEXT NOT NULL CHECK(type IN ('IN', 'OUT', 'ADJUST', 'TRANSFER', 'SCRAP')),
  quantity INTEGER NOT NULL,
  reference_id TEXT, -- Ticket ID for OUT
  unit_cost REAL,
  from_location TEXT,
  to_location TEXT,
  reason TEXT,
  created_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_movements_part ON part_movements(part_id);
CREATE INDEX idx_movements_type ON part_movements(type);
CREATE INDEX idx_movements_created ON part_movements(created_at);

-- ═══════════════════════════════════════════════════════════════════
-- KNOWLEDGE BASE
-- ═══════════════════════════════════════════════════════════════════

-- KB Articles
CREATE TABLE IF NOT EXISTS kb_articles (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  slug TEXT UNIQUE,
  content TEXT NOT NULL,
  summary TEXT,
  category TEXT,
  tags TEXT DEFAULT '[]', -- JSON array
  device_types TEXT DEFAULT '[]', -- JSON array
  
  -- Status
  status TEXT DEFAULT 'draft' CHECK(status IN ('draft', 'published', 'archived')),
  
  -- Author
  author_id TEXT REFERENCES users(id),
  
  -- Metrics
  views INTEGER DEFAULT 0,
  helpful_votes INTEGER DEFAULT 0,
  not_helpful_votes INTEGER DEFAULT 0,
  
  -- SEO
  meta_title TEXT,
  meta_description TEXT,
  
  -- Timestamps
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now')),
  published_at TEXT
);

CREATE INDEX idx_kb_status ON kb_articles(status);
CREATE INDEX idx_kb_category ON kb_articles(category);
CREATE INDEX idx_kb_slug ON kb_articles(slug);

-- ═══════════════════════════════════════════════════════════════════
-- AR GUIDES
-- ═══════════════════════════════════════════════════════════════════

-- Repair Guides
CREATE TABLE IF NOT EXISTS repair_guides (
  id TEXT PRIMARY KEY,
  title TEXT,
  device_type TEXT NOT NULL,
  device_model TEXT,
  repair_type TEXT NOT NULL,
  difficulty TEXT DEFAULT 'medium' CHECK(difficulty IN ('easy', 'medium', 'hard', 'expert')),
  
  -- Content
  estimated_time_minutes INTEGER DEFAULT 30,
  tools_required TEXT DEFAULT '[]', -- JSON array
  parts_required TEXT DEFAULT '[]', -- JSON array
  steps TEXT DEFAULT '[]', -- JSON array of RepairStep
  safety_warnings TEXT DEFAULT '[]', -- JSON array
  
  -- Status
  approved INTEGER DEFAULT 0,
  created_by TEXT REFERENCES users(id),
  
  -- Metrics
  views INTEGER DEFAULT 0,
  success_rate REAL DEFAULT 0,
  
  -- Timestamps
  created_at TEXT DEFAULT (datetime('now')),
  updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_guides_device ON repair_guides(device_type, device_model);
CREATE INDEX idx_guides_repair ON repair_guides(repair_type);
CREATE INDEX idx_guides_approved ON repair_guides(approved);

-- AR Sessions
CREATE TABLE IF NOT EXISTS ar_sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  guide_id TEXT REFERENCES repair_guides(id),
  current_step INTEGER DEFAULT 1,
  completed_steps TEXT DEFAULT '[]', -- JSON array
  notes TEXT DEFAULT '[]', -- JSON array
  photos_taken TEXT DEFAULT '[]', -- JSON array
  started_at TEXT DEFAULT (datetime('now')),
  last_activity TEXT DEFAULT (datetime('now')),
  completed_at TEXT
);

CREATE INDEX idx_ar_sessions_user ON ar_sessions(user_id);
CREATE INDEX idx_ar_sessions_guide ON ar_sessions(guide_id);

-- Live Shares
CREATE TABLE IF NOT EXISTS live_shares (
  id TEXT PRIMARY KEY,
  session_id TEXT REFERENCES ar_sessions(id),
  created_by TEXT REFERENCES users(id),
  annotations TEXT DEFAULT '[]', -- JSON array
  active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now'))
);

-- ═══════════════════════════════════════════════════════════════════
-- TRAINING SYSTEM
-- ═══════════════════════════════════════════════════════════════════

-- Training Modules
CREATE TABLE IF NOT EXISTS training_modules (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  device_category TEXT,
  difficulty TEXT DEFAULT 'beginner' CHECK(difficulty IN ('beginner', 'intermediate', 'advanced', 'expert')),
  skill_points INTEGER DEFAULT 100,
  estimated_minutes INTEGER DEFAULT 30,
  prerequisites TEXT DEFAULT '[]', -- JSON array of module IDs
  lessons TEXT DEFAULT '[]', -- JSON array of TrainingLesson
  final_exam TEXT, -- JSON Exam object
  certification TEXT, -- JSON Certification object or null
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_modules_category ON training_modules(device_category);
CREATE INDEX idx_modules_difficulty ON training_modules(difficulty);

-- Training Simulations
CREATE TABLE IF NOT EXISTS training_simulations (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  device_type TEXT,
  scenario TEXT,
  difficulty TEXT,
  difficulty_multiplier REAL DEFAULT 1.0,
  initial_state TEXT, -- JSON DeviceState
  target_state TEXT, -- JSON DeviceState
  available_tools TEXT DEFAULT '[]', -- JSON array
  available_parts TEXT DEFAULT '[]', -- JSON array
  time_limit_seconds INTEGER DEFAULT 600,
  hints TEXT DEFAULT '[]', -- JSON array of SimulationHint
  scoring TEXT DEFAULT '{}', -- JSON ScoringRules
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_simulations_device ON training_simulations(device_type);

-- Training Sessions
CREATE TABLE IF NOT EXISTS training_sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  module_id TEXT REFERENCES training_modules(id),
  current_lesson INTEGER DEFAULT 0,
  completed_lessons TEXT DEFAULT '[]', -- JSON array
  score INTEGER DEFAULT 0,
  status TEXT DEFAULT 'in_progress' CHECK(status IN ('in_progress', 'completed', 'abandoned')),
  started_at TEXT DEFAULT (datetime('now')),
  completed_at TEXT
);

CREATE INDEX idx_training_sessions_user ON training_sessions(user_id);

-- Simulation Sessions
CREATE TABLE IF NOT EXISTS simulation_sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  simulation_id TEXT REFERENCES training_simulations(id),
  current_state TEXT, -- JSON DeviceState
  actions_taken TEXT DEFAULT '[]', -- JSON array
  hints_used INTEGER DEFAULT 0,
  mistakes INTEGER DEFAULT 0,
  score INTEGER DEFAULT 0,
  status TEXT DEFAULT 'in_progress',
  started_at TEXT DEFAULT (datetime('now')),
  completed_at TEXT
);

CREATE INDEX idx_sim_sessions_user ON simulation_sessions(user_id);

-- Training Exams
CREATE TABLE IF NOT EXISTS training_exams (
  id TEXT PRIMARY KEY,
  title TEXT,
  module_id TEXT REFERENCES training_modules(id),
  questions TEXT DEFAULT '[]', -- JSON array of ExamQuestion
  passing_score INTEGER DEFAULT 70,
  time_limit_minutes INTEGER DEFAULT 30,
  certification_id TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

-- Exam Sessions
CREATE TABLE IF NOT EXISTS exam_sessions (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  exam_id TEXT REFERENCES training_exams(id),
  questions TEXT, -- JSON shuffled questions
  answers TEXT DEFAULT '{}', -- JSON user answers
  score INTEGER,
  passed INTEGER DEFAULT 0,
  status TEXT DEFAULT 'in_progress',
  started_at TEXT DEFAULT (datetime('now')),
  completed_at TEXT
);

CREATE INDEX idx_exam_sessions_user ON exam_sessions(user_id);

-- User Training Progress
CREATE TABLE IF NOT EXISTS user_training_progress (
  user_id TEXT PRIMARY KEY REFERENCES users(id),
  total_xp INTEGER DEFAULT 0,
  level INTEGER DEFAULT 1,
  modules_completed TEXT DEFAULT '[]', -- JSON array
  certifications TEXT DEFAULT '[]', -- JSON array
  achievements TEXT DEFAULT '[]', -- JSON array
  current_streak INTEGER DEFAULT 0,
  longest_streak INTEGER DEFAULT 0,
  skills TEXT DEFAULT '{}', -- JSON skill levels
  last_activity TEXT DEFAULT (datetime('now'))
);

-- Achievements
CREATE TABLE IF NOT EXISTS achievements (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  icon TEXT,
  xp_reward INTEGER DEFAULT 0,
  rarity TEXT DEFAULT 'common' CHECK(rarity IN ('common', 'uncommon', 'rare', 'epic', 'legendary')),
  condition TEXT DEFAULT '{}' -- JSON AchievementCondition
);

-- Certifications
CREATE TABLE IF NOT EXISTS certifications (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  level INTEGER DEFAULT 1,
  valid_months INTEGER DEFAULT 12,
  badge_url TEXT,
  requirements TEXT DEFAULT '{}' -- JSON requirements
);

-- User Certifications
CREATE TABLE IF NOT EXISTS user_certifications (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  certification_id TEXT REFERENCES certifications(id),
  credential_id TEXT UNIQUE,
  earned_at TEXT DEFAULT (datetime('now')),
  expires_at TEXT
);

CREATE INDEX idx_user_certs_user ON user_certifications(user_id);
CREATE INDEX idx_user_certs_credential ON user_certifications(credential_id);

-- XP Log
CREATE TABLE IF NOT EXISTS xp_log (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  xp_earned INTEGER,
  source TEXT,
  reference_id TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_xp_log_user ON xp_log(user_id);
CREATE INDEX idx_xp_log_created ON xp_log(created_at);

-- ═══════════════════════════════════════════════════════════════════
-- NOTIFICATIONS SYSTEM
-- ═══════════════════════════════════════════════════════════════════

-- Notifications
CREATE TABLE IF NOT EXISTS notifications (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  type TEXT NOT NULL,
  channel TEXT NOT NULL CHECK(channel IN ('push', 'email', 'sms', 'slack', 'discord', 'teams', 'in_app')),
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  data TEXT DEFAULT '{}', -- JSON
  priority TEXT DEFAULT 'normal' CHECK(priority IN ('low', 'normal', 'high', 'critical')),
  status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'sent', 'delivered', 'failed', 'read')),
  error TEXT,
  scheduled_at TEXT,
  sent_at TEXT,
  read_at TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_status ON notifications(status);
CREATE INDEX idx_notifications_created ON notifications(created_at);

-- Notification Preferences
CREATE TABLE IF NOT EXISTS notification_preferences (
  user_id TEXT PRIMARY KEY REFERENCES users(id),
  channels TEXT DEFAULT '{}', -- JSON enabled channels
  types TEXT DEFAULT '{}', -- JSON type -> channels mapping
  quiet_hours TEXT, -- JSON { start, end }
  digest_mode INTEGER DEFAULT 0,
  digest_frequency TEXT DEFAULT 'daily',
  email TEXT,
  phone TEXT,
  push_subscriptions TEXT DEFAULT '[]' -- JSON array
);

-- Notification Templates
CREATE TABLE IF NOT EXISTS notification_templates (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,
  channel TEXT NOT NULL,
  subject TEXT,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  variables TEXT DEFAULT '[]', -- JSON array of variable names
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_templates_type ON notification_templates(type, channel);

-- ═══════════════════════════════════════════════════════════════════
-- EBAY SNIPER
-- ═══════════════════════════════════════════════════════════════════

-- Watched Searches
CREATE TABLE IF NOT EXISTS ebay_watched_searches (
  id TEXT PRIMARY KEY,
  query TEXT NOT NULL,
  category TEXT,
  max_price REAL,
  min_profit_margin REAL DEFAULT 20,
  condition TEXT,
  active INTEGER DEFAULT 1,
  created_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

-- Found Items
CREATE TABLE IF NOT EXISTS ebay_found_items (
  id TEXT PRIMARY KEY,
  search_id TEXT REFERENCES ebay_watched_searches(id),
  ebay_item_id TEXT UNIQUE,
  title TEXT,
  price REAL,
  shipping REAL,
  condition TEXT,
  seller_rating REAL,
  end_time TEXT,
  image_url TEXT,
  item_url TEXT,
  estimated_profit REAL,
  profit_analysis TEXT, -- JSON
  alert_sent INTEGER DEFAULT 0,
  purchased INTEGER DEFAULT 0,
  found_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_ebay_items_search ON ebay_found_items(search_id);
CREATE INDEX idx_ebay_items_profit ON ebay_found_items(estimated_profit DESC);

-- ═══════════════════════════════════════════════════════════════════
-- PRICING ENGINE
-- ═══════════════════════════════════════════════════════════════════

-- Pricing Rules
CREATE TABLE IF NOT EXISTS pricing_rules (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  device_type TEXT,
  repair_type TEXT,
  base_price REAL NOT NULL,
  complexity_multiplier REAL DEFAULT 1.0,
  urgency_multiplier REAL DEFAULT 1.0,
  margin_target REAL DEFAULT 30,
  min_price REAL,
  max_price REAL,
  active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_pricing_device ON pricing_rules(device_type, repair_type);

-- Price History
CREATE TABLE IF NOT EXISTS price_history (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id),
  quoted_price REAL,
  final_price REAL,
  parts_cost REAL,
  labor_cost REAL,
  margin_actual REAL,
  pricing_rule_id TEXT REFERENCES pricing_rules(id),
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_price_history_ticket ON price_history(ticket_id);

-- Competitor Prices
CREATE TABLE IF NOT EXISTS competitor_prices (
  id TEXT PRIMARY KEY,
  competitor_name TEXT,
  device_type TEXT,
  repair_type TEXT,
  price REAL,
  source_url TEXT,
  scraped_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_competitor_device ON competitor_prices(device_type, repair_type);

-- ═══════════════════════════════════════════════════════════════════
-- BRAIN WORKER (AI Diagnostics)
-- ═══════════════════════════════════════════════════════════════════

-- Diagnosis History
CREATE TABLE IF NOT EXISTS ai_diagnoses (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id),
  symptoms TEXT DEFAULT '[]', -- JSON input symptoms
  diagnosis TEXT, -- JSON AI diagnosis result
  confidence REAL,
  thinking_process TEXT, -- Extended thinking output
  repair_plan TEXT, -- JSON repair steps
  estimated_time INTEGER,
  estimated_cost REAL,
  model_used TEXT,
  tokens_used INTEGER,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_diagnoses_ticket ON ai_diagnoses(ticket_id);

-- Repair Learnings
CREATE TABLE IF NOT EXISTS repair_learnings (
  id TEXT PRIMARY KEY,
  device_type TEXT,
  device_model TEXT,
  issue_type TEXT,
  symptoms TEXT DEFAULT '[]', -- JSON
  successful_fix TEXT,
  failure_modes TEXT DEFAULT '[]', -- JSON
  tips TEXT DEFAULT '[]', -- JSON
  times_referenced INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_learnings_device ON repair_learnings(device_type, device_model);
CREATE INDEX idx_learnings_issue ON repair_learnings(issue_type);

-- ═══════════════════════════════════════════════════════════════════
-- VISION WORKER (PCB Analysis)
-- ═══════════════════════════════════════════════════════════════════

-- Golden References
CREATE TABLE IF NOT EXISTS golden_references (
  id TEXT PRIMARY KEY,
  device_type TEXT NOT NULL,
  device_model TEXT NOT NULL,
  board_name TEXT,
  image_key TEXT NOT NULL, -- R2 key
  component_map TEXT, -- JSON component locations
  annotations TEXT DEFAULT '[]', -- JSON annotations
  uploaded_by TEXT REFERENCES users(id),
  verified INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_golden_refs_device ON golden_references(device_type, device_model);

-- Analysis Results
CREATE TABLE IF NOT EXISTS pcb_analyses (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id),
  uploaded_image_key TEXT,
  golden_ref_id TEXT REFERENCES golden_references(id),
  anomalies TEXT DEFAULT '[]', -- JSON detected anomalies
  confidence_scores TEXT, -- JSON component-by-component confidence
  ar_overlay_data TEXT, -- JSON AR overlay coordinates
  analysis_time_ms INTEGER,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_pcb_analyses_ticket ON pcb_analyses(ticket_id);

-- ═══════════════════════════════════════════════════════════════════
-- APPOINTMENTS & SCHEDULING
-- ═══════════════════════════════════════════════════════════════════

-- Appointments
CREATE TABLE IF NOT EXISTS appointments (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id),
  customer_id TEXT REFERENCES users(id),
  technician_id TEXT REFERENCES users(id),
  type TEXT DEFAULT 'drop_off' CHECK(type IN ('drop_off', 'pickup', 'on_site', 'virtual')),
  scheduled_at TEXT NOT NULL,
  duration_minutes INTEGER DEFAULT 30,
  status TEXT DEFAULT 'scheduled' CHECK(status IN ('scheduled', 'confirmed', 'in_progress', 'completed', 'cancelled', 'no_show')),
  location TEXT,
  notes TEXT,
  reminder_sent INTEGER DEFAULT 0,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_appointments_ticket ON appointments(ticket_id);
CREATE INDEX idx_appointments_customer ON appointments(customer_id);
CREATE INDEX idx_appointments_technician ON appointments(technician_id);
CREATE INDEX idx_appointments_scheduled ON appointments(scheduled_at);

-- Business Hours
CREATE TABLE IF NOT EXISTS business_hours (
  id TEXT PRIMARY KEY,
  day_of_week INTEGER NOT NULL CHECK(day_of_week BETWEEN 0 AND 6),
  open_time TEXT NOT NULL,
  close_time TEXT NOT NULL,
  is_closed INTEGER DEFAULT 0
);

-- ═══════════════════════════════════════════════════════════════════
-- WORKSPACES & TEAMS
-- ═══════════════════════════════════════════════════════════════════

-- Workspaces
CREATE TABLE IF NOT EXISTS workspaces (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  slug TEXT UNIQUE,
  owner_id TEXT REFERENCES users(id),
  settings TEXT DEFAULT '{}', -- JSON
  created_at TEXT DEFAULT (datetime('now'))
);

-- Workspace Members
CREATE TABLE IF NOT EXISTS workspace_members (
  workspace_id TEXT REFERENCES workspaces(id) ON DELETE CASCADE,
  user_id TEXT REFERENCES users(id) ON DELETE CASCADE,
  role TEXT DEFAULT 'member' CHECK(role IN ('owner', 'admin', 'member')),
  joined_at TEXT DEFAULT (datetime('now')),
  PRIMARY KEY (workspace_id, user_id)
);

-- ═══════════════════════════════════════════════════════════════════
-- AUDIT & COMPLIANCE
-- ═══════════════════════════════════════════════════════════════════

-- Audit Log
CREATE TABLE IF NOT EXISTS audit_log (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  action TEXT NOT NULL,
  resource_type TEXT,
  resource_id TEXT,
  old_value TEXT,
  new_value TEXT,
  ip_address TEXT,
  user_agent TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_audit_user ON audit_log(user_id);
CREATE INDEX idx_audit_resource ON audit_log(resource_type, resource_id);
CREATE INDEX idx_audit_created ON audit_log(created_at);

-- GDPR Data Export Requests
CREATE TABLE IF NOT EXISTS gdpr_requests (
  id TEXT PRIMARY KEY,
  user_id TEXT REFERENCES users(id),
  type TEXT CHECK(type IN ('export', 'delete')),
  status TEXT DEFAULT 'pending' CHECK(status IN ('pending', 'processing', 'completed', 'failed')),
  download_url TEXT,
  expires_at TEXT,
  created_at TEXT DEFAULT (datetime('now')),
  completed_at TEXT
);

CREATE INDEX idx_gdpr_user ON gdpr_requests(user_id);

-- ═══════════════════════════════════════════════════════════════════
-- SURVEYS & FEEDBACK
-- ═══════════════════════════════════════════════════════════════════

-- Surveys
CREATE TABLE IF NOT EXISTS surveys (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id),
  customer_id TEXT REFERENCES users(id),
  overall_rating INTEGER CHECK(overall_rating BETWEEN 1 AND 5),
  quality_rating INTEGER CHECK(quality_rating BETWEEN 1 AND 5),
  service_rating INTEGER CHECK(service_rating BETWEEN 1 AND 5),
  speed_rating INTEGER CHECK(speed_rating BETWEEN 1 AND 5),
  would_recommend INTEGER CHECK(would_recommend BETWEEN 1 AND 10),
  feedback TEXT,
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_surveys_ticket ON surveys(ticket_id);
CREATE INDEX idx_surveys_customer ON surveys(customer_id);

-- ═══════════════════════════════════════════════════════════════════
-- CANNED RESPONSES & TEMPLATES
-- ═══════════════════════════════════════════════════════════════════

-- Canned Responses
CREATE TABLE IF NOT EXISTS canned_responses (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  content TEXT NOT NULL,
  variables TEXT DEFAULT '[]', -- JSON array
  use_count INTEGER DEFAULT 0,
  created_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX idx_canned_category ON canned_responses(category);

-- Email Templates
CREATE TABLE IF NOT EXISTS email_templates (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  subject TEXT NOT NULL,
  html_body TEXT NOT NULL,
  text_body TEXT,
  variables TEXT DEFAULT '[]', -- JSON array
  category TEXT,
  active INTEGER DEFAULT 1,
  created_at TEXT DEFAULT (datetime('now'))
);

-- ═══════════════════════════════════════════════════════════════════
-- INTEGRATIONS
-- ═══════════════════════════════════════════════════════════════════

-- Chat Integrations
CREATE TABLE IF NOT EXISTS chat_integrations (
  id TEXT PRIMARY KEY,
  platform TEXT NOT NULL CHECK(platform IN ('slack', 'discord', 'teams', 'telegram')),
  webhook_url TEXT NOT NULL,
  channel_name TEXT,
  events TEXT DEFAULT '[]', -- JSON array of event types
  active INTEGER DEFAULT 1,
  created_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

-- Webhook Endpoints
CREATE TABLE IF NOT EXISTS webhooks (
  id TEXT PRIMARY KEY,
  url TEXT NOT NULL,
  events TEXT DEFAULT '[]', -- JSON array
  secret TEXT,
  active INTEGER DEFAULT 1,
  last_triggered TEXT,
  failure_count INTEGER DEFAULT 0,
  created_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

-- ═══════════════════════════════════════════════════════════════════
-- TIMERS & SLA
-- ═══════════════════════════════════════════════════════════════════

-- Work Timers
CREATE TABLE IF NOT EXISTS work_timers (
  id TEXT PRIMARY KEY,
  ticket_id TEXT REFERENCES tickets(id),
  user_id TEXT REFERENCES users(id),
  started_at TEXT NOT NULL,
  stopped_at TEXT,
  duration_seconds INTEGER,
  notes TEXT,
  billable INTEGER DEFAULT 1
);

CREATE INDEX idx_timers_ticket ON work_timers(ticket_id);
CREATE INDEX idx_timers_user ON work_timers(user_id);

-- SLA Policies
CREATE TABLE IF NOT EXISTS sla_policies (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  priority TEXT NOT NULL,
  first_response_minutes INTEGER,
  resolution_hours INTEGER,
  business_hours_only INTEGER DEFAULT 1,
  active INTEGER DEFAULT 1
);

-- ═══════════════════════════════════════════════════════════════════
-- REPORTING
-- ═══════════════════════════════════════════════════════════════════

-- Saved Reports
CREATE TABLE IF NOT EXISTS saved_reports (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  parameters TEXT DEFAULT '{}', -- JSON
  schedule TEXT, -- cron expression
  last_run TEXT,
  created_by TEXT REFERENCES users(id),
  created_at TEXT DEFAULT (datetime('now'))
);

-- Report Snapshots
CREATE TABLE IF NOT EXISTS report_snapshots (
  id TEXT PRIMARY KEY,
  report_id TEXT REFERENCES saved_reports(id),
  data TEXT, -- JSON report data
  generated_at TEXT DEFAULT (datetime('now'))
);

-- ═══════════════════════════════════════════════════════════════════
-- INSERT DEFAULT DATA
-- ═══════════════════════════════════════════════════════════════════

-- Default SLA Policies
INSERT OR IGNORE INTO sla_policies (id, name, priority, first_response_minutes, resolution_hours) VALUES
  ('sla_critical', 'Critical', 'critical', 15, 4),
  ('sla_urgent', 'Urgent', 'urgent', 30, 8),
  ('sla_high', 'High', 'high', 60, 24),
  ('sla_normal', 'Normal', 'normal', 240, 48),
  ('sla_low', 'Low', 'low', 480, 72);

-- Default Business Hours (Mon-Sat 9am-6pm)
INSERT OR IGNORE INTO business_hours (id, day_of_week, open_time, close_time, is_closed) VALUES
  ('bh_sun', 0, '00:00', '00:00', 1),
  ('bh_mon', 1, '09:00', '18:00', 0),
  ('bh_tue', 2, '09:00', '18:00', 0),
  ('bh_wed', 3, '09:00', '18:00', 0),
  ('bh_thu', 4, '09:00', '18:00', 0),
  ('bh_fri', 5, '09:00', '18:00', 0),
  ('bh_sat', 6, '10:00', '16:00', 0);

-- Default Achievements
INSERT OR IGNORE INTO achievements (id, name, description, icon, xp_reward, rarity, condition) VALUES
  ('first_sim', 'First Steps', 'Complete your first simulation', '🎮', 100, 'common', '{"type":"count","target":1,"metric":"simulations_completed"}'),
  ('perfect_sim', 'Perfectionist', 'Complete a simulation with 100% score', '⭐', 500, 'rare', '{"type":"score","target":100,"metric":"simulation_score"}'),
  ('no_hints_master', 'Self Reliant', 'Complete a simulation without using any hints', '🧠', 300, 'uncommon', '{"type":"special","metric":"no_hints"}'),
  ('flawless', 'Flawless', 'Complete a simulation without any mistakes', '💎', 750, 'epic', '{"type":"special","metric":"no_mistakes"}'),
  ('speed_demon', 'Speed Demon', 'Complete a simulation in under 2 minutes', '⚡', 400, 'rare', '{"type":"time","target":120,"metric":"completion_time"}'),
  ('certified_tech', 'Certified Technician', 'Earn your first certification', '🏆', 1000, 'epic', '{"type":"count","target":1,"metric":"certifications"}'),
  ('streak_7', 'Week Warrior', 'Maintain a 7-day training streak', '🔥', 500, 'uncommon', '{"type":"streak","target":7,"metric":"daily_streak"}'),
  ('streak_30', 'Monthly Master', 'Maintain a 30-day training streak', '🌟', 2000, 'legendary', '{"type":"streak","target":30,"metric":"daily_streak"}');

-- Default Certifications
INSERT OR IGNORE INTO certifications (id, name, description, level, valid_months, badge_url) VALUES
  ('cert_basic', 'NoizyLab Basic Technician', 'Foundation certification for device repair', 1, 24, '/badges/basic.png'),
  ('cert_phone', 'Smartphone Specialist', 'Advanced certification for smartphone repairs', 2, 12, '/badges/phone.png'),
  ('cert_laptop', 'Laptop Specialist', 'Advanced certification for laptop repairs', 2, 12, '/badges/laptop.png'),
  ('cert_console', 'Game Console Specialist', 'Advanced certification for game console repairs', 2, 12, '/badges/console.png'),
  ('cert_micro', 'Microsoldering Expert', 'Expert certification for board-level repairs', 3, 12, '/badges/micro.png'),
  ('cert_master', 'NoizyLab Master Technician', 'Highest level of technical certification', 4, 12, '/badges/master.png');

PRAGMA optimize;
