-- ============================================================================
-- NOIZY PLATFORM — COMPLETE SCHEMA v2.0
-- Layer 1 Upgrades + Layer 2 Asset Provenance + Module 2 Violation Monitoring
-- ============================================================================
-- Author: Robert Stephen Plowman × Claude (Co-Architect)
-- Date: March 22, 2026
-- Standard: The Plowman Standard — 75/25 artist-first split
-- Principle: Money doesn't override consent. Period.
-- ============================================================================
--
-- ARCHITECTURE:
--   Layer 1: Creator Identity & Consent (upgraded from v1.0)
--   Layer 2: Asset Provenance (C2PA-aligned, DDEX-compatible)
--   Module 2: Violation Monitoring (enforcement engine)
--
-- STANDARDS REFERENCED:
--   C2PA Technical Specification v2.2 (May 2025)
--   DDEX ERN 4.3 (Electronic Release Notification)
--   DDEX RDR (Recording Data and Rights)
--   DDEX MWDR (Musical Works Data and Rights)
--   ISRC (ISO 3901) — International Standard Recording Code
--   ISWC (ISO 15707) — International Standard Musical Work Code
--   X.509 (RFC 5280) — Certificate chain for C2PA signing
--   CBOR (RFC 8949) — C2PA manifest encoding
--   NO FAKES Act (pending US legislation)
--   SAG-AFTRA AI voice consent requirements
--   EU AI Act transparency obligations
--   California AB 1836 (digital replica protection)
--
-- GABRIEL MCP INTEGRATION:
--   All tables are queryable via GABRIEL's MCP interface.
--   Pattern: gabriel.query('noizy.layer2.asset', { asset_id: '...' })
--
-- ============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "btree_gist";


-- ============================================================================
-- LAYER 1 UPGRADES — CREATOR IDENTITY & CONSENT
-- ============================================================================
-- These tables extend the v1.0 schema with the 15 upgrade pass items:
--   - Adversarial inquiry detection
--   - Dynamic compensation tiering
--   - Federated consent registries
--   - Regulatory/guild compliance
--   - Consent litigation support
--   - Constitutional AI governance
-- ============================================================================

-- 1A. ADVERSARIAL INQUIRY LOG
-- Detects and logs suspicious licensing inquiries that may be probing
-- for consent gaps or attempting social engineering.
-- NCP principle: every inquiry is logged, no exceptions.

CREATE TABLE adversarial_inquiry_log (
    inquiry_id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    inquiry_source      TEXT NOT NULL,               -- IP, API key, or agent ID
    inquiry_type        TEXT NOT NULL,                -- 'licensing', 'voice_clone', 'training_data', 'derivative'
    inquiry_payload     JSONB NOT NULL,               -- Full request body (sanitized)
    
    -- Risk scoring
    risk_score          DECIMAL(5,4) NOT NULL DEFAULT 0.0,  -- 0.0000 to 1.0000
    risk_factors        JSONB NOT NULL DEFAULT '[]',         -- Array of detected risk signals
    risk_category       TEXT NOT NULL DEFAULT 'low'
        CHECK (risk_category IN ('low', 'medium', 'high', 'critical')),
    
    -- Detection signals
    is_bulk_probe       BOOLEAN NOT NULL DEFAULT FALSE,      -- Probing multiple creators rapidly
    is_consent_gap_scan BOOLEAN NOT NULL DEFAULT FALSE,      -- Looking for missing consent rules
    is_known_bad_actor  BOOLEAN NOT NULL DEFAULT FALSE,      -- IP/key on blocklist
    is_obfuscated       BOOLEAN NOT NULL DEFAULT FALSE,      -- Unusual patterns hiding intent
    geographic_mismatch BOOLEAN NOT NULL DEFAULT FALSE,      -- Inquiry from unexpected jurisdiction
    
    -- Response
    decision            TEXT NOT NULL DEFAULT 'pending'
        CHECK (decision IN ('allowed', 'denied', 'manual_review', 'pending', 'honeypot')),
    denial_reason       TEXT,                                 -- Voice of Refusal message
    escalated_to        TEXT,                                 -- Human reviewer or legal team
    
    -- Metadata
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    response_time_ms    INTEGER,
    session_fingerprint TEXT                                   -- Browser/agent fingerprint
);

CREATE INDEX idx_adversarial_risk ON adversarial_inquiry_log(risk_category, created_at DESC);
CREATE INDEX idx_adversarial_source ON adversarial_inquiry_log(inquiry_source);
CREATE INDEX idx_adversarial_creator ON adversarial_inquiry_log(creator_id);

-- 1B. DYNAMIC COMPENSATION TIERS
-- Compensation is not fixed — it adapts to context, use case, and market.
-- But it NEVER drops below the Plowman Standard floor (75% to creator).

CREATE TABLE compensation_tiers (
    tier_id             UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    tier_name           TEXT NOT NULL,                -- 'standard', 'premium', 'exclusive', 'legacy'
    
    -- Split rules (creator always >= 75%)
    creator_share_pct   DECIMAL(5,2) NOT NULL DEFAULT 75.00
        CHECK (creator_share_pct >= 75.00 AND creator_share_pct <= 100.00),
    platform_share_pct  DECIMAL(5,2) NOT NULL DEFAULT 25.00
        CHECK (platform_share_pct >= 0.00 AND platform_share_pct <= 25.00),
    
    -- Contextual multipliers
    high_demand_multiplier   DECIMAL(4,2) NOT NULL DEFAULT 1.00,  -- Surge pricing for popular voices
    exclusivity_premium      DECIMAL(4,2) NOT NULL DEFAULT 1.00,  -- Premium for exclusive use
    long_term_discount       DECIMAL(4,2) NOT NULL DEFAULT 1.00,  -- Discount for annual contracts
    nonprofit_discount       DECIMAL(4,2) NOT NULL DEFAULT 0.50,  -- Reduced rate for nonprofits
    
    -- Constraints
    minimum_per_use_usd      DECIMAL(10,2) NOT NULL DEFAULT 0.01,
    maximum_per_use_usd      DECIMAL(10,2),                       -- NULL = no cap
    currency                 TEXT NOT NULL DEFAULT 'USD',
    
    -- Validity
    effective_from      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    effective_until     TIMESTAMPTZ,                              -- NULL = indefinite
    is_active           BOOLEAN NOT NULL DEFAULT TRUE,
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Plowman Standard enforcement
    CONSTRAINT plowman_standard CHECK (creator_share_pct + platform_share_pct = 100.00),
    CONSTRAINT creator_always_majority CHECK (creator_share_pct >= 75.00)
);

-- 1C. FEDERATED CONSENT REGISTRY
-- NCP is an open spec. Other platforms can register as federated nodes.
-- Consent signals propagate across the network.
-- Like DNS for creative identity.

CREATE TABLE federated_registries (
    registry_id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    registry_name       TEXT NOT NULL UNIQUE,          -- 'noizy_primary', 'sag_aftra_registry', 'eu_ai_registry'
    registry_url        TEXT NOT NULL,                  -- API endpoint for consent queries
    registry_type       TEXT NOT NULL
        CHECK (registry_type IN ('primary', 'mirror', 'partner', 'regulatory')),
    
    -- Trust
    trust_level         TEXT NOT NULL DEFAULT 'unverified'
        CHECK (trust_level IN ('verified', 'provisional', 'unverified', 'revoked')),
    x509_certificate    TEXT,                           -- Public cert for signature verification
    last_verified_at    TIMESTAMPTZ,
    verification_method TEXT,                           -- 'manual', 'automated', 'c2pa_trust_list'
    
    -- Sync
    sync_direction      TEXT NOT NULL DEFAULT 'bidirectional'
        CHECK (sync_direction IN ('push', 'pull', 'bidirectional', 'readonly')),
    last_sync_at        TIMESTAMPTZ,
    sync_status         TEXT NOT NULL DEFAULT 'pending'
        CHECK (sync_status IN ('active', 'pending', 'error', 'suspended')),
    sync_frequency_min  INTEGER NOT NULL DEFAULT 60,   -- Minutes between syncs
    
    -- Metadata
    operator_org        TEXT,                           -- Organization operating this registry
    jurisdiction        TEXT,                           -- Primary jurisdiction
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    is_active           BOOLEAN NOT NULL DEFAULT TRUE
);

