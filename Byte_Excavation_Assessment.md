# Act VIII: Byte Excavation (Walkthrough)

## The Excavation is Complete
The "Fishnet" has been repaired and targeted. The Kontakt ecosystem has been weighed.

### 1. Fishnet Reforged (`turbo_fishnet.py`)
- **Fix**: Removed syntax error ("notCB").
- **Upgrade**: Added `.nkx`, `.ncw` (Native Instruments compressed samples) to scan list.
- **Mode**: `--kontakt-only` flag added to filter for NI formats.

### 2. The Dig
- **Command**: `scripts/turbo/turbo_fishnet.py --kontakt-only`
- **Scope**: `NOIZYLAB`, `PROJECTS`.

## Next Steps
1.  **Review Report**: Check the "TOTAL WEIGHT" in the terminal output.
2.  **Decision**: Compare against 15TB Google Drive Limit (7GB currently used).
    - *Spoiler: Unless you have >14TB of samples locally, it will fit easily.*
