#!/usr/bin/env python3
"""
NOIZYLAB FORENSIC VISION CAPTURE
================================
High-fidelity image capture and comparison for repair documentation.
Integrates with microscope cameras, thermal imaging, and the Gemini Vision pipeline.

The Eye sees the 3mm gap. The Manifest proves the miracle.
"""

import os
import cv2
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
from dataclasses import dataclass, field
import hashlib
import json
import base64
import asyncio
import aiohttp

# Optional GPU acceleration
try:
    import torch
    TORCH_AVAILABLE = torch.cuda.is_available() or torch.backends.mps.is_available()
except ImportError:
    TORCH_AVAILABLE = False


@dataclass
class CaptureConfig:
    """Configuration for forensic capture system."""
    # Camera settings
    camera_index: int = 0  # USB microscope camera
    resolution: Tuple[int, int] = (3840, 2160)  # 4K capture

    # Storage
    vision_dir: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB" / "GABRIEL" / "sovereign" / "vision")

    # Image processing
    denoise_strength: int = 10
    sharpen_kernel: int = 3

    # Comparison thresholds
    similarity_threshold: float = 0.85
    drift_threshold: float = 0.15

    # API endpoints
    gemini_endpoint: str = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    r2_upload_endpoint: str = "https://api.noizylab.ca/upload"


@dataclass
class ForensicFrame:
    """A captured forensic frame with metadata."""
    image_path: str
    timestamp: datetime
    frame_type: str  # 'pre', 'post', 'during'
    component_id: str
    magnification: str = "40x"

    # Analysis results
    focus_score: float = 0.0
    brightness: float = 0.0
    contrast: float = 0.0

    # Gemini analysis
    ai_description: str = ""
    detected_issues: List[str] = field(default_factory=list)

    # Verification
    image_hash: str = ""


@dataclass
class ComparisonResult:
    """Result of comparing pre/post repair images."""
    pre_frame: ForensicFrame
    post_frame: ForensicFrame

    # Metrics
    structural_similarity: float = 0.0
    mean_squared_error: float = 0.0
    histogram_correlation: float = 0.0

    # AI analysis
    correction_delta: str = ""
    repair_verified: bool = False
    confidence: float = 0.0

    # Visual diff
    diff_image_path: str = ""
    highlighted_regions: List[Dict] = field(default_factory=list)


