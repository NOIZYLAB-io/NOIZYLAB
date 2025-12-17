-- NOIZYVOX GUILD REGISTRY SCHEMA

DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS royalties;

CREATE TABLE IF NOT EXISTS artists (
  id TEXT PRIMARY KEY,
  name TEXT,
  wallet TEXT,
  status TEXT,
  joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  agreement_version TEXT
);

CREATE TABLE IF NOT EXISTS royalties (
  id TEXT PRIMARY KEY,
  artist_id TEXT,
  total_amount_usd REAL,
  artist_share REAL,
  platform_share REAL,
  meta TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  transaction_id TEXT
);

-- Seed Data (The Guild Founders)
INSERT INTO artists (id, name, wallet, status, agreement_version) VALUES 
('titan', 'Thunder Titan', '0x123...TITAN', 'active', 'v1.0'),
('solar', 'Solar Sentinel', '0x456...SOLAR', 'active', 'v1.0'),
('void', 'Void Ranger', '0x789...VOID', 'active', 'v1.0'),
('architect', 'Mythic Architect', '0xABC...ARCH', 'active', 'v1.0'),
('director', 'The Director', '0xDEF...DIR', 'active', 'v1.0');
