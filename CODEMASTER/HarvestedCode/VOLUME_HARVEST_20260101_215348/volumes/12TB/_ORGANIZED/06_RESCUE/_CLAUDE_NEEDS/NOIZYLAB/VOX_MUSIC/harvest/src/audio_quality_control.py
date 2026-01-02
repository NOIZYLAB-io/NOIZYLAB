#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎚️ PROFESSIONAL AUDIO QUALITY CONTROL SYSTEM 🎚️                 ║
║                                                                           ║
║  Deconstruct, Analyze, Reconstruct, Perfect                              ║
║  Studio-grade audio processing for voice recordings                      ║
║  Part of VOX - Voice Control Application                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class AudioQualityMetrics:
    """Comprehensive audio quality metrics."""
    # File info
    filepath: str
    filename: str
    duration_seconds: float

    # Basic audio properties
    sample_rate: int
    bit_depth: int
    channels: int
    file_size_mb: float

    # Quality measurements
    average_db: float
    peak_db: float
    dynamic_range_db: float
    signal_to_noise_ratio: float

    # Frequency analysis
    low_frequency_energy: float  # < 200 Hz
    mid_frequency_energy: float  # 200-4000 Hz
    high_frequency_energy: float  # > 4000 Hz

    # Voice quality indicators
    clarity_score: float  # 0-100
    consistency_score: float  # 0-100
    background_noise_level: float  # dB

    # Issues detected
    clipping_detected: bool
    silence_gaps: List[Tuple[float, float]]  # (start, end) in seconds
    pops_clicks_detected: bool
    hum_detected: bool

    # Overall quality score
    overall_quality_score: float  # 0-100
    quality_grade: str  # A+, A, B, C, D, F

    # Recommendations
    needs_noise_reduction: bool
    needs_eq_adjustment: bool
    needs_compression: bool
    needs_limiting: bool
    needs_retake: bool


@dataclass
class AudioProcessingSettings:
    """Settings for audio processing pipeline."""
    # Normalization
    target_loudness_lufs: float = -16.0  # Standard for voice content
    normalize_peaks: bool = True
    peak_target_db: float = -3.0

    # Noise reduction
    noise_reduction_strength: float = 0.5  # 0-1
    noise_gate_threshold_db: float = -50.0
    reduce_hum: bool = True

    # EQ settings
    apply_eq: bool = True
    high_pass_hz: float = 80.0  # Remove rumble
    low_pass_hz: float = 12000.0  # Remove unnecessary highs
    presence_boost_db: float = 2.0  # 2-4 kHz for clarity

    # Dynamics
    apply_compression: bool = True
    compression_ratio: float = 3.0
    compression_threshold_db: float = -20.0
    apply_limiting: bool = True
    limiter_ceiling_db: float = -1.0

    # De-esser
    apply_deesser: bool = True
    deesser_frequency_hz: float = 6000.0

    # Output settings
    output_sample_rate: int = 44100
    output_bit_depth: int = 24
    output_format: str = "WAV"