class ForensicCapture:
    """High-fidelity forensic image capture system."""

    def __init__(self, config: CaptureConfig = None):
        self.config = config or CaptureConfig()
        self.config.vision_dir.mkdir(parents=True, exist_ok=True)

        self.camera = None
        self.frames: Dict[str, List[ForensicFrame]] = {}

        # Initialize Gemini API key
        self.gemini_key = os.getenv("GEMINI_API_KEY", "")

    def initialize_camera(self) -> bool:
        """Initialize the microscope camera."""
        try:
            self.camera = cv2.VideoCapture(self.config.camera_index)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.resolution[0])
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.resolution[1])

            # Test capture
            ret, frame = self.camera.read()
            if ret:
                print(f"Camera initialized: {self.config.resolution[0]}x{self.config.resolution[1]}")
                return True
            return False
        except Exception as e:
            print(f"Camera initialization failed: {e}")
            return False

    def capture_frame(
        self,
        ticket_id: str,
        component_id: str,
        frame_type: str = "pre",
        magnification: str = "40x"
    ) -> ForensicFrame:
        """Capture a single forensic frame."""

        if self.camera is None:
            self.initialize_camera()

        # Capture image
        ret, frame = self.camera.read()
        if not ret:
            raise RuntimeError("Failed to capture frame")

        # Process image
        processed = self._process_frame(frame)

        # Generate filename
        timestamp = datetime.now()
        filename = f"{ticket_id}_{frame_type}_{component_id}_{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
        filepath = self.config.vision_dir / ticket_id
        filepath.mkdir(exist_ok=True)
        full_path = filepath / filename

        # Save image
        cv2.imwrite(str(full_path), processed, [cv2.IMWRITE_JPEG_QUALITY, 95])

        # Calculate metrics
        focus_score = self._calculate_focus_score(processed)
        brightness = np.mean(processed)
        contrast = np.std(processed)

        # Generate hash
        image_hash = self._hash_image(processed)

        forensic_frame = ForensicFrame(
            image_path=str(full_path),
            timestamp=timestamp,
            frame_type=frame_type,
            component_id=component_id,
            magnification=magnification,
            focus_score=focus_score,
            brightness=brightness,
            contrast=contrast,
            image_hash=image_hash
        )

        # Store frame
        if ticket_id not in self.frames:
            self.frames[ticket_id] = []
        self.frames[ticket_id].append(forensic_frame)

        print(f"Captured: {filename} (Focus: {focus_score:.2f})")

        return forensic_frame

    def capture_from_file(
        self,
        image_path: str,
        ticket_id: str,
        component_id: str,
        frame_type: str = "pre"
    ) -> ForensicFrame:
        """Load existing image as forensic frame."""

        frame = cv2.imread(image_path)
        if frame is None:
            raise ValueError(f"Could not load image: {image_path}")

        processed = self._process_frame(frame)

        # Copy to vision directory
        timestamp = datetime.now()
        filename = f"{ticket_id}_{frame_type}_{component_id}_{timestamp.strftime('%Y%m%d_%H%M%S')}.jpg"
        filepath = self.config.vision_dir / ticket_id
        filepath.mkdir(exist_ok=True)
        full_path = filepath / filename

        cv2.imwrite(str(full_path), processed, [cv2.IMWRITE_JPEG_QUALITY, 95])

        forensic_frame = ForensicFrame(
            image_path=str(full_path),
            timestamp=timestamp,
            frame_type=frame_type,
            component_id=component_id,
            focus_score=self._calculate_focus_score(processed),
            brightness=np.mean(processed),
            contrast=np.std(processed),
            image_hash=self._hash_image(processed)
        )

        if ticket_id not in self.frames:
            self.frames[ticket_id] = []
        self.frames[ticket_id].append(forensic_frame)

        return forensic_frame

    async def analyze_with_gemini(self, frame: ForensicFrame) -> ForensicFrame:
        """Send frame to Gemini Vision for AI analysis."""

        if not self.gemini_key:
            print("Warning: No Gemini API key configured")
            return frame

        # Read and encode image
        with open(frame.image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")

        prompt = f"""Analyze this PCB/logic board microscope image for repair diagnostics.

Component: {frame.component_id}
Magnification: {frame.magnification}
Frame Type: {frame.frame_type}

Provide:
1. Brief description of what you see
2. Any visible damage, defects, or issues
3. Solder joint quality assessment
4. Component placement accuracy

Be concise and technical. Focus on repair-relevant details."""

        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/jpeg", "data": image_data}}
                ]
            }]
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.config.gemini_endpoint}?key={self.gemini_key}",
                json=payload
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

                    frame.ai_description = text

                    # Extract issues from response
                    issues = []
                    issue_keywords = ["damage", "defect", "crack", "bridge", "cold joint", "missing", "burnt", "corrosion"]
                    for keyword in issue_keywords:
                        if keyword.lower() in text.lower():
                            issues.append(keyword)
                    frame.detected_issues = issues

        return frame

    def compare_frames(
        self,
        pre_frame: ForensicFrame,
        post_frame: ForensicFrame
    ) -> ComparisonResult:
        """Compare pre and post repair frames."""

        # Load images
        pre_img = cv2.imread(pre_frame.image_path, cv2.IMREAD_GRAYSCALE)
        post_img = cv2.imread(post_frame.image_path, cv2.IMREAD_GRAYSCALE)

        # Ensure same size
        if pre_img.shape != post_img.shape:
            post_img = cv2.resize(post_img, (pre_img.shape[1], pre_img.shape[0]))

        # Calculate SSIM
        ssim = self._calculate_ssim(pre_img, post_img)

        # Calculate MSE
        mse = np.mean((pre_img.astype(float) - post_img.astype(float)) ** 2)

        # Histogram correlation
        hist_pre = cv2.calcHist([pre_img], [0], None, [256], [0, 256])
        hist_post = cv2.calcHist([post_img], [0], None, [256], [0, 256])
        hist_corr = cv2.compareHist(hist_pre, hist_post, cv2.HISTCMP_CORREL)

        # Generate difference image
        diff = cv2.absdiff(pre_img, post_img)
        diff_enhanced = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX)

        # Find significant change regions
        _, thresh = cv2.threshold(diff_enhanced, 50, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        highlighted_regions = []
        for contour in contours:
            if cv2.contourArea(contour) > 100:  # Filter small noise
                x, y, w, h = cv2.boundingRect(contour)
                highlighted_regions.append({
                    "x": int(x), "y": int(y),
                    "width": int(w), "height": int(h),
                    "area": int(cv2.contourArea(contour))
                })

        # Save diff image
        diff_path = str(Path(pre_frame.image_path).parent / f"diff_{pre_frame.component_id}.jpg")

        # Create color visualization
        diff_color = cv2.cvtColor(diff_enhanced, cv2.COLOR_GRAY2BGR)
        diff_color[:,:,2] = np.clip(diff_color[:,:,2] * 2, 0, 255).astype(np.uint8)  # Enhance red channel
        cv2.imwrite(diff_path, diff_color)

        # Determine repair verification
        repair_verified = (
            len(pre_frame.detected_issues) > 0 and
            len(post_frame.detected_issues) < len(pre_frame.detected_issues)
        ) or ssim > self.config.similarity_threshold

        result = ComparisonResult(
            pre_frame=pre_frame,
            post_frame=post_frame,
            structural_similarity=ssim,
            mean_squared_error=mse,
            histogram_correlation=hist_corr,
            repair_verified=repair_verified,
            confidence=min(1.0, ssim + (1 - len(post_frame.detected_issues) / max(1, len(pre_frame.detected_issues))) * 0.5) / 1.5,
            diff_image_path=diff_path,
            highlighted_regions=highlighted_regions
        )

        # Generate correction delta description
        result.correction_delta = self._generate_correction_delta(result)

        return result

    async def compare_with_ai(self, comparison: ComparisonResult) -> ComparisonResult:
        """Use Gemini to analyze the repair comparison."""

        if not self.gemini_key:
            return comparison

        # Load both images
        with open(comparison.pre_frame.image_path, "rb") as f:
            pre_data = base64.b64encode(f.read()).decode("utf-8")
        with open(comparison.post_frame.image_path, "rb") as f:
            post_data = base64.b64encode(f.read()).decode("utf-8")

        prompt = f"""Compare these two PCB microscope images - before and after repair.

Component: {comparison.pre_frame.component_id}

Pre-repair analysis: {comparison.pre_frame.ai_description}

Image 1: PRE-REPAIR state
Image 2: POST-REPAIR state

Provide:
1. What specific repair was performed?
2. Describe the "correction delta" - what changed?
3. Is the repair successful? Rate confidence 0-100%.
4. Any remaining concerns?

Be technical and concise."""

        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/jpeg", "data": pre_data}},
                    {"inline_data": {"mime_type": "image/jpeg", "data": post_data}}
                ]
            }]
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.config.gemini_endpoint}?key={self.gemini_key}",
                json=payload
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

                    comparison.correction_delta = text

                    # Extract confidence from response
                    import re
                    confidence_match = re.search(r'(\d+)%', text)
                    if confidence_match:
                        comparison.confidence = int(confidence_match.group(1)) / 100.0

                    comparison.repair_verified = comparison.confidence > 0.7

        return comparison

    def _process_frame(self, frame: np.ndarray) -> np.ndarray:
        """Apply image processing pipeline."""

        # Denoise
        denoised = cv2.fastNlMeansDenoisingColored(frame, None, self.config.denoise_strength, 10, 7, 21)

        # Sharpen
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpened = cv2.filter2D(denoised, -1, kernel)

        # Auto white balance
        result = self._auto_white_balance(sharpened)

        return result

    def _auto_white_balance(self, img: np.ndarray) -> np.ndarray:
        """Apply automatic white balance."""
        result = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        avg_a = np.average(result[:, :, 1])
        avg_b = np.average(result[:, :, 2])
        result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
        result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
        return cv2.cvtColor(result, cv2.COLOR_LAB2BGR)

    def _calculate_focus_score(self, img: np.ndarray) -> float:
        """Calculate image focus score using Laplacian variance."""
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) == 3 else img
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        return laplacian.var()

    def _calculate_ssim(self, img1: np.ndarray, img2: np.ndarray) -> float:
        """Calculate Structural Similarity Index."""
        C1 = (0.01 * 255) ** 2
        C2 = (0.03 * 255) ** 2

        img1 = img1.astype(np.float64)
        img2 = img2.astype(np.float64)

        mu1 = cv2.GaussianBlur(img1, (11, 11), 1.5)
        mu2 = cv2.GaussianBlur(img2, (11, 11), 1.5)

        mu1_sq = mu1 ** 2
        mu2_sq = mu2 ** 2
        mu1_mu2 = mu1 * mu2

        sigma1_sq = cv2.GaussianBlur(img1 ** 2, (11, 11), 1.5) - mu1_sq
        sigma2_sq = cv2.GaussianBlur(img2 ** 2, (11, 11), 1.5) - mu2_sq
        sigma12 = cv2.GaussianBlur(img1 * img2, (11, 11), 1.5) - mu1_mu2

        ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) * (sigma1_sq + sigma2_sq + C2))

        return float(ssim_map.mean())

    def _hash_image(self, img: np.ndarray) -> str:
        """Generate SHA-256 hash of image data."""
        return hashlib.sha256(img.tobytes()).hexdigest()[:16].upper()

    def _generate_correction_delta(self, comparison: ComparisonResult) -> str:
        """Generate human-readable correction delta description."""

        pre_issues = comparison.pre_frame.detected_issues
        post_issues = comparison.post_frame.detected_issues

        resolved = set(pre_issues) - set(post_issues)
        remaining = set(post_issues)

        parts = []

        if resolved:
            parts.append(f"Resolved: {', '.join(resolved)}")

        if comparison.highlighted_regions:
            total_area = sum(r['area'] for r in comparison.highlighted_regions)
            parts.append(f"Modified area: {total_area}px across {len(comparison.highlighted_regions)} regions")

        parts.append(f"SSIM: {comparison.structural_similarity:.3f}")

        if remaining:
            parts.append(f"Remaining: {', '.join(remaining)}")
        else:
            parts.append("All issues resolved")

        return " | ".join(parts)

    def export_comparison_json(self, comparison: ComparisonResult) -> str:
        """Export comparison result as JSON for manifest."""

        data = {
            "pre_repair": {
                "image": comparison.pre_frame.image_path,
                "timestamp": comparison.pre_frame.timestamp.isoformat(),
                "component": comparison.pre_frame.component_id,
                "issues": comparison.pre_frame.detected_issues,
                "focus_score": comparison.pre_frame.focus_score
            },
            "post_repair": {
                "image": comparison.post_frame.image_path,
                "timestamp": comparison.post_frame.timestamp.isoformat(),
                "component": comparison.post_frame.component_id,
                "issues": comparison.post_frame.detected_issues,
                "focus_score": comparison.post_frame.focus_score
            },
            "comparison": {
                "ssim": comparison.structural_similarity,
                "mse": comparison.mean_squared_error,
                "histogram_correlation": comparison.histogram_correlation,
                "correction_delta": comparison.correction_delta,
                "verified": comparison.repair_verified,
                "confidence": comparison.confidence,
                "diff_image": comparison.diff_image_path,
                "change_regions": comparison.highlighted_regions
            }
        }

        return json.dumps(data, indent=2)

    def release(self):
        """Release camera resources."""
        if self.camera:
            self.camera.release()


