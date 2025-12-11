# Audio Processing Scripts

Audio repair, restoration, and dataset curation pipelines for professional audio workflows.

## Overview

This directory contains scripts for processing, repairing, and managing audio files at scale. These tools are designed for professional audio engineers and music producers working with large audio datasets.

## Key Scripts

### `rr.sh` - Main Audio Repair Pipeline

The primary audio repair and restoration script.

**Features:**
- Automated audio repair workflows
- Batch processing capabilities
- Quality analysis and reporting
- Dataset curation tools

**Usage:**
```bash
# Setup the pipeline
./rr.sh setup

# Process a single file
./rr.sh process input.wav

# Process a directory
./rr.sh batch /path/to/audio/files

# Get help
./rr.sh --help
```

## Supported Audio Formats

- WAV (PCM, float)
- AIFF
- FLAC
- MP3 (via ffmpeg)
- OGG Vorbis

## Dependencies

### Required
- **ffmpeg** - Audio conversion and processing
- **sox** - Sound processing utilities
- **Bash 4.0+** - Shell environment

### Optional
- **lame** - MP3 encoding
- **flac** - FLAC compression
- **wavpack** - WavPack compression

### Installation (macOS)
```bash
brew install ffmpeg sox lame flac wavpack
```

## Common Workflows

### Audio Repair
```bash
# Repair corrupted audio file
./rr.sh repair damaged-audio.wav

# Analyze audio quality
./rr.sh analyze audio-file.wav

# Batch repair directory
./rr.sh batch-repair /path/to/audio/
```

### Dataset Curation
```bash
# Organize audio files
./rr.sh organize /path/to/raw/audio

# Validate audio integrity
./rr.sh validate /path/to/dataset

# Generate metadata
./rr.sh metadata /path/to/audio
```

### Format Conversion
```bash
# Convert to WAV
./rr.sh convert input.mp3 output.wav

# Batch convert
./rr.sh batch-convert /path/to/audio wav
```

## Configuration

### Environment Variables
```bash
# Set output directory
export AUDIO_OUTPUT_DIR="/path/to/output"

# Set quality threshold
export AUDIO_QUALITY_THRESHOLD=95

# Set processing threads
export AUDIO_THREADS=4
```

### Config File
Create `.audio-config` in your home directory:
```bash
OUTPUT_DIR=/path/to/output
QUALITY_THRESHOLD=95
THREADS=4
SAMPLE_RATE=48000
BIT_DEPTH=24
```

## Output Structure

Processed files are organized as:
```
output/
├── repaired/           # Repaired audio files
├── logs/               # Processing logs
├── reports/            # Quality reports
├── metadata/           # Generated metadata
└── backups/            # Original file backups
```

## Audio Processing Pipeline

1. **Input Validation** - Verify file integrity
2. **Format Detection** - Identify audio format
3. **Quality Analysis** - Assess audio quality
4. **Repair Operations** - Apply necessary repairs
5. **Format Conversion** - Convert to target format
6. **Quality Verification** - Verify output quality
7. **Metadata Generation** - Create metadata
8. **Archiving** - Store original files

## Quality Checks

The pipeline performs these quality checks:
- **Clipping detection** - Identify clipped audio
- **DC offset** - Detect DC bias
- **Peak levels** - Check for proper headroom
- **RMS levels** - Verify average loudness
- **Frequency analysis** - Check frequency response
- **Phase issues** - Detect phase problems

## Error Handling

### Common Errors

**File Not Found**
```bash
Error: Input file not found: input.wav
```
Solution: Verify file path and permissions

**Unsupported Format**
```bash
Error: Unsupported audio format
```
Solution: Convert to supported format first

**Insufficient Memory**
```bash
Error: Cannot allocate memory
```
Solution: Process smaller batches or increase RAM

## Performance Optimization

### Batch Processing
```bash
# Use parallel processing
./rr.sh batch --parallel 4 /path/to/audio

# Set priority
nice -n 10 ./rr.sh batch /path/to/audio
```

### Large Files
```bash
# Process in chunks
./rr.sh process --chunk-size 1024M large-file.wav
```

## Best Practices

1. **Backup originals** - Always keep original files
2. **Test first** - Test on sample files before batch processing
3. **Monitor progress** - Watch logs during processing
4. **Verify output** - Check processed files manually
5. **Document settings** - Save processing parameters
6. **Use staging** - Process in staging area first

## Troubleshooting

### Debug Mode
```bash
# Enable verbose logging
./rr.sh --debug process input.wav

# Check logs
tail -f logs/audio-processing.log
```

### Common Issues

**Script won't run:**
```bash
chmod +x rr.sh
```

**ffmpeg not found:**
```bash
brew install ffmpeg
```

**Out of disk space:**
```bash
# Clean up temporary files
./rr.sh cleanup
```

## Integration

### With Other Scripts
```bash
# Chain with mail manager
./rr.sh process audio.wav && ../mail_manager_pro/backup.sh
```

### As Library
```bash
# Source in other scripts
source audio-processing/rr.sh
audio_repair "file.wav"
```

## Related Documentation

- [Scripts Overview](../README.md)
- [Main README](../../README.md)
- [Audio Engineering Docs](../../docs/music-production/)

## Support

For audio processing questions:
- Check processing logs
- Review error messages
- Test with sample files
- Open an issue on GitHub

---

**NOIZYLAB Audio Processing** | Professional Audio Repair & Restoration
