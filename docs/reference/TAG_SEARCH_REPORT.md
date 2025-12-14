# ID3 Tag Search Report

## Summary

**Total Files Scanned:** 1,594 WAV files  
**Files with Tags:** 1,581 files (99.2%)  
**Files with ID3 Tags:** 1,581 files (99.2%)  
**Unique Tag Types Found:** 18

## Tag Frequency Analysis

| Tag Type | Files | Percentage | Description |
|----------|-------|------------|-------------|
| **TIT2** | 1,494 | 93.7% | Title/Description |
| **TXXX:Tags** | 1,164 | 73.0% | Custom Tags |
| **TXXX:Keywords** | 1,160 | 72.8% | Keywords |
| **TCON** | 1,043 | 65.4% | Genre/Category |
| **TENC** | 407 | 25.5% | Encoder |
| **TPUB** | 257 | 16.1% | Publisher |
| **TDRC** | 203 | 12.7% | Date Recorded |
| **COMM::eng** | 154 | 9.7% | Comments (English) |
| **TPE1** | 110 | 6.9% | Artist/Performer |
| **TALB** | 109 | 6.8% | Album |
| **TRCK** | 101 | 6.3% | Track Number |
| **COMM:iTunNORM:eng** | 97 | 6.1% | iTunes Normalization |
| **COMM:iTunes_CDDB_IDs:eng** | 97 | 6.1% | iTunes CDDB IDs |
| **TCOM** | 81 | 5.1% | Composer |
| **APIC:** | 49 | 3.1% | Album Art/Image |
| **TXXX:Location** | 44 | 2.8% | Location |
| **TPE2** | 7 | 0.4% | Album Artist |
| **TPOS** | 4 | 0.3% | Disc Number |

## Tag Type Descriptions

### Standard ID3 Tags

- **TIT2**: Title/Description of the audio file
- **TCON**: Content type/Genre (e.g., Aircraft, Ambience, Crowd, Footsteps)
- **TPE1**: Artist/Performer name
- **TPE2**: Album Artist
- **TALB**: Album name
- **TCOM**: Composer
- **TDRC**: Date recorded
- **TPUB**: Publisher
- **TRCK**: Track number
- **TPOS**: Disc/Part of set position
- **TENC**: Encoder used

### Custom Tags (TXXX)

- **TXXX:Tags**: Custom tags (categories, characteristics)
- **TXXX:Keywords**: Extracted keywords from filename
- **TXXX:Location**: Geographic location (Paris, Venice, Germany, etc.)

### Comments (COMM)

- **COMM::eng**: General comments in English
- **COMM:iTunNORM:eng**: iTunes normalization data
- **COMM:iTunes_CDDB_IDs:eng**: iTunes CDDB identification

### Images

- **APIC**: Album art/embedded images

## Categories Found (TCON)

- Aircraft
- Ambience
- City
- Crowd
- Footsteps
- Industry
- Music
- Nature
- Party
- Restaurant
- Sports
- Traffic
- Water
- Uncategorized

## Locations Found (TXXX:Location)

- Australia
- Germany
- Mexico
- Paris
- Venice
- Vienna

## Publishers/Artists Found (TPE1)

- Digiffects
- Hanna Barbera 5
- Hollywood Edge
- Hollywood Edge - Premiere Edition
- Sound Ideas
- Various Artists

## Albums Found (TALB)

- 3001 Ambience - City Atmospheres
- 3006 Ambience - Outdoor Crowds
- 3007 Ambience - Outdoor Crowds
- 3008 Ambience - Indoor Crowds
- 3009 - Ambience Indoor Crowds
- 3010 Ambience Restaurants, Bars, Offices
- 3011 Ambience - European Ambiences
- 3012 Ambience - Room Tones
- H03 Sports
- HB05

## Files Generated

1. **all_id3_tags.json**: Complete tag data for all files
2. **tag_statistics.json**: Statistical summary of all tags
3. **TAG_SEARCH_REPORT.md**: This report

## Notes

- Most files (93.7%) have title/description tags (TIT2)
- 73% of files have custom tags and keywords embedded
- 65.4% of files are categorized by genre/content type
- Files are well-organized with comprehensive metadata
- Location tags are present in 44 files (2.8%)
- Some files contain album art (APIC) - 49 files (3.1%)

## Search Capabilities

All tag data is available in JSON format for:
- Searching by category
- Searching by location
- Searching by keywords
- Searching by artist/publisher
- Searching by album
- Filtering by tag presence

