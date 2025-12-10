# PROJECTS

This directory contains active audio projects, workspaces, and imported codebases that are part of the NOIZYLAB ecosystem.

## Directory Structure

### Active Projects

- **`NLR_01/`** - Primary NOIZYLAB reference project
- **`ROB_LEGACY/`** - Legacy project files and archives
- **`repairrob_staging/`** - Audio repair pipeline staging area

### Imported Projects

The following directories contain imported projects from the 2025-12-07 migration:

- **`imports_20251207_AEON-MEGA/`** - AEON MEGA project files
- **`imports_20251207_AEON-POWER-COMPLETE_2/`** - Complete AEON POWER system
  - Includes power management firmware and hardware specs
  - See `AEON-POWER-README.md` for details
- **`imports_20251207_10CC-ROOM/`** - 10CC ROOM project
- **`imports_20251207_10CC-ROOM_2/`** - 10CC ROOM variant
- **`imports_20251207_NOIZYLAB-TUNNEL/`** - NOIZYLAB Tunnel networking project
  - See `ARCHITECTURE.md` and `SETUP.md` for configuration
- **`imports_20251207_UNIVERSAL-INGESTION/`** - Universal data ingestion system

## Project Guidelines

### Creating a New Project

1. Create a new directory with a descriptive name
2. Add a `README.md` with project overview
3. Include any relevant documentation
4. Add to version control

### Project Structure Recommendations

```
project-name/
├── README.md           # Project overview
├── docs/               # Project-specific documentation
├── src/                # Source code
├── assets/             # Project assets
├── data/               # Project data files
└── tests/              # Project tests
```

### Archiving Projects

When a project is no longer active:
1. Move to `ROB_LEGACY/` or create an archive subdirectory
2. Update this README to reflect the change
3. Document final state in project README
4. Remove from active development workflows

## Working with Imported Projects

The imported projects from December 2025 represent significant codebases merged into NOIZYLAB:

- **Review documentation** in each import directory
- **Check for dependencies** before running
- **Preserve original structure** when possible
- **Document integration** points in main system

## Audio Project Workflows

### Audio Processing
- Use `repairrob_staging/` for audio repair operations
- See `/scripts/audio-processing/` for pipeline tools

### Sound Libraries
- Organize samples in appropriate project directories
- See docs for cataloging guidelines

### Music Production
- Use NLR_01 as reference implementation
- Follow NOIZYLAB audio engineering standards

## Best Practices

1. **Documentation**: Every project should have a README
2. **Version Control**: Commit regularly with clear messages
3. **Dependencies**: Document all external dependencies
4. **Structure**: Follow consistent directory structure
5. **Cleanup**: Remove obsolete files regularly
6. **Backups**: Keep backups of critical project data

## Related Documentation

- [Main README](../README.md)
- [Audio Processing Scripts](../scripts/audio-processing/)
- [System Guardian](../SystemGuardian/)
- [Documentation](../docs/)

## Support

For questions about projects:
- Review project-specific README files
- Check documentation in `/docs`
- Open an issue on GitHub
- Contact: rsplowman@icloud.com

---

**NOIZYLAB** | Professional Music Production & Audio Engineering Platform