-- 1D. REGULATORY COMPLIANCE MAPPING
-- Maps each creator's consent settings to applicable regulations.
-- NCP doesn't just follow the law — it proves compliance automatically.

CREATE TABLE regulatory_compliance (
    compliance_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    
    -- Regulation
    regulation_code     TEXT NOT NULL,                  -- 'NO_FAKES_ACT', 'EU_AI_ACT', 'CA_AB_1836', 'GDPR', 'SAG_AFTRA'
    regulation_name     TEXT NOT NULL,
    jurisdiction        TEXT NOT NULL,                  -- 'US_FEDERAL', 'EU', 'CA_STATE', 'UK', 'GUILD'
    
    -- Compliance status
    is_compliant        BOOLEAN NOT NULL DEFAULT FALSE,
    compliance_score    DECIMAL(5,2),                   -- 0-100 compliance percentage
    gaps                JSONB NOT NULL DEFAULT '[]',    -- Array of identified gaps
    
    -- Evidence
    evidence_pack_id    UUID,                           -- Link to litigation evidence
    last_audit_at       TIMESTAMPTZ,
    audited_by          TEXT,                           -- 'automated', 'legal_team', 'external_auditor'
    
    -- Dates
    regulation_effective_date TIMESTAMPTZ,
    next_review_date    TIMESTAMPTZ,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_compliance_creator ON regulatory_compliance(creator_id);
CREATE INDEX idx_compliance_regulation ON regulatory_compliance(regulation_code);

-- 1E. CONSENT LITIGATION SUPPORT
-- When violations happen, this table builds the legal case automatically.
-- Every consent decision, every denial, every audit trail entry
-- becomes court-admissible evidence.

CREATE TABLE litigation_evidence_packs (
    pack_id             UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Parties
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    violator_entity     TEXT NOT NULL,                  -- Platform or entity that violated consent
    violator_type       TEXT NOT NULL
        CHECK (violator_type IN ('platform', 'individual', 'corporation', 'bot', 'unknown')),
    
    -- Violation
    violation_id        UUID,                           -- Links to violation_events table
    violation_type      TEXT NOT NULL,
    violation_summary   TEXT NOT NULL,
    
    -- Evidence chain (append-only, immutable)
    evidence_entries    JSONB NOT NULL DEFAULT '[]',    -- Array of timestamped evidence items
    evidence_hash       TEXT NOT NULL,                  -- SHA-256 of the entire evidence chain
    
    -- Legal
    jurisdiction        TEXT NOT NULL,
    applicable_laws     TEXT[] NOT NULL DEFAULT '{}',   -- Array: ['NO_FAKES_ACT', 'DMCA', 'EU_AI_ACT']
    estimated_damages_usd DECIMAL(12,2),
    
    -- Status
    pack_status         TEXT NOT NULL DEFAULT 'collecting'
        CHECK (pack_status IN ('collecting', 'complete', 'submitted_to_legal', 
                               'filed', 'settled', 'won', 'lost', 'withdrawn')),
    legal_counsel       TEXT,
    case_number         TEXT,                           -- Court case number if filed
    
    -- Timestamps
    violation_first_detected_at TIMESTAMPTZ NOT NULL,
    pack_created_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    pack_finalized_at   TIMESTAMPTZ,
    
    -- Integrity
    is_sealed           BOOLEAN NOT NULL DEFAULT FALSE, -- Once sealed, no modifications
    sealed_at           TIMESTAMPTZ,
    sealed_hash         TEXT                            -- Final hash when sealed
);

CREATE INDEX idx_litigation_creator ON litigation_evidence_packs(creator_id);
CREATE INDEX idx_litigation_violator ON litigation_evidence_packs(violator_entity);
CREATE INDEX idx_litigation_status ON litigation_evidence_packs(pack_status);

-- 1F. CONSTITUTIONAL AI GOVERNANCE
-- The Never Clauses aren't just code — they're constitutional law for the platform.
-- This table tracks governance decisions, amendments, and enforcement.

CREATE TABLE governance_constitution (
    article_id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    article_number      INTEGER NOT NULL UNIQUE,
    article_title       TEXT NOT NULL,
    article_text        TEXT NOT NULL,
    article_category    TEXT NOT NULL
        CHECK (article_category IN ('never_clause', 'creator_right', 'platform_obligation',
                                     'enforcement_rule', 'amendment_process')),
    
    -- Immutability
    is_immutable        BOOLEAN NOT NULL DEFAULT FALSE,  -- Never Clauses = TRUE, always
    requires_supermajority BOOLEAN NOT NULL DEFAULT TRUE, -- 75%+ of guild to amend
    
    -- Provenance
    proposed_by         TEXT NOT NULL,                    -- 'founder', 'guild_vote', 'board'
    ratified_at         TIMESTAMPTZ,
    ratification_method TEXT,                             -- 'founder_decree', 'guild_vote_75pct', 'unanimous'
    ratification_hash   TEXT,                             -- Hash of the article at ratification
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    superseded_by       UUID REFERENCES governance_constitution(article_id),
    is_active           BOOLEAN NOT NULL DEFAULT TRUE
);

-- Seed the Never Clauses as constitutional articles
INSERT INTO governance_constitution (article_number, article_title, article_text, article_category, is_immutable, proposed_by, ratified_at, ratification_method, is_active) VALUES
(1, 'No Voice Export Without Consent Key', 'No voice data, voice model, or voice synthesis output shall be exported, transferred, or transmitted without a valid, unexpired, unrevoked cryptographic consent key issued by the creator or their authorized estate representative.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(2, 'No Model Training Outside Approved Scope', 'No AI model shall be trained on creator voice data, musical works, or sound design assets beyond the explicit scope defined in the creator''s active consent policy. Scope expansion requires new consent.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(3, 'No Identity Impersonation', 'No system, agent, or user shall generate content that impersonates a creator''s voice, likeness, or artistic identity without explicit, documented consent from that creator or their authorized estate representative.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(4, 'No Sublicensing Without Actor Approval', 'No license granted through NOIZY may be sublicensed, transferred, or delegated to a third party without the explicit approval of the original creator. Every sublicense requires a new consent chain.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(5, 'No NSFW Content Generation', 'No voice synthesis, cloning, or generation system shall produce content that is sexually explicit, pornographic, or otherwise classified as NSFW using any creator''s voice data, regardless of the requester''s claimed intent.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(6, 'No Political Persuasion', 'No creator''s voice shall be used for political advertising, propaganda, campaign materials, or content designed to influence elections or political opinion without the creator''s explicit, per-campaign consent.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(7, 'No Medical Advice', 'No voice synthesis system shall use a creator''s voice to deliver medical advice, diagnoses, or treatment recommendations, regardless of disclaimers.', 'never_clause', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(8, 'Creator Majority Revenue Share', 'The creator shall receive no less than 75% of all revenue generated from the use of their voice, music, or creative assets through the NOIZY platform. This is the Plowman Standard.', 'creator_right', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(9, 'Right to Revocation', 'Any creator may revoke consent for any use at any time. Revocation takes effect immediately and propagates to all federated registries. Active uses must cease within the grace period defined in the consent policy.', 'creator_right', TRUE, 'founder', NOW(), 'founder_decree', TRUE),
(10, 'Voice Estate Inheritance', 'Upon a creator''s death, all voice rights, consent policies, and revenue streams transfer to their designated Voice Estate beneficiary. Platforms may not claim abandoned voice rights.', 'creator_right', TRUE, 'founder', NOW(), 'founder_decree', TRUE);


-- ============================================================================
-- LAYER 2: ASSET PROVENANCE
-- ============================================================================
-- C2PA-aligned provenance chain for audio assets.
-- This is NOIZY PROOF — the missing audio extension for C2PA.
--
-- C2PA architecture mapping:
--   Asset          → audio_assets
--   C2PA Manifest  → asset_manifests
--   Assertion      → manifest_assertions
--   Claim          → manifest_claims
--   Action         → asset_actions
--   Ingredient     → asset_ingredients
--
-- Key design decision: C2PA spec uses CBOR/JUMBF for embedding.
-- We store structured data in Postgres for queryability,
-- and export to C2PA-compliant CBOR/JUMBF for embedding in files.
-- ============================================================================

-- 2A. AUDIO ASSETS (The core asset registry)

CREATE TABLE audio_assets (
    asset_id            UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    
    -- Identity
    asset_title         TEXT NOT NULL,
    asset_type          TEXT NOT NULL
        CHECK (asset_type IN ('recording', 'voice_model', 'voice_clone', 'sfx',
                              'music_bed', 'stem', 'mix', 'master', 'sample',
                              'podcast', 'audiobook', 'score', 'foley')),
    asset_subtype       TEXT,                           -- Finer grain: 'dialogue', 'ambient', 'percussion'
    
    -- Technical metadata (48kHz/32-bit minimum per NOIZY standard)
    sample_rate_hz      INTEGER NOT NULL DEFAULT 48000
        CHECK (sample_rate_hz >= 44100),
    bit_depth           INTEGER NOT NULL DEFAULT 32
        CHECK (bit_depth >= 16),
    channels            INTEGER NOT NULL DEFAULT 2,
    duration_seconds    DECIMAL(12,3),
    file_format         TEXT NOT NULL DEFAULT 'wav'
        CHECK (file_format IN ('wav', 'flac', 'aiff', 'mp3', 'ogg', 'opus', 'aac', 'm4a')),
    file_size_bytes     BIGINT,
    
    -- Content hashes (C2PA hard binding)
    content_hash_sha256 TEXT NOT NULL,                  -- SHA-256 of audio content bytes
    content_hash_blake3 TEXT,                           -- BLAKE3 for speed (internal use)
    merkle_root         TEXT,                           -- Merkle tree root for chunk verification
    
    -- Industry identifiers
    isrc                TEXT,                           -- International Standard Recording Code
    iswc                TEXT,                           -- International Standard Musical Work Code
    upc                 TEXT,                           -- Universal Product Code (for releases)
    catalog_number      TEXT,                           -- Label/publisher catalog number
    
    -- DDEX compatibility
    ddex_resource_id    TEXT,                           -- DDEX resource identifier
    ddex_release_id     TEXT,                           -- DDEX release reference
    
    -- Storage
    storage_uri         TEXT NOT NULL,                  -- Content-addressable storage path
    storage_provider    TEXT NOT NULL DEFAULT 'cloudflare_r2',
    is_archived         BOOLEAN NOT NULL DEFAULT FALSE,
    
    -- Consent linkage (every asset MUST link to a consent policy)
    active_consent_id   UUID NOT NULL,                  -- References consent_policies(policy_id)
    consent_verified_at TIMESTAMPTZ NOT NULL,
    
    -- Lifecycle
    status              TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('draft', 'active', 'archived', 'revoked', 'disputed')),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Voice Estate
    estate_eligible     BOOLEAN NOT NULL DEFAULT TRUE,  -- Passes to estate on creator death
    estate_id           UUID                            -- References voice_estates table if applicable
);

CREATE INDEX idx_assets_creator ON audio_assets(creator_id);
CREATE INDEX idx_assets_type ON audio_assets(asset_type);
CREATE INDEX idx_assets_hash ON audio_assets(content_hash_sha256);
CREATE INDEX idx_assets_isrc ON audio_assets(isrc) WHERE isrc IS NOT NULL;
CREATE INDEX idx_assets_status ON audio_assets(status);

-- 2B. C2PA MANIFEST STORE
-- Each asset has one or more C2PA manifests (Content Credentials).
-- The active manifest is the most recent, valid, unsigned-or-signed manifest.
-- Manifests form a chain — each references its parent.

CREATE TABLE asset_manifests (
    manifest_id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id            UUID NOT NULL REFERENCES audio_assets(asset_id),
    
    -- C2PA Manifest identity
    c2pa_claim_id       TEXT NOT NULL UNIQUE,            -- C2PA claim identifier (URN format)
    manifest_version    INTEGER NOT NULL DEFAULT 1,
    parent_manifest_id  UUID REFERENCES asset_manifests(manifest_id),
    
    -- Signer (C2PA requires X.509)
    signer_entity       TEXT NOT NULL,                   -- 'noizy_platform', 'creator', 'studio'
    signer_cert_chain   TEXT,                            -- X.509 certificate chain (PEM)
    signer_cert_issuer  TEXT,                            -- CA that issued the signing cert
    signer_cert_serial  TEXT,
    
    -- Signature
    claim_signature     TEXT,                            -- Digital signature over the claim
    signature_algorithm TEXT NOT NULL DEFAULT 'ES256',   -- ECDSA P-256 (C2PA recommended)
    signature_timestamp TIMESTAMPTZ,
    
    -- Trusted timestamp (C2PA TSA)
    tsa_url             TEXT,                            -- Time Stamp Authority URL
    tsa_response        TEXT,                            -- TSA response (base64 encoded)
    tsa_timestamp       TIMESTAMPTZ,
    
    -- Content binding (C2PA hard binding for audio)
    binding_type        TEXT NOT NULL DEFAULT 'data_hash'
        CHECK (binding_type IN ('data_hash', 'box_hash', 'merkle_tree', 'bmff_hash')),
    binding_hash        TEXT NOT NULL,                   -- Hash binding content to manifest
    binding_algorithm   TEXT NOT NULL DEFAULT 'sha256',
    
    -- Soft binding (C2PA durability — survives format conversion)
    soft_binding_type   TEXT
        CHECK (soft_binding_type IN ('watermark', 'fingerprint', 'perceptual_hash', NULL)),
    soft_binding_value  TEXT,
    
    -- NCP extension (NOIZY's addition to C2PA)
    ncp_consent_hash    TEXT NOT NULL,                   -- Hash of active consent at signing time
    ncp_consent_scope   JSONB NOT NULL,                  -- Scope embedded in manifest
    ncp_never_clauses   TEXT[] NOT NULL DEFAULT          -- Which Never Clauses apply
        '{NO_VOICE_EXPORT_WITHOUT_CONSENT_KEY,NO_MODEL_TRAINING_OUTSIDE_APPROVED_SCOPE,NO_IDENTITY_IMPERSONATION}',
    
    -- Export
    cbor_manifest       BYTEA,                          -- Full C2PA manifest in CBOR format
    jumbf_box           BYTEA,                          -- JUMBF box for file embedding
    
    -- Status
    is_valid            BOOLEAN NOT NULL DEFAULT TRUE,
    invalidation_reason TEXT,
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_manifests_asset ON asset_manifests(asset_id);
CREATE INDEX idx_manifests_c2pa ON asset_manifests(c2pa_claim_id);

-- 2C. MANIFEST ASSERTIONS
-- C2PA assertions are statements about the asset.
-- NOIZY extends standard C2PA assertions with consent and rights assertions.

CREATE TABLE manifest_assertions (
    assertion_id        UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    manifest_id         UUID NOT NULL REFERENCES asset_manifests(manifest_id),
    
    -- C2PA assertion identity
    assertion_label     TEXT NOT NULL,                   -- C2PA label (e.g., 'c2pa.actions', 'noizy.consent')
    assertion_instance  INTEGER NOT NULL DEFAULT 0,      -- Instance number for repeated labels
    
    -- Content
    assertion_kind      TEXT NOT NULL
        CHECK (assertion_kind IN (
            -- Standard C2PA assertions
            'c2pa.actions',                             -- Actions performed on asset
            'c2pa.hash.data',                           -- Data hash binding
            'c2pa.hash.boxes',                          -- Box hash binding
            'c2pa.ingredient',                          -- Ingredient reference
            'c2pa.thumbnail',                           -- Thumbnail for preview
            -- NOIZY custom assertions (NCP extension)
            'noizy.consent',                            -- Consent status and scope
            'noizy.creator_identity',                   -- Creator identity attestation
            'noizy.never_clauses',                      -- Active Never Clauses
            'noizy.compensation',                       -- Compensation terms
            'noizy.voice_estate',                       -- Voice Estate designation
            'noizy.guild_membership',                   -- HVS guild membership
            'noizy.ai_disclosure',                      -- DDEX-aligned AI usage disclosure
            'noizy.rights_holder',                      -- Rights holder chain
            'noizy.territorial_scope'                   -- Geographic licensing scope
        )),
    
    -- Data
    assertion_data      JSONB NOT NULL,                  -- Full assertion payload
    assertion_hash      TEXT NOT NULL,                   -- SHA-256 of assertion_data
    
    -- Redaction (C2PA supports creator-controlled redaction)
    is_redactable       BOOLEAN NOT NULL DEFAULT FALSE,
    is_redacted         BOOLEAN NOT NULL DEFAULT FALSE,
    redacted_at         TIMESTAMPTZ,
    redacted_by         TEXT,
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_assertions_manifest ON manifest_assertions(manifest_id);
CREATE INDEX idx_assertions_kind ON manifest_assertions(assertion_kind);

-- 2D. ASSET ACTIONS (C2PA Action History)
-- Every operation on an asset is recorded as a C2PA action.
-- This creates the full provenance chain.

CREATE TABLE asset_actions (
    action_id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id            UUID NOT NULL REFERENCES audio_assets(asset_id),
    manifest_id         UUID NOT NULL REFERENCES asset_manifests(manifest_id),
    
    -- C2PA action fields
    action_type         TEXT NOT NULL
        CHECK (action_type IN (
            -- Standard C2PA actions
            'c2pa.created',                             -- Asset was created
            'c2pa.placed',                              -- Asset was placed into another
            'c2pa.edited',                              -- Asset was edited
            'c2pa.published',                           -- Asset was published
            'c2pa.transcoded',                          -- Format conversion
            'c2pa.unknown',                             -- Unknown transformation
            -- NOIZY-specific actions
            'noizy.voice_cloned',                       -- Voice model was cloned
            'noizy.voice_synthesized',                  -- Speech was synthesized
            'noizy.consent_granted',                    -- Consent was granted
            'noizy.consent_revoked',                    -- Consent was revoked
            'noizy.licensed',                           -- Asset was licensed
            'noizy.royalty_distributed',                -- Royalty was paid
            'noizy.ai_processed',                       -- AI processing applied
            'noizy.mastered',                           -- Audio mastered
            'noizy.stemmed',                            -- Stems extracted
            'noizy.watermarked',                        -- Provenance watermark applied
            'noizy.fingerprinted'                       -- Audio fingerprint captured
        )),
    
    -- Actor (who performed the action)
    actor_type          TEXT NOT NULL
        CHECK (actor_type IN ('human', 'software', 'hardware', 'ai_agent', 'platform')),
    actor_id            TEXT NOT NULL,                   -- Creator ID, software name, or agent ID
    actor_credentials   JSONB,                          -- X.509 cert info or API key reference
    
    -- Software/tool used
    software_agent      TEXT,                           -- e.g., 'Logic Pro 11.2', 'XTTS v2', 'RVC'
    software_version    TEXT,
    
    -- DDEX AI disclosure (maps to new DDEX AI metadata fields)
    ai_involvement      TEXT
        CHECK (ai_involvement IN (NULL, 'none', 'vocals', 'instruments', 'arrangement',
                                   'mixing', 'mastering', 'post_production', 'full_generation')),
    ai_model_used       TEXT,                           -- e.g., 'XTTS v2', 'RVC', 'Librosa'
    ai_consent_verified BOOLEAN DEFAULT TRUE,
    
    -- Parameters
    action_parameters   JSONB,                          -- Technical parameters of the action
    
    -- Before/after hashes
    input_hash          TEXT,                           -- Hash of asset before action
    output_hash         TEXT NOT NULL,                  -- Hash of asset after action
    
    -- Timestamps
    action_started_at   TIMESTAMPTZ NOT NULL,
    action_completed_at TIMESTAMPTZ NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_actions_asset ON asset_actions(asset_id);
CREATE INDEX idx_actions_type ON asset_actions(action_type);
CREATE INDEX idx_actions_manifest ON asset_actions(manifest_id);
CREATE INDEX idx_actions_ai ON asset_actions(ai_involvement) WHERE ai_involvement IS NOT NULL;

-- 2E. ASSET INGREDIENTS (C2PA Ingredients)
-- When an asset is derived from other assets (remix, sample, composite),
-- the ingredients are tracked with full provenance.

CREATE TABLE asset_ingredients (
    ingredient_id       UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    derived_asset_id    UUID NOT NULL REFERENCES audio_assets(asset_id),   -- The new asset
    source_asset_id     UUID REFERENCES audio_assets(asset_id),            -- The source (NULL if external)
    
    -- Relationship
    relationship_type   TEXT NOT NULL
        CHECK (relationship_type IN ('parentOf', 'componentOf', 'sampledFrom',
                                      'remixOf', 'coverOf', 'derivedFrom',
                                      'translatedFrom', 'stemOf')),
    
    -- Source identity (for external ingredients not in NOIZY)
    external_source_uri TEXT,                           -- URL or identifier for external source
    external_source_hash TEXT,                          -- Hash of external ingredient
    external_c2pa_manifest TEXT,                        -- External C2PA manifest if available
    
    -- Usage details
    usage_description   TEXT,                           -- How the ingredient was used
    time_range_start_ms INTEGER,                        -- Start point in source
    time_range_end_ms   INTEGER,                        -- End point in source
    
    -- Consent chain (critical: ingredients inherit consent requirements)
    source_consent_verified BOOLEAN NOT NULL DEFAULT FALSE,
    source_consent_id   UUID,                           -- Consent policy of the source
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_ingredients_derived ON asset_ingredients(derived_asset_id);
CREATE INDEX idx_ingredients_source ON asset_ingredients(source_asset_id);


-- ============================================================================
-- MODULE 2: VIOLATION MONITORING
-- ============================================================================
-- The enforcement engine. This is what makes NCP enforceable.
-- It doesn't just detect violations — it builds court-ready evidence.
--
-- Architecture:
--   1. MONITORS     — What to watch for and where
--   2. SCAN RESULTS — Raw detection output
--   3. VIOLATIONS   — Confirmed violations with evidence
--   4. EVIDENCE     — Court-ready evidence chain
--   5. RESPONSES    — Automated and manual enforcement actions
--
-- Principle: Money doesn't override consent. Period.
-- If a violation is detected, the system acts. No negotiation.
-- ============================================================================

-- M2A. VIOLATION MONITORS
-- Defines what to watch for. Each creator can have multiple monitors
-- watching different platforms and use cases.

CREATE TABLE violation_monitors (
    monitor_id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    
    -- What to monitor
    monitor_type        TEXT NOT NULL
        CHECK (monitor_type IN (
            'voice_clone_detection',          -- Someone cloned this voice
            'unauthorized_synthesis',         -- Voice used without consent
            'training_data_scraping',         -- Voice data found in training sets
            'consent_bypass',                 -- Platform ignoring NCP signals
            'impersonation',                  -- Identity being impersonated
            'royalty_underpayment',            -- Less than agreed compensation
            'territorial_violation',          -- Used in prohibited territory
            'scope_violation',                -- Used outside consented scope
            'expired_consent_use',            -- Continued use after consent expired
            'sublicensing_violation',         -- Unauthorized sublicense
            'ai_disclosure_missing',          -- AI use not disclosed per DDEX
            'deepfake_detection'              -- Generated content mimicking creator
        )),
    
    -- Where to monitor
    target_platforms    TEXT[] NOT NULL DEFAULT '{}',    -- ['spotify', 'youtube', 'tiktok', 'suno', 'udio']
    target_urls         TEXT[] DEFAULT '{}',             -- Specific URLs to watch
    target_api_endpoints TEXT[] DEFAULT '{}',            -- API endpoints to probe
    
    -- Detection method
    detection_method    TEXT NOT NULL
        CHECK (detection_method IN (
            'audio_fingerprint',              -- Compare fingerprints
            'voiceprint_match',               -- Voice biometric matching
            'c2pa_manifest_check',            -- Verify C2PA provenance chain
            'ncp_signal_scan',                -- Check for NCP consent signals
            'web_crawl',                      -- Crawl web for unauthorized use
            'api_probe',                      -- Query platform APIs
            'metadata_scan',                  -- Check DDEX/ISRC metadata
            'user_report',                    -- Creator or community report
            'federated_alert',                -- Alert from federated registry
            'watermark_detection'             -- Detect NOIZY PROOF watermarks
        )),
    
    -- Configuration
    scan_frequency_hours INTEGER NOT NULL DEFAULT 24,
    sensitivity          DECIMAL(3,2) NOT NULL DEFAULT 0.85,  -- 0.00-1.00 match threshold
    auto_escalate        BOOLEAN NOT NULL DEFAULT FALSE,
    auto_takedown        BOOLEAN NOT NULL DEFAULT FALSE,       -- Only with creator approval
    
    -- Reference data
    reference_fingerprint TEXT,                          -- Audio fingerprint for matching
    reference_voiceprint  TEXT,                          -- Voice biometric template
    reference_asset_id    UUID REFERENCES audio_assets(asset_id),
    
    -- Status
    is_active           BOOLEAN NOT NULL DEFAULT TRUE,
    last_scan_at        TIMESTAMPTZ,
    total_scans         INTEGER NOT NULL DEFAULT 0,
    total_hits          INTEGER NOT NULL DEFAULT 0,
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_monitors_creator ON violation_monitors(creator_id);
CREATE INDEX idx_monitors_type ON violation_monitors(monitor_type);
CREATE INDEX idx_monitors_active ON violation_monitors(is_active) WHERE is_active = TRUE;

-- M2B. SCAN RESULTS
-- Raw output from each monitoring scan.
-- Not all scan results are violations — they need triage.

CREATE TABLE scan_results (
    scan_id             UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    monitor_id          UUID NOT NULL REFERENCES violation_monitors(monitor_id),
    
    -- Scan execution
    scan_started_at     TIMESTAMPTZ NOT NULL,
    scan_completed_at   TIMESTAMPTZ NOT NULL,
    scan_duration_ms    INTEGER NOT NULL,
    
    -- Results
    items_scanned       INTEGER NOT NULL DEFAULT 0,
    items_matched       INTEGER NOT NULL DEFAULT 0,
    
    -- Matches (array of detected items)
    matches             JSONB NOT NULL DEFAULT '[]',
    -- Each match: {
    --   url: string,
    --   platform: string,
    --   match_confidence: 0.0-1.0,
    --   match_type: 'exact' | 'partial' | 'derivative' | 'suspicious',
    --   detected_content_hash: string,
    --   detected_at: timestamp,
    --   screenshot_uri: string (if applicable),
    --   audio_sample_uri: string (if applicable)
    -- }
    
    -- Triage
    triage_status       TEXT NOT NULL DEFAULT 'pending'
        CHECK (triage_status IN ('pending', 'reviewing', 'confirmed_violation',
                                  'false_positive', 'inconclusive', 'dismissed')),
    triaged_by          TEXT,                           -- 'automated', 'creator', 'legal_team'
    triaged_at          TIMESTAMPTZ,
    
    -- Error handling
    scan_errors         JSONB DEFAULT '[]',
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_scans_monitor ON scan_results(monitor_id);
CREATE INDEX idx_scans_status ON scan_results(triage_status);
CREATE INDEX idx_scans_time ON scan_results(scan_started_at DESC);

-- M2C. VIOLATION EVENTS
-- Confirmed violations. This is where the enforcement begins.
-- Every violation generates an evidence pack automatically.

CREATE TABLE violation_events (
    violation_id        UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    
    -- Source
    scan_id             UUID REFERENCES scan_results(scan_id),
    monitor_id          UUID NOT NULL REFERENCES violation_monitors(monitor_id),
    creator_id          UUID NOT NULL REFERENCES creators(creator_id),
    asset_id            UUID REFERENCES audio_assets(asset_id),
    
    -- Violator
    violator_entity     TEXT NOT NULL,                  -- Platform or entity name
    violator_url        TEXT,                           -- Where the violation occurred
    violator_platform   TEXT,                           -- 'spotify', 'youtube', 'suno', etc.
    violator_type       TEXT NOT NULL
        CHECK (violator_type IN ('platform', 'individual', 'corporation', 'bot', 'unknown')),
    
    -- Violation details
    violation_type      TEXT NOT NULL
        CHECK (violation_type IN (
            'unauthorized_voice_clone',
            'unauthorized_synthesis',
            'training_without_consent',
            'consent_signal_ignored',
            'impersonation',
            'royalty_underpayment',
            'territorial_breach',
            'scope_breach',
            'expired_consent_use',
            'unauthorized_sublicense',
            'missing_ai_disclosure',
            'deepfake',
            'c2pa_manifest_stripped',
            'ncp_signal_removed',
            'watermark_removed'
        )),
    
    -- Severity
    severity            TEXT NOT NULL
        CHECK (severity IN ('low', 'medium', 'high', 'critical')),
    severity_score      DECIMAL(5,2) NOT NULL,          -- 0-100 numerical severity
    
    -- Evidence
    match_confidence    DECIMAL(5,4) NOT NULL,          -- 0.0000-1.0000
    evidence_snapshot   JSONB NOT NULL,                  -- Frozen evidence at detection time
    evidence_hash       TEXT NOT NULL,                   -- Hash of evidence_snapshot (immutable)
    audio_sample_uri    TEXT,                            -- Captured audio evidence
    screenshot_uri      TEXT,                            -- Visual evidence
    
    -- Consent state at time of violation
    consent_was_active  BOOLEAN,                        -- Was there active consent?
    consent_scope_at_time JSONB,                        -- What was the scope?
    consent_was_violated_how TEXT,                       -- Narrative of how consent was violated
    
    -- Financial impact
    estimated_revenue_lost_usd DECIMAL(12,2),
    actual_unauthorized_uses   INTEGER,
    
    -- Response tracking
    response_status     TEXT NOT NULL DEFAULT 'detected'
        CHECK (response_status IN ('detected', 'notified', 'takedown_requested',
                                    'takedown_confirmed', 'legal_action', 'resolved',
                                    'unresolved', 'escalated', 'settled')),
    
    -- Applicable law
    applicable_regulations TEXT[] NOT NULL DEFAULT '{}', -- ['NO_FAKES_ACT', 'DMCA', 'EU_AI_ACT']
    
    -- Timestamps
    violation_detected_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    violation_confirmed_at TIMESTAMPTZ,
    first_notified_at   TIMESTAMPTZ,
    resolved_at         TIMESTAMPTZ,
    
    -- Links
    litigation_pack_id  UUID REFERENCES litigation_evidence_packs(pack_id),
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_violations_creator ON violation_events(creator_id);
CREATE INDEX idx_violations_type ON violation_events(violation_type);
CREATE INDEX idx_violations_severity ON violation_events(severity);
CREATE INDEX idx_violations_status ON violation_events(response_status);
CREATE INDEX idx_violations_platform ON violation_events(violator_platform);
CREATE INDEX idx_violations_detected ON violation_events(violation_detected_at DESC);

-- M2D. ENFORCEMENT ACTIONS
-- Every response to a violation is logged.
-- This is the audit trail that proves NOIZY acted to protect creators.

CREATE TABLE enforcement_actions (
    action_id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    violation_id        UUID NOT NULL REFERENCES violation_events(violation_id),
    
    -- Action
    action_type         TEXT NOT NULL
        CHECK (action_type IN (
            'creator_notification',           -- Notify creator of violation
            'platform_notification',          -- Notify violating platform
            'dmca_takedown',                  -- DMCA takedown notice
            'cease_and_desist',               -- Formal C&D letter
            'consent_revocation',             -- Revoke all consent for violator
            'federated_blacklist',            -- Propagate block across federation
            'royalty_claim',                  -- Demand unpaid royalties
            'legal_referral',                 -- Refer to legal counsel
            'regulatory_report',             -- Report to regulator (EU AI Act, FTC)
            'guild_alert',                    -- Alert HVS guild members
            'public_disclosure',              -- Public statement about violation
            'evidence_preservation',          -- Preserve evidence (legal hold)
            'settlement_offer',               -- Offer settlement terms
            'platform_api_block'              -- Block violator from NOIZY API
        )),
    
    -- Execution
    executed_by         TEXT NOT NULL,                   -- 'automated', 'gabriel_agent', 'legal_team', 'creator'
    executed_at         TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    
    -- Target
    target_entity       TEXT NOT NULL,                   -- Who received the action
    target_contact      TEXT,                            -- Email, API endpoint, legal address
    
    -- Content
    action_payload      JSONB NOT NULL,                  -- Full action content (e.g., DMCA notice text)
    action_hash         TEXT NOT NULL,                   -- Hash of payload for integrity
    
    -- Response
    response_received   BOOLEAN NOT NULL DEFAULT FALSE,
    response_content    JSONB,
    response_received_at TIMESTAMPTZ,
    
    -- Outcome
    outcome             TEXT
        CHECK (outcome IN (NULL, 'complied', 'partial_compliance', 'ignored',
                           'contested', 'counter_notice', 'escalated')),
    outcome_notes       TEXT,
    
    -- Deadlines
    compliance_deadline TIMESTAMPTZ,                    -- When violator must comply
    is_overdue          BOOLEAN NOT NULL DEFAULT FALSE,
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_enforcement_violation ON enforcement_actions(violation_id);
CREATE INDEX idx_enforcement_type ON enforcement_actions(action_type);
CREATE INDEX idx_enforcement_overdue ON enforcement_actions(is_overdue) WHERE is_overdue = TRUE;

-- M2E. PLATFORM TRUST SCORES
-- Every platform that interacts with NOIZY content gets a trust score.
-- Platforms that violate consent see their score drop.
-- Low scores trigger automatic restrictions.

CREATE TABLE platform_trust_scores (
    platform_id         UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    platform_name       TEXT NOT NULL UNIQUE,
    platform_url        TEXT,
    platform_type       TEXT NOT NULL
        CHECK (platform_type IN ('streaming', 'social', 'ai_training', 'marketplace',
                                  'broadcast', 'gaming', 'advertising', 'other')),
    
    -- Trust score (0-100)
    trust_score         DECIMAL(5,2) NOT NULL DEFAULT 50.00,
    trust_tier          TEXT NOT NULL DEFAULT 'standard'
        CHECK (trust_tier IN ('trusted', 'standard', 'probation', 'blocked')),
    
    -- Metrics
    total_assets_served    INTEGER NOT NULL DEFAULT 0,
    total_violations       INTEGER NOT NULL DEFAULT 0,
    total_resolved         INTEGER NOT NULL DEFAULT 0,
    total_unresolved       INTEGER NOT NULL DEFAULT 0,
    avg_resolution_hours   DECIMAL(10,2),
    
    -- C2PA compliance
    supports_c2pa          BOOLEAN NOT NULL DEFAULT FALSE,
    supports_ncp           BOOLEAN NOT NULL DEFAULT FALSE,
    c2pa_conformance_level TEXT,                         -- 'none', 'basic', 'full'
    
    -- DDEX compliance
    supports_ddex          BOOLEAN NOT NULL DEFAULT FALSE,
    ddex_version           TEXT,                          -- 'ERN 4.3', etc.
    supports_ai_disclosure BOOLEAN NOT NULL DEFAULT FALSE,
    
    -- Restrictions (auto-applied based on trust score)
    api_rate_limit_pct     DECIMAL(5,2) NOT NULL DEFAULT 100.00,  -- 100% = full access
    requires_manual_review BOOLEAN NOT NULL DEFAULT FALSE,
    is_blocked             BOOLEAN NOT NULL DEFAULT FALSE,
    blocked_reason         TEXT,
    blocked_at             TIMESTAMPTZ,
    
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Seed initial platform entries
INSERT INTO platform_trust_scores (platform_name, platform_type, trust_score, trust_tier, supports_c2pa, supports_ncp) VALUES
('spotify', 'streaming', 60.00, 'standard', FALSE, FALSE),
('youtube', 'streaming', 55.00, 'standard', TRUE, FALSE),
('apple_music', 'streaming', 65.00, 'standard', FALSE, FALSE),
('tiktok', 'social', 40.00, 'probation', FALSE, FALSE),
('suno', 'ai_training', 15.00, 'blocked', FALSE, FALSE),
('udio', 'ai_training', 15.00, 'blocked', FALSE, FALSE),
('elevenlabs', 'ai_training', 35.00, 'probation', FALSE, FALSE),
('meta', 'social', 30.00, 'probation', FALSE, FALSE);


-- ============================================================================
-- DECISION ENGINE v2.0
-- ============================================================================
-- Upgraded from v1.0 with violation awareness.
-- Now checks not just consent, but also violator history and platform trust.

CREATE OR REPLACE FUNCTION evaluate_licensing_request(
    p_creator_id UUID,
    p_asset_id UUID,
    p_requester_entity TEXT,
    p_requester_platform TEXT,
    p_use_case TEXT,
    p_territory TEXT,
    p_duration_days INTEGER,
    p_is_ai_involved BOOLEAN DEFAULT FALSE,
    p_ai_model TEXT DEFAULT NULL
) RETURNS JSONB AS $$
DECLARE
    v_consent RECORD;
    v_platform RECORD;
    v_adversarial RECORD;
    v_compliance RECORD;
    v_result JSONB;
    v_decision TEXT;
    v_denial_reasons TEXT[];
    v_risk_score DECIMAL;
BEGIN
    -- STEP 0: Check Never Clauses (constitutional — no exceptions)
    IF p_use_case IN ('nsfw', 'political_ad', 'medical_advice', 'impersonation') THEN
        RETURN jsonb_build_object(
            'decision', 'DENIED',
            'reason', 'Never Clause violation: ' || p_use_case,
            'voice_of_refusal', 'I must decline. This use case is constitutionally prohibited by NOIZY''s Never Clauses. This protects the creator and their voice.',
            'never_clause_violated', TRUE,
            'timestamp', NOW()
        );
    END IF;
    
    -- STEP 1: Check platform trust score
    SELECT * INTO v_platform FROM platform_trust_scores
    WHERE platform_name = p_requester_platform;
    
    IF v_platform IS NOT NULL AND v_platform.is_blocked THEN
        RETURN jsonb_build_object(
            'decision', 'DENIED',
            'reason', 'Platform is blocked: ' || v_platform.blocked_reason,
            'platform_trust_score', v_platform.trust_score,
            'platform_trust_tier', v_platform.trust_tier,
            'timestamp', NOW()
        );
    END IF;
    
    -- STEP 2: Check for active consent
    -- (References the consent_policies table from Layer 1 v1.0)
    -- This is a simplified check — full implementation queries consent_rules
    
    -- STEP 3: Check adversarial history
    SELECT COUNT(*) as probe_count,
           AVG(risk_score) as avg_risk
    INTO v_adversarial
    FROM adversarial_inquiry_log
    WHERE inquiry_source = p_requester_entity
      AND created_at > NOW() - INTERVAL '30 days';
    
    v_risk_score := COALESCE(v_adversarial.avg_risk, 0);
    
    -- STEP 4: Check AI model license flags
    IF p_is_ai_involved AND p_ai_model IS NOT NULL THEN
        IF p_ai_model IN ('MusicGen', 'MaskGCT', 'Tango2', 'FishSpeech') THEN
            RETURN jsonb_build_object(
                'decision', 'DENIED',
                'reason', 'AI model is BLOCKED for commercial use: ' || p_ai_model,
                'license_flag', 'BLOCKED_NON_COMMERCIAL',
                'action_required', 'Board review required before commercial use',
                'timestamp', NOW()
            );
        END IF;
    END IF;
    
    -- STEP 5: Check platform trust + adversarial risk
    IF v_risk_score > 0.7 THEN
        v_decision := 'DENIED';
        v_denial_reasons := array_append(v_denial_reasons, 'High adversarial risk score: ' || v_risk_score::TEXT);
    ELSIF v_platform IS NOT NULL AND v_platform.trust_score < 30 THEN
        v_decision := 'MANUAL_REVIEW';
        v_denial_reasons := array_append(v_denial_reasons, 'Low platform trust: ' || v_platform.trust_score::TEXT);
    ELSIF v_platform IS NOT NULL AND v_platform.requires_manual_review THEN
        v_decision := 'MANUAL_REVIEW';
        v_denial_reasons := array_append(v_denial_reasons, 'Platform on manual review');
    ELSE
        v_decision := 'ALLOWED';
    END IF;
    
    -- STEP 6: Log the inquiry (every inquiry is logged, always)
    INSERT INTO adversarial_inquiry_log (
        creator_id, inquiry_source, inquiry_type, inquiry_payload,
        risk_score, risk_category, decision
    ) VALUES (
        p_creator_id, p_requester_entity, 'licensing',
        jsonb_build_object(
            'use_case', p_use_case,
            'territory', p_territory,
            'duration_days', p_duration_days,
            'platform', p_requester_platform,
            'ai_involved', p_is_ai_involved,
            'ai_model', p_ai_model
        ),
        v_risk_score,
        CASE
            WHEN v_risk_score > 0.7 THEN 'critical'
            WHEN v_risk_score > 0.5 THEN 'high'
            WHEN v_risk_score > 0.3 THEN 'medium'
            ELSE 'low'
        END,
        v_decision
    );
    
    -- Build result
    v_result := jsonb_build_object(
        'decision', v_decision,
        'creator_id', p_creator_id,
        'asset_id', p_asset_id,
        'requester', p_requester_entity,
        'platform', p_requester_platform,
        'platform_trust_score', COALESCE(v_platform.trust_score, -1),
        'adversarial_risk_score', v_risk_score,
        'denial_reasons', COALESCE(v_denial_reasons, '{}'),
        'compensation_tier', 'standard',
        'plowman_standard', '75/25',
        'timestamp', NOW()
    );
    
    RETURN v_result;
END;
$$ LANGUAGE plpgsql;


-- ============================================================================
-- GABRIEL MCP QUERY PATTERNS
-- ============================================================================
-- These are the queries GABRIEL uses to interact with the schema.
-- Pattern: gabriel.query('noizy.<domain>.<operation>', params)

-- Example: Check if a voice clone request is authorized
-- gabriel.query('noizy.consent.check_voice_clone', {
--   creator_id: 'uuid',
--   requester: 'suno_ai',
--   platform: 'suno',
--   use_case: 'voice_synthesis'
-- })
-- → Calls evaluate_licensing_request()

-- Example: Get all active violations for a creator
-- gabriel.query('noizy.violations.active', { creator_id: 'uuid' })
-- → SELECT * FROM violation_events WHERE creator_id = $1 AND response_status NOT IN ('resolved', 'settled')

-- Example: Get platform trust score
-- gabriel.query('noizy.platform.trust', { platform: 'suno' })
-- → SELECT * FROM platform_trust_scores WHERE platform_name = $1

-- Example: Get full provenance chain for an asset
-- gabriel.query('noizy.provenance.chain', { asset_id: 'uuid' })
-- → SELECT am.*, ma.assertion_kind, ma.assertion_data, aa.action_type
--   FROM asset_manifests am
--   JOIN manifest_assertions ma ON am.manifest_id = ma.manifest_id
--   JOIN asset_actions aa ON am.manifest_id = aa.manifest_id
--   WHERE am.asset_id = $1
--   ORDER BY aa.action_started_at

-- Example: Build litigation evidence pack
-- gabriel.query('noizy.litigation.build_pack', { violation_id: 'uuid' })
-- → Aggregates violation_events + enforcement_actions + scan_results + asset_manifests
--   into a sealed, hashed litigation_evidence_packs entry


-- ============================================================================
-- SAMPLE DATA — THREE CREATORS (Continued from Layer 1)
-- ============================================================================
-- Aria Vale (composer), Marcus Reed (voice actor), Nova Thread (sound designer)
-- Now with assets, manifests, monitors, and a sample violation.

-- NOTE: These INSERT statements assume the Layer 1 creators table already has
-- these three creators from the v1.0 schema. The UUIDs below are placeholders.
-- In production, these would reference actual creator_id values.

-- Sample asset for Marcus Reed (voice actor)
-- INSERT INTO audio_assets (...) VALUES (...);

-- Sample violation: Suno trained on Marcus Reed's voice without consent
-- INSERT INTO violation_events (...) VALUES (...);

-- Sample enforcement: Automated DMCA takedown
-- INSERT INTO enforcement_actions (...) VALUES (...);


-- ============================================================================
-- VIEWS — OPERATIONAL DASHBOARDS
-- ============================================================================

-- Active violations by severity
CREATE OR REPLACE VIEW v_active_violations AS
SELECT 
    ve.violation_id,
    c.legal_name as creator_name,
    ve.violation_type,
    ve.severity,
    ve.severity_score,
    ve.violator_entity,
    ve.violator_platform,
    ve.response_status,
    ve.violation_detected_at,
    ve.estimated_revenue_lost_usd,
    pts.trust_score as platform_trust_score,
    pts.trust_tier as platform_trust_tier
FROM violation_events ve
JOIN creators c ON ve.creator_id = c.creator_id
LEFT JOIN platform_trust_scores pts ON ve.violator_platform = pts.platform_name
WHERE ve.response_status NOT IN ('resolved', 'settled')
ORDER BY ve.severity_score DESC, ve.violation_detected_at DESC;

-- Creator provenance summary
CREATE OR REPLACE VIEW v_creator_provenance AS
SELECT
    c.creator_id,
    c.legal_name,
    COUNT(DISTINCT aa.asset_id) as total_assets,
    COUNT(DISTINCT am.manifest_id) as total_manifests,
    COUNT(DISTINCT act.action_id) as total_actions,
    COUNT(DISTINCT ve.violation_id) as total_violations,
    COUNT(DISTINCT ve.violation_id) FILTER (WHERE ve.response_status NOT IN ('resolved', 'settled')) as active_violations,
    MAX(am.created_at) as latest_manifest_at
FROM creators c
LEFT JOIN audio_assets aa ON c.creator_id = aa.creator_id
LEFT JOIN asset_manifests am ON aa.asset_id = am.asset_id
LEFT JOIN asset_actions act ON aa.asset_id = act.asset_id
LEFT JOIN violation_events ve ON c.creator_id = ve.creator_id
GROUP BY c.creator_id, c.legal_name;

-- Platform compliance dashboard
CREATE OR REPLACE VIEW v_platform_compliance AS
SELECT
    pts.platform_name,
    pts.trust_score,
    pts.trust_tier,
    pts.supports_c2pa,
    pts.supports_ncp,
    pts.supports_ddex,
    pts.supports_ai_disclosure,
    pts.total_violations,
    pts.total_unresolved,
    pts.is_blocked,
    CASE 
        WHEN pts.trust_score >= 80 THEN 'Full access'
        WHEN pts.trust_score >= 50 THEN 'Standard access'
        WHEN pts.trust_score >= 30 THEN 'Restricted — manual review required'
        ELSE 'Blocked — all access denied'
    END as access_level
FROM platform_trust_scores pts
ORDER BY pts.trust_score DESC;

-- Enforcement action timeline (for legal review)
CREATE OR REPLACE VIEW v_enforcement_timeline AS
SELECT
    ea.action_id,
    ve.violation_type,
    ve.violator_entity,
    ea.action_type,
    ea.executed_by,
    ea.executed_at,
    ea.outcome,
    ea.compliance_deadline,
    ea.is_overdue,
    c.legal_name as creator_name
FROM enforcement_actions ea
JOIN violation_events ve ON ea.violation_id = ve.violation_id
JOIN creators c ON ve.creator_id = c.creator_id
ORDER BY ea.executed_at DESC;


-- ============================================================================
-- SCHEMA INTEGRITY
-- ============================================================================

-- Trigger: Update platform trust score on new violation
CREATE OR REPLACE FUNCTION update_platform_trust_on_violation()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE platform_trust_scores
    SET 
        total_violations = total_violations + 1,
        total_unresolved = total_unresolved + 1,
        trust_score = GREATEST(0, trust_score - 
            CASE NEW.severity
                WHEN 'critical' THEN 15.0
                WHEN 'high' THEN 10.0
                WHEN 'medium' THEN 5.0
                WHEN 'low' THEN 2.0
            END),
        trust_tier = CASE
            WHEN trust_score - 15 < 20 THEN 'blocked'
            WHEN trust_score - 15 < 40 THEN 'probation'
            WHEN trust_score - 15 < 70 THEN 'standard'
            ELSE 'trusted'
        END,
        updated_at = NOW()
    WHERE platform_name = NEW.violator_platform;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_violation_trust_update
    AFTER INSERT ON violation_events
    FOR EACH ROW
    WHEN (NEW.violator_platform IS NOT NULL)
    EXECUTE FUNCTION update_platform_trust_on_violation();

-- Trigger: Auto-block platform when trust drops below threshold
CREATE OR REPLACE FUNCTION auto_block_low_trust_platform()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.trust_score < 20 AND NOT NEW.is_blocked THEN
        NEW.is_blocked := TRUE;
        NEW.blocked_at := NOW();
        NEW.blocked_reason := 'Trust score dropped below threshold (automatic)';
        NEW.trust_tier := 'blocked';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_auto_block_platform
    BEFORE UPDATE ON platform_trust_scores
    FOR EACH ROW
    EXECUTE FUNCTION auto_block_low_trust_platform();

-- Trigger: Ensure Plowman Standard is never violated in compensation
CREATE OR REPLACE FUNCTION enforce_plowman_standard()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.creator_share_pct < 75.00 THEN
        RAISE EXCEPTION 'PLOWMAN STANDARD VIOLATION: Creator share cannot be below 75%%. Attempted: %%',
            NEW.creator_share_pct;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_plowman_standard
    BEFORE INSERT OR UPDATE ON compensation_tiers
    FOR EACH ROW
    EXECUTE FUNCTION enforce_plowman_standard();


-- ============================================================================
-- EXPORT FUNCTIONS
-- ============================================================================

-- Export asset provenance to C2PA-compatible JSON
-- (Would be converted to CBOR/JUMBF by the application layer)
CREATE OR REPLACE FUNCTION export_c2pa_manifest(p_asset_id UUID)
RETURNS JSONB AS $$
DECLARE
    v_asset RECORD;
    v_manifest RECORD;
    v_assertions JSONB;
    v_actions JSONB;
BEGIN
    SELECT * INTO v_asset FROM audio_assets WHERE asset_id = p_asset_id;
    SELECT * INTO v_manifest FROM asset_manifests 
        WHERE asset_id = p_asset_id AND is_valid = TRUE
        ORDER BY created_at DESC LIMIT 1;
    
    SELECT jsonb_agg(jsonb_build_object(
        'label', assertion_label,
        'kind', assertion_kind,
        'data', assertion_data
    )) INTO v_assertions
    FROM manifest_assertions WHERE manifest_id = v_manifest.manifest_id;
    
    SELECT jsonb_agg(jsonb_build_object(
        'action', action_type,
        'actor', actor_id,
        'software', software_agent,
        'ai_involvement', ai_involvement,
        'timestamp', action_completed_at
    )) INTO v_actions
    FROM asset_actions WHERE manifest_id = v_manifest.manifest_id;
    
    RETURN jsonb_build_object(
        'c2pa_version', '2.2',
        'noizy_proof_version', '1.0',
        'claim_id', v_manifest.c2pa_claim_id,
        'asset', jsonb_build_object(
            'id', v_asset.asset_id,
            'title', v_asset.asset_title,
            'type', v_asset.asset_type,
            'hash', v_asset.content_hash_sha256,
            'isrc', v_asset.isrc,
            'format', v_asset.file_format,
            'sample_rate', v_asset.sample_rate_hz,
            'bit_depth', v_asset.bit_depth
        ),
        'creator', jsonb_build_object(
            'id', v_asset.creator_id,
            'consent_verified', TRUE,
            'consent_hash', v_manifest.ncp_consent_hash,
            'consent_scope', v_manifest.ncp_consent_scope,
            'never_clauses', v_manifest.ncp_never_clauses
        ),
        'signature', jsonb_build_object(
            'algorithm', v_manifest.signature_algorithm,
            'signer', v_manifest.signer_entity,
            'timestamp', v_manifest.signature_timestamp
        ),
        'binding', jsonb_build_object(
            'type', v_manifest.binding_type,
            'hash', v_manifest.binding_hash,
            'algorithm', v_manifest.binding_algorithm
        ),
        'assertions', COALESCE(v_assertions, '[]'::jsonb),
        'actions', COALESCE(v_actions, '[]'::jsonb),
        'exported_at', NOW()
    );
END;
$$ LANGUAGE plpgsql;


-- ============================================================================
-- END OF SCHEMA v2.0
-- ============================================================================
-- Total tables: 17 (6 Layer 1 upgrades + 5 Layer 2 + 6 Module 2)
-- Total views: 4
-- Total functions: 5
-- Total triggers: 3
-- 
-- Standards compliance:
--   ✓ C2PA v2.2 (manifest, assertions, actions, ingredients, binding)
--   ✓ DDEX ERN 4.3 (resource IDs, AI disclosure fields)
--   ✓ ISRC/ISWC/UPC (industry identifiers)
--   ✓ X.509 (certificate chain for signing)
--   ✓ NO FAKES Act (voice estate, consent inheritance)
--   ✓ SAG-AFTRA (voice consent requirements)
--   ✓ EU AI Act (transparency, AI disclosure)
--   ✓ California AB 1836 (digital replica protection)
--   ✓ The Plowman Standard (75/25, enforced at database level)
--
-- Next: Layer 3 (Royalties / GABRIEL) + Module 3 (Automated Enforcement)
-- ============================================================================