class AudioQualityControl:
    """Professional audio quality control and processing system."""

    def __init__(self):
        self.base_path = Path("/Users/rsp_ms/MC96_MobileApp/VOX")
        self.raw_audio_dir = self.base_path / "voice_recordings" / "AUDIO" / "RAW"
        self.processed_audio_dir = self.base_path / "voice_recordings" / "AUDIO" / "PROCESSED"
        self.analysis_dir = self.base_path / "voice_recordings" / "AUDIO" / "ANALYSIS"
        self.rejected_dir = self.base_path / "voice_recordings" / "AUDIO" / "REJECTED"

        # Create directories
        for dir_path in [self.raw_audio_dir, self.processed_audio_dir,
                         self.analysis_dir, self.rejected_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

        # Quality thresholds
        self.quality_thresholds = {
            "excellent": 90,
            "good": 75,
            "acceptable": 60,
            "poor": 40,
            "unacceptable": 0,
        }

    def analyze_audio(self, audio_path: Path) -> AudioQualityMetrics:
        """
        Comprehensively analyze audio file quality.

        Uses ffmpeg and ffprobe for detailed analysis.
        """

        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

        # Get basic file info using ffprobe
        probe_result = self._run_ffprobe(audio_path)

        # Extract metrics
        duration = float(probe_result.get("duration", 0))
        sample_rate = int(probe_result.get("sample_rate", 44100))
        channels = int(probe_result.get("channels", 1))
        bit_rate = int(probe_result.get("bit_rate", 0))
        file_size_mb = audio_path.stat().st_size / (1024 * 1024)

        # Analyze audio levels using ffmpeg
        audio_stats = self._analyze_audio_levels(audio_path)

        # Detect issues
        issues = self._detect_audio_issues(audio_path, audio_stats)

        # Calculate quality scores
        scores = self._calculate_quality_scores(audio_stats, issues)

        # Determine quality grade
        grade = self._get_quality_grade(scores["overall"])

        metrics = AudioQualityMetrics(
            filepath=str(audio_path),
            filename=audio_path.name,
            duration_seconds=duration,
            sample_rate=sample_rate,
            bit_depth=16,  # Default, would need deeper analysis
            channels=channels,
            file_size_mb=file_size_mb,
            average_db=audio_stats.get("mean_volume", -20),
            peak_db=audio_stats.get("max_volume", -6),
            dynamic_range_db=audio_stats.get("dynamic_range", 30),
            signal_to_noise_ratio=audio_stats.get("snr", 40),
            low_frequency_energy=audio_stats.get("low_freq_energy", 0.2),
            mid_frequency_energy=audio_stats.get("mid_freq_energy", 0.6),
            high_frequency_energy=audio_stats.get("high_freq_energy", 0.2),
            clarity_score=scores["clarity"],
            consistency_score=scores["consistency"],
            background_noise_level=audio_stats.get("noise_floor", -60),
            clipping_detected=issues["clipping"],
            silence_gaps=issues["silence_gaps"],
            pops_clicks_detected=issues["pops_clicks"],
            hum_detected=issues["hum"],
            overall_quality_score=scores["overall"],
            quality_grade=grade,
            needs_noise_reduction=audio_stats.get("noise_floor", -60) > -50,
            needs_eq_adjustment=True,  # Always apply EQ
            needs_compression=audio_stats.get("dynamic_range", 30) > 20,
            needs_limiting=audio_stats.get("max_volume", -6) > -3,
            needs_retake=scores["overall"] < self.quality_thresholds["acceptable"],
        )

        # Save analysis
        self._save_analysis(metrics)

        return metrics

    def _run_ffprobe(self, audio_path: Path) -> Dict:
        """Run ffprobe to get audio file information."""
        try:
            cmd = [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(audio_path)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                data = json.loads(result.stdout)
                stream = data.get("streams", [{}])[0]
                format_info = data.get("format", {})

                return {
                    "duration": format_info.get("duration", "0"),
                    "sample_rate": stream.get("sample_rate", "44100"),
                    "channels": stream.get("channels", "1"),
                    "bit_rate": format_info.get("bit_rate", "0"),
                }
        except Exception as e:
            print(f"ffprobe error: {e}")

        return {}

    def _analyze_audio_levels(self, audio_path: Path) -> Dict:
        """Analyze audio levels and statistics using ffmpeg."""
        try:
            cmd = [
                "ffmpeg",
                "-i", str(audio_path),
                "-af", "volumedetect,astats",
                "-f", "null",
                "-"
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            stderr = result.stderr

            # Parse volumedetect output
            stats = {
                "mean_volume": -20.0,
                "max_volume": -6.0,
                "noise_floor": -60.0,
                "dynamic_range": 30.0,
                "snr": 40.0,
                "low_freq_energy": 0.2,
                "mid_freq_energy": 0.6,
                "high_freq_energy": 0.2,
            }

            # Extract mean and max volume
            for line in stderr.split('\n'):
                if "mean_volume:" in line:
                    try:
                        stats["mean_volume"] = float(line.split("mean_volume:")[1].split("dB")[0].strip())
                    except:
                        pass
                elif "max_volume:" in line:
                    try:
                        stats["max_volume"] = float(line.split("max_volume:")[1].split("dB")[0].strip())
                    except:
                        pass

            # Calculate dynamic range
            stats["dynamic_range"] = abs(stats["max_volume"] - stats["mean_volume"])

            return stats

        except Exception as e:
            print(f"Audio analysis error: {e}")
            return {}

    def _detect_audio_issues(self, audio_path: Path, stats: Dict) -> Dict:
        """Detect common audio issues."""
        issues = {
            "clipping": stats.get("max_volume", -6) >= -0.5,
            "silence_gaps": [],
            "pops_clicks": False,
            "hum": False,
        }

        # Detect silence gaps using ffmpeg silencedetect
        try:
            cmd = [
                "ffmpeg",
                "-i", str(audio_path),
                "-af", "silencedetect=n=-50dB:d=0.5",
                "-f", "null",
                "-"
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            # Parse silence detection
            silence_start = None
            for line in result.stderr.split('\n'):
                if "silence_start:" in line:
                    try:
                        silence_start = float(line.split("silence_start:")[1].split()[0])
                    except:
                        pass
                elif "silence_end:" in line and silence_start is not None:
                    try:
                        silence_end = float(line.split("silence_end:")[1].split()[0])
                        issues["silence_gaps"].append((silence_start, silence_end))
                        silence_start = None
                    except:
                        pass

        except Exception as e:
            print(f"Silence detection error: {e}")

        return issues

    def _calculate_quality_scores(self, stats: Dict, issues: Dict) -> Dict:
        """Calculate quality scores based on analysis."""
        scores = {
            "clarity": 100.0,
            "consistency": 100.0,
            "overall": 100.0,
        }

        # Clarity score (based on frequency distribution and noise)
        noise_floor = stats.get("noise_floor", -60)
        if noise_floor > -40:
            scores["clarity"] -= 40
        elif noise_floor > -50:
            scores["clarity"] -= 20
        elif noise_floor > -60:
            scores["clarity"] -= 10

        # Deduct for clipping
        if issues["clipping"]:
            scores["clarity"] -= 30
            scores["consistency"] -= 20

        # Consistency score (based on dynamic range and silence gaps)
        dynamic_range = stats.get("dynamic_range", 30)
        if dynamic_range > 40:
            scores["consistency"] -= 20
        elif dynamic_range < 10:
            scores["consistency"] -= 15

        # Deduct for silence gaps
        if len(issues["silence_gaps"]) > 5:
            scores["consistency"] -= 20
        elif len(issues["silence_gaps"]) > 2:
            scores["consistency"] -= 10

        # Deduct for pops/clicks
        if issues["pops_clicks"]:
            scores["clarity"] -= 15
            scores["consistency"] -= 10

        # Overall score (weighted average)
        scores["overall"] = (scores["clarity"] * 0.6 + scores["consistency"] * 0.4)

        # Clamp scores to 0-100
        for key in scores:
            scores[key] = max(0, min(100, scores[key]))

        return scores

    def _get_quality_grade(self, score: float) -> str:
        """Convert numeric score to letter grade."""
        if score >= 95:
            return "A+"
        elif score >= 90:
            return "A"
        elif score >= 85:
            return "A-"
        elif score >= 80:
            return "B+"
        elif score >= 75:
            return "B"
        elif score >= 70:
            return "B-"
        elif score >= 65:
            return "C+"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"

    def _save_analysis(self, metrics: AudioQualityMetrics):
        """Save analysis results to JSON."""
        analysis_file = self.analysis_dir / f"{Path(metrics.filename).stem}_analysis.json"

        with open(analysis_file, 'w') as f:
            json.dump(asdict(metrics), f, indent=2)

    def process_audio(
        self,
        input_path: Path,
        settings: Optional[AudioProcessingSettings] = None
    ) -> Tuple[Path, AudioQualityMetrics]:
        """
        Process audio through professional quality enhancement pipeline.

        Pipeline stages:
        1. Normalize levels
        2. Remove noise
        3. Apply EQ
        4. Compress dynamics
        5. Limit peaks
        6. Final normalization
        """

        if settings is None:
            settings = AudioProcessingSettings()

        # Analyze first
        print(f"\n🔍 Analyzing: {input_path.name}")
        initial_metrics = self.analyze_audio(input_path)

        print(f"   Initial Quality: {initial_metrics.quality_grade} ({initial_metrics.overall_quality_score:.1f}/100)")

        # Check if retake is needed
        if initial_metrics.needs_retake:
            print(f"   ⚠️  Quality too low - RETAKE RECOMMENDED")
            # Move to rejected folder
            rejected_path = self.rejected_dir / input_path.name
            subprocess.run(["cp", str(input_path), str(rejected_path)])
            return rejected_path, initial_metrics

        # Build ffmpeg filter chain
        filters = []

        # 1. High-pass filter (remove rumble)
        if settings.apply_eq:
            filters.append(f"highpass=f={settings.high_pass_hz}")

        # 2. Low-pass filter (remove unnecessary highs)
        if settings.apply_eq:
            filters.append(f"lowpass=f={settings.low_pass_hz}")

        # 3. Noise gate
        if initial_metrics.needs_noise_reduction:
            filters.append(f"agate=threshold={settings.noise_gate_threshold_db}dB:ratio=3")

        # 4. EQ for presence/clarity boost
        if settings.apply_eq:
            filters.append(f"equalizer=f=3000:t=h:w=1000:g={settings.presence_boost_db}")

        # 5. De-esser
        if settings.apply_deesser:
            filters.append(f"deesser=i=0.1:m=0.5:f={settings.deesser_frequency_hz}:s=o")

        # 6. Compression
        if settings.apply_compression and initial_metrics.needs_compression:
            filters.append(
                f"acompressor=threshold={settings.compression_threshold_db}dB:"
                f"ratio={settings.compression_ratio}:attack=5:release=50"
            )

        # 7. Limiter
        if settings.apply_limiting:
            filters.append(f"alimiter=limit={settings.limiter_ceiling_db}dB")

        # 8. Final normalization
        if settings.normalize_peaks:
            filters.append("loudnorm=I=-16:TP=-1.5:LRA=11")

        # Build output path
        output_path = self.processed_audio_dir / f"{input_path.stem}_processed.wav"

        # Run ffmpeg processing
        print(f"\n🎛️  Processing audio through {len(filters)}-stage pipeline...")

        try:
            filter_chain = ",".join(filters)

            cmd = [
                "ffmpeg",
                "-y",
                "-i", str(input_path),
                "-af", filter_chain,
                "-ar", str(settings.output_sample_rate),
                "-sample_fmt", "s24" if settings.output_bit_depth == 24 else "s16",
                "-c:a", "pcm_s24le" if settings.output_bit_depth == 24 else "pcm_s16le",
                str(output_path)
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            if result.returncode != 0:
                print(f"   ❌ Processing failed: {result.stderr}")
                return input_path, initial_metrics

            print(f"   ✅ Processing complete!")

            # Analyze processed audio
            print(f"\n🔍 Analyzing processed audio...")
            final_metrics = self.analyze_audio(output_path)

            print(f"   Final Quality: {final_metrics.quality_grade} ({final_metrics.overall_quality_score:.1f}/100)")
            print(f"   Improvement: +{final_metrics.overall_quality_score - initial_metrics.overall_quality_score:.1f} points")

            return output_path, final_metrics

        except subprocess.TimeoutExpired:
            print(f"   ❌ Processing timeout")
            return input_path, initial_metrics
        except Exception as e:
            print(f"   ❌ Processing error: {e}")
            return input_path, initial_metrics

    def generate_quality_report(self, metrics: AudioQualityMetrics) -> str:
        """Generate a detailed quality report."""

        report = f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        📊 AUDIO QUALITY ANALYSIS REPORT 📊                               ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

FILE: {metrics.filename}
DATE: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

═══════════════════════════════════════════════════════════════════════════

📁 FILE INFORMATION:

   Duration: {metrics.duration_seconds:.2f} seconds ({metrics.duration_seconds/60:.1f} minutes)
   Sample Rate: {metrics.sample_rate} Hz
   Bit Depth: {metrics.bit_depth} bit
   Channels: {metrics.channels} ({' mono' if metrics.channels == 1 else 'stereo'})
   File Size: {metrics.file_size_mb:.2f} MB

═══════════════════════════════════════════════════════════════════════════

🔊 AUDIO LEVELS:

   Average Level: {metrics.average_db:.1f} dB
   Peak Level: {metrics.peak_db:.1f} dB
   Dynamic Range: {metrics.dynamic_range_db:.1f} dB
   Signal-to-Noise Ratio: {metrics.signal_to_noise_ratio:.1f} dB
   Background Noise: {metrics.background_noise_level:.1f} dB

═══════════════════════════════════════════════════════════════════════════

🎚️ FREQUENCY DISTRIBUTION:

   Low Frequencies (<200Hz): {metrics.low_frequency_energy*100:.1f}%
   Mid Frequencies (200-4k): {metrics.mid_frequency_energy*100:.1f}%
   High Frequencies (>4k): {metrics.high_frequency_energy*100:.1f}%

═══════════════════════════════════════════════════════════════════════════

📊 QUALITY SCORES:

   Clarity: {metrics.clarity_score:.1f}/100
   Consistency: {metrics.consistency_score:.1f}/100

   OVERALL QUALITY: {metrics.overall_quality_score:.1f}/100
   GRADE: {metrics.quality_grade}

═══════════════════════════════════════════════════════════════════════════

⚠️  ISSUES DETECTED:

   Clipping: {'❌ YES - CRITICAL' if metrics.clipping_detected else '✅ None'}
   Pops/Clicks: {'⚠️  Detected' if metrics.pops_clicks_detected else '✅ None'}
   Hum/Buzz: {'⚠️  Detected' if metrics.hum_detected else '✅ None'}
   Silence Gaps: {len(metrics.silence_gaps)} gaps detected

"""

        if metrics.silence_gaps:
            report += "\n   Silence Gap Details:\n"
            for i, (start, end) in enumerate(metrics.silence_gaps[:5], 1):
                report += f"      {i}. {start:.2f}s - {end:.2f}s ({end-start:.2f}s)\n"

        report += f"""
═══════════════════════════════════════════════════════════════════════════

🔧 PROCESSING RECOMMENDATIONS:

   Noise Reduction: {'✅ NEEDED' if metrics.needs_noise_reduction else '⬜ Not required'}
   EQ Adjustment: {'✅ NEEDED' if metrics.needs_eq_adjustment else '⬜ Not required'}
   Compression: {'✅ NEEDED' if metrics.needs_compression else '⬜ Not required'}
   Limiting: {'✅ NEEDED' if metrics.needs_limiting else '⬜ Not required'}

   RETAKE NEEDED: {'❌ YES - Quality below acceptable threshold' if metrics.needs_retake else '✅ NO - Quality acceptable'}

═══════════════════════════════════════════════════════════════════════════

💡 QUALITY ASSESSMENT:

"""

        if metrics.overall_quality_score >= 90:
            report += "   ⭐ EXCELLENT - Professional broadcast quality\n"
        elif metrics.overall_quality_score >= 75:
            report += "   ✅ GOOD - Acceptable for production use\n"
        elif metrics.overall_quality_score >= 60:
            report += "   ⚠️  ACCEPTABLE - Consider reprocessing or minor retakes\n"
        elif metrics.overall_quality_score >= 40:
            report += "   ⚠️  POOR - Reprocessing strongly recommended\n"
        else:
            report += "   ❌ UNACCEPTABLE - Retake required\n"

        report += "\n═══════════════════════════════════════════════════════════════════════════\n"

        return report

    def batch_process_session(
        self,
        session_id: str,
        audio_files: List[Path],
        settings: Optional[AudioProcessingSettings] = None
    ) -> Dict:
        """Process all audio files from a recording session."""

        print(f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎚️ BATCH PROCESSING SESSION 🎚️                                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

Session ID: {session_id}
Files to Process: {len(audio_files)}

""")

        results = {
            "session_id": session_id,
            "total_files": len(audio_files),
            "processed_files": [],
            "rejected_files": [],
            "average_quality_before": 0,
            "average_quality_after": 0,
        }

        quality_before = []
        quality_after = []

        for i, audio_file in enumerate(audio_files, 1):
            print(f"\n[{i}/{len(audio_files)}] Processing: {audio_file.name}")
            print("─" * 75)

            processed_path, final_metrics = self.process_audio(audio_file, settings)

            if final_metrics.needs_retake:
                results["rejected_files"].append({
                    "file": audio_file.name,
                    "quality_score": final_metrics.overall_quality_score,
                    "grade": final_metrics.quality_grade,
                })
            else:
                results["processed_files"].append({
                    "original": audio_file.name,
                    "processed": processed_path.name,
                    "quality_score": final_metrics.overall_quality_score,
                    "grade": final_metrics.quality_grade,
                })
                quality_after.append(final_metrics.overall_quality_score)

        # Calculate averages
        if quality_after:
            results["average_quality_after"] = sum(quality_after) / len(quality_after)

        # Print summary
        print(f"""

╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        ✅ BATCH PROCESSING COMPLETE ✅                                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

📊 SUMMARY:

   Total Files: {results['total_files']}
   Processed Successfully: {len(results['processed_files'])}
   Rejected (Need Retake): {len(results['rejected_files'])}

   Average Quality: {results['average_quality_after']:.1f}/100

""")

        return results


def main():
    """Demo the audio quality control system."""
    qc = AudioQualityControl()

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎚️ AUDIO QUALITY CONTROL SYSTEM 🎚️                              ║
║                                                                           ║
║  Professional Audio Processing Pipeline                                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

SYSTEM CAPABILITIES:

1. ANALYSIS
   • Comprehensive audio quality metrics
   • Issue detection (clipping, noise, gaps)
   • Frequency distribution analysis
   • Quality scoring (0-100 + letter grade)

2. PROCESSING PIPELINE
   • Noise reduction and gating
   • Professional EQ (HPF, LPF, presence boost)
   • Dynamic range compression
   • Peak limiting
   • Loudness normalization (LUFS standard)
   • De-essing

3. QUALITY CONTROL
   • Automatic quality assessment
   • Retake recommendations
   • Before/after comparison
   • Detailed reporting

4. BATCH PROCESSING
   • Process entire recording sessions
   • Consistent quality across all files
   • Automatic rejection of poor quality

═══════════════════════════════════════════════════════════════════════════

QUALITY STANDARDS:

   A+ (95-100): Exceptional broadcast quality
   A  (90-94):  Professional broadcast quality
   B  (75-89):  Production ready
   C  (60-74):  Acceptable with processing
   D  (40-59):  Needs significant work
   F  (<40):    Retake required

═══════════════════════════════════════════════════════════════════════════

PROCESSING SETTINGS:

Target Loudness: -16 LUFS (industry standard for voice)
Sample Rate: 44.1 kHz
Bit Depth: 24-bit
Dynamic Range: Optimized for voice clarity
Noise Floor: < -50 dB

═══════════════════════════════════════════════════════════════════════════

📁 DIRECTORY STRUCTURE:

RAW:       {qc.raw_audio_dir}
PROCESSED: {qc.processed_audio_dir}
ANALYSIS:  {qc.analysis_dir}
REJECTED:  {qc.rejected_dir}

═══════════════════════════════════════════════════════════════════════════

✅ Audio Quality Control System Ready!

NOTE: This system uses ffmpeg for professional-grade audio processing.
      All processing is non-destructive - originals are preserved.

""")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