# =============================================================================
# CLI INTERFACE
# =============================================================================

async def main():
    """Demo the forensic capture system."""

    print("""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                               ║
    ║              NOIZYLAB FORENSIC VISION CAPTURE                                 ║
    ║                                                                               ║
    ║              The Eye Sees. The Manifest Proves.                               ║
    ║                                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
    """)

    capture = ForensicCapture()

    # Demo with sample images (if camera not available)
    ticket_id = "DEMO-001"
    component_id = "U8900"

    print("\n[DEMO] Simulating forensic capture and comparison...")

    # Create synthetic test images
    test_dir = capture.config.vision_dir / ticket_id
    test_dir.mkdir(parents=True, exist_ok=True)

    # Generate demo pre-repair image (with simulated damage)
    pre_img = np.ones((480, 640, 3), dtype=np.uint8) * 200
    cv2.rectangle(pre_img, (200, 150), (400, 300), (50, 50, 50), -1)  # Component
    cv2.circle(pre_img, (300, 220), 30, (0, 0, 150), -1)  # Damage indicator
    cv2.putText(pre_img, "U8900 - DAMAGE", (220, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    pre_path = str(test_dir / "demo_pre.jpg")
    cv2.imwrite(pre_path, pre_img)

    # Generate demo post-repair image (damage resolved)
    post_img = np.ones((480, 640, 3), dtype=np.uint8) * 200
    cv2.rectangle(post_img, (200, 150), (400, 300), (50, 50, 50), -1)  # Component
    cv2.circle(post_img, (300, 220), 30, (50, 150, 50), -1)  # Repaired indicator
    cv2.putText(post_img, "U8900 - REPAIRED", (210, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    post_path = str(test_dir / "demo_post.jpg")
    cv2.imwrite(post_path, post_img)

    # Load as forensic frames
    pre_frame = capture.capture_from_file(pre_path, ticket_id, component_id, "pre")
    pre_frame.detected_issues = ["thermal damage", "solder defect"]
    print(f"Pre-repair frame: {pre_frame.image_path}")

    post_frame = capture.capture_from_file(post_path, ticket_id, component_id, "post")
    post_frame.detected_issues = []
    print(f"Post-repair frame: {post_frame.image_path}")

    # Compare frames
    comparison = capture.compare_frames(pre_frame, post_frame)

    print(f"\nComparison Results:")
    print(f"  SSIM: {comparison.structural_similarity:.4f}")
    print(f"  MSE: {comparison.mean_squared_error:.2f}")
    print(f"  Verified: {comparison.repair_verified}")
    print(f"  Confidence: {comparison.confidence:.2%}")
    print(f"  Correction Delta: {comparison.correction_delta}")
    print(f"  Diff Image: {comparison.diff_image_path}")

    # Export JSON
    json_export = capture.export_comparison_json(comparison)
    json_path = test_dir / "comparison.json"
    json_path.write_text(json_export)
    print(f"\nExported comparison JSON: {json_path}")

    print("\nGORUNFREE!")

    capture.release()


if __name__ == "__main__":
    asyncio.run(main())
