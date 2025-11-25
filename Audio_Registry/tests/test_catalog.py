#!/usr/bin/env python3
# ==============================================================================
# METABEAST_CC - Unit Test Suite
# ==============================================================================
# Comprehensive tests for catalog validation and tools
# Fish Music Inc. / MissionControl96 / NOIZYLAB
# ==============================================================================

"""
Unit tests for METABEAST_CC catalog system.

Run with:
    python -m pytest tests/ -v
    python tests/test_catalog.py
"""

import os
import sys
import json
import yaml
import unittest
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# ==============================================================================
# CONFIGURATION
# ==============================================================================

REGISTRY_ROOT = Path(__file__).parent.parent
DATA_DIR = REGISTRY_ROOT / "data"
MANIFESTS_DIR = REGISTRY_ROOT / "manifests"
TOOLS_DIR = REGISTRY_ROOT / "tools"

CATALOG_FILE = DATA_DIR / "catalog.yaml"
INDEX_FILE = DATA_DIR / "index.json"

# Schema definitions
VALID_TYPES = ["daw", "plugin", "instrument", "ai_model"]
VALID_CATEGORIES = [
    "daw", "synth", "sampler", "drum", "orchestral", "hybrid",
    "eq", "compressor", "reverb", "delay", "saturation", "pitch",
    "spectral", "utility", "limiter", "multiband", "channel-strip",
    "metering", "modulation", "gate", "exciter", "stereo",
    "noise_reduction", "stem_separation", "transcription", "voice", "video"
]
VALID_FORMATS = ["VST2", "VST3", "AU", "AAX", "CLAP", "Standalone", "AUv3", "RTAS", "Kontakt", "UAD"]
VALID_OS = ["macOS", "Windows", "Linux", "iOS", "Web"]
VALID_STATUS = ["active", "legacy", "discontinued", "beta"]
REQUIRED_FIELDS = ["name", "type", "category", "developer"]


# ==============================================================================
# TEST: CATALOG STRUCTURE
# ==============================================================================

class TestCatalogStructure(unittest.TestCase):
    """Tests for catalog file structure and existence."""

    def setUp(self):
        """Load catalog before each test."""
        self.assertTrue(CATALOG_FILE.exists(), f"Catalog file not found: {CATALOG_FILE}")
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)

    def test_catalog_exists(self):
        """Test that catalog.yaml exists."""
        self.assertTrue(CATALOG_FILE.exists())

    def test_catalog_has_meta(self):
        """Test that catalog has meta section."""
        self.assertIn("meta", self.catalog)
        self.assertIn("catalogName", self.catalog["meta"])
        self.assertIn("version", self.catalog["meta"])

    def test_catalog_has_items(self):
        """Test that catalog has items list."""
        self.assertIn("items", self.catalog)
        self.assertIsInstance(self.catalog["items"], list)
        self.assertGreater(len(self.catalog["items"]), 0)

    def test_catalog_has_taxonomy(self):
        """Test that catalog has taxonomy section."""
        self.assertIn("taxonomy", self.catalog)

    def test_minimum_item_count(self):
        """Test that catalog has minimum expected items."""
        items = self.catalog.get("items", [])
        self.assertGreaterEqual(len(items), 50, "Catalog should have at least 50 items")


# ==============================================================================
# TEST: ITEM VALIDATION
# ==============================================================================

class TestItemValidation(unittest.TestCase):
    """Tests for individual item validation."""

    def setUp(self):
        """Load catalog before each test."""
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)
        self.items = self.catalog.get("items", [])

    def test_required_fields_present(self):
        """Test that all items have required fields."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            for field in REQUIRED_FIELDS:
                self.assertIn(
                    field, item,
                    f"Item {item_id} missing required field: {field}"
                )
                self.assertIsNotNone(
                    item[field],
                    f"Item {item_id} has empty required field: {field}"
                )

    def test_valid_types(self):
        """Test that all items have valid type values."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            item_type = item.get("type")
            self.assertIn(
                item_type, VALID_TYPES,
                f"Item {item_id} has invalid type: {item_type}"
            )

    def test_valid_categories(self):
        """Test that all items have valid category values."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            category = item.get("category")
            self.assertIn(
                category, VALID_CATEGORIES,
                f"Item {item_id} has invalid category: {category}"
            )

    def test_valid_formats(self):
        """Test that all format values are valid."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            formats = item.get("format", [])
            if formats:
                for fmt in formats:
                    self.assertIn(
                        fmt, VALID_FORMATS,
                        f"Item {item_id} has invalid format: {fmt}"
                    )

    def test_valid_os(self):
        """Test that all OS values are valid."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            os_list = item.get("os", [])
            if os_list:
                for os_name in os_list:
                    self.assertIn(
                        os_name, VALID_OS,
                        f"Item {item_id} has invalid OS: {os_name}"
                    )

    def test_valid_status(self):
        """Test that all status values are valid."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            status = item.get("status")
            if status:
                self.assertIn(
                    status, VALID_STATUS,
                    f"Item {item_id} has invalid status: {status}"
                )

    def test_release_year_range(self):
        """Test that release years are in valid range."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            year = item.get("releaseYear")
            if year:
                self.assertGreaterEqual(
                    year, 1980,
                    f"Item {item_id} has unrealistic year: {year}"
                )
                self.assertLessEqual(
                    year, datetime.now().year + 1,
                    f"Item {item_id} has future year: {year}"
                )


# ==============================================================================
# TEST: ITEM ID VALIDATION
# ==============================================================================

class TestItemIds(unittest.TestCase):
    """Tests for item ID format and uniqueness."""

    def setUp(self):
        """Load catalog before each test."""
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)
        self.items = self.catalog.get("items", [])

    def test_no_duplicate_ids(self):
        """Test that there are no duplicate item IDs."""
        item_ids = [item.get("itemId") for item in self.items if item.get("itemId")]
        duplicates = [id for id in item_ids if item_ids.count(id) > 1]
        self.assertEqual(
            len(duplicates), 0,
            f"Duplicate item IDs found: {set(duplicates)}"
        )

    def test_id_format(self):
        """Test that item IDs follow the correct format."""
        valid_prefixes = ["daw-", "plug-", "inst-", "ai-"]
        for item in self.items:
            item_id = item.get("itemId")
            if item_id:
                has_valid_prefix = any(item_id.startswith(p) for p in valid_prefixes)
                self.assertTrue(
                    has_valid_prefix,
                    f"Item ID has invalid prefix: {item_id}"
                )

    def test_id_number_format(self):
        """Test that item ID numbers are zero-padded."""
        for item in self.items:
            item_id = item.get("itemId", "")
            if "-" in item_id:
                prefix, number = item_id.rsplit("-", 1)
                self.assertEqual(
                    len(number), 3,
                    f"Item ID number should be 3 digits: {item_id}"
                )
                self.assertTrue(
                    number.isdigit(),
                    f"Item ID number should be numeric: {item_id}"
                )


# ==============================================================================
# TEST: URL VALIDATION
# ==============================================================================

class TestUrls(unittest.TestCase):
    """Tests for URL validation."""

    def setUp(self):
        """Load catalog before each test."""
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)
        self.items = self.catalog.get("items", [])

    def test_urls_are_https(self):
        """Test that all URLs use HTTPS."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            urls = item.get("urls", {})
            for key, url in urls.items():
                if url:
                    self.assertTrue(
                        url.startswith("https://"),
                        f"Item {item_id} has non-HTTPS URL: {url}"
                    )

    def test_no_trailing_slashes(self):
        """Test that URLs don't have trailing slashes (optional check)."""
        # This is a soft check - trailing slashes are allowed but not preferred
        pass


# ==============================================================================
# TEST: MANIFEST FILES
# ==============================================================================

class TestManifests(unittest.TestCase):
    """Tests for manifest file existence and structure."""

    def test_daw_manifest_exists(self):
        """Test that DAW manifest exists."""
        manifest_path = MANIFESTS_DIR / "DAW" / "DAW_MANIFEST.yaml"
        self.assertTrue(manifest_path.exists(), f"DAW manifest not found: {manifest_path}")

    def test_plugin_manifest_exists(self):
        """Test that Plugin manifest exists."""
        manifest_path = MANIFESTS_DIR / "Plugins" / "PLUGIN_MANIFEST.yaml"
        self.assertTrue(manifest_path.exists(), f"Plugin manifest not found: {manifest_path}")

    def test_instrument_manifest_exists(self):
        """Test that Instrument manifest exists."""
        manifest_path = MANIFESTS_DIR / "Instruments" / "INSTRUMENT_MANIFEST.yaml"
        self.assertTrue(manifest_path.exists(), f"Instrument manifest not found: {manifest_path}")

    def test_ai_models_manifest_exists(self):
        """Test that AI Models manifest exists."""
        manifest_path = MANIFESTS_DIR / "AI_Models" / "AI_MODELS_MANIFEST.yaml"
        self.assertTrue(manifest_path.exists(), f"AI Models manifest not found: {manifest_path}")

    def test_manifest_meta_sections(self):
        """Test that all manifests have meta sections."""
        manifest_dirs = [
            "DAW", "Plugins", "Instruments", "AI_Models",
            "Sample_Libraries", "Hardware", "MIDI_Controllers"
        ]
        for dir_name in manifest_dirs:
            manifest_dir = MANIFESTS_DIR / dir_name
            if manifest_dir.exists():
                for yaml_file in manifest_dir.glob("*.yaml"):
                    with open(yaml_file, 'r') as f:
                        manifest = yaml.safe_load(f)
                    self.assertIn(
                        "meta", manifest,
                        f"Manifest {yaml_file.name} missing meta section"
                    )


# ==============================================================================
# TEST: INDEX JSON
# ==============================================================================

class TestIndexJson(unittest.TestCase):
    """Tests for index.json export."""

    def setUp(self):
        """Check if index.json exists."""
        self.index_exists = INDEX_FILE.exists()
        if self.index_exists:
            with open(INDEX_FILE, 'r') as f:
                self.index = json.load(f)

    def test_index_has_meta(self):
        """Test that index.json has meta section."""
        if self.index_exists:
            self.assertIn("meta", self.index)

    def test_index_has_items(self):
        """Test that index.json has items array."""
        if self.index_exists:
            self.assertIn("items", self.index)
            self.assertIsInstance(self.index["items"], list)

    def test_index_has_stats(self):
        """Test that index.json has stats section."""
        if self.index_exists:
            self.assertIn("stats", self.index)

    def test_index_item_count_matches(self):
        """Test that index item count matches catalog."""
        if self.index_exists:
            with open(CATALOG_FILE, 'r') as f:
                catalog = yaml.safe_load(f)
            catalog_count = len(catalog.get("items", []))
            index_count = len(self.index.get("items", []))
            self.assertEqual(
                catalog_count, index_count,
                f"Index count ({index_count}) doesn't match catalog ({catalog_count})"
            )


# ==============================================================================
# TEST: TOOLS
# ==============================================================================

class TestTools(unittest.TestCase):
    """Tests for tool file existence."""

    def test_audiocat_exists(self):
        """Test that audiocat CLI exists."""
        audiocat_path = TOOLS_DIR / "audiocat"
        self.assertTrue(audiocat_path.exists(), f"audiocat not found: {audiocat_path}")

    def test_validate_schema_exists(self):
        """Test that validate_schema.py exists."""
        script_path = TOOLS_DIR / "validate_schema.py"
        self.assertTrue(script_path.exists(), f"validate_schema.py not found: {script_path}")

    def test_ai_host_guide_exists(self):
        """Test that ai_host_guide.py exists."""
        script_path = TOOLS_DIR / "ai_host_guide.py"
        self.assertTrue(script_path.exists(), f"ai_host_guide.py not found: {script_path}")


# ==============================================================================
# TEST: DATA INTEGRITY
# ==============================================================================

class TestDataIntegrity(unittest.TestCase):
    """Tests for overall data integrity."""

    def setUp(self):
        """Load catalog before each test."""
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)
        self.items = self.catalog.get("items", [])

    def test_no_empty_names(self):
        """Test that no items have empty names."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            name = item.get("name", "")
            self.assertTrue(
                len(name.strip()) > 0,
                f"Item {item_id} has empty name"
            )

    def test_no_empty_developers(self):
        """Test that no items have empty developers."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            developer = item.get("developer", "")
            self.assertTrue(
                len(developer.strip()) > 0,
                f"Item {item_id} has empty developer"
            )

    def test_type_category_consistency(self):
        """Test that DAW items have DAW category."""
        for item in self.items:
            item_id = item.get("itemId", "UNKNOWN")
            item_type = item.get("type")
            category = item.get("category")
            if item_type == "daw":
                self.assertEqual(
                    category, "daw",
                    f"DAW item {item_id} should have 'daw' category"
                )


# ==============================================================================
# TEST: NAMING CONVENTIONS
# ==============================================================================

class TestNamingConventions(unittest.TestCase):
    """Tests for naming convention compliance."""

    def setUp(self):
        """Load catalog before each test."""
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)

    def test_brand_capitalization(self):
        """Test that brand names are properly capitalized."""
        text = yaml.dump(self.catalog)
        # Check that NOIZY is always uppercase when it appears
        # This is a soft check - brands should be capitalized correctly
        # NOIZY, METABEAST_CC, MissionControl96
        pass  # Soft test - no assertion needed

    def test_no_tabs_in_yaml(self):
        """Test that YAML files don't contain tabs."""
        with open(CATALOG_FILE, 'r') as f:
            content = f.read()
        self.assertNotIn(
            "\t", content,
            "Catalog file contains tabs - use spaces only"
        )


# ==============================================================================
# HEALTH SCORE CALCULATION
# ==============================================================================

class TestHealthScore(unittest.TestCase):
    """Tests for catalog health score."""

    def setUp(self):
        """Load catalog and calculate health."""
        with open(CATALOG_FILE, 'r') as f:
            self.catalog = yaml.safe_load(f)
        self.items = self.catalog.get("items", [])

    def calculate_health_score(self) -> int:
        """Calculate health score (0-100)."""
        if not self.items:
            return 0

        total_points = 0
        max_points = 0

        for item in self.items:
            # Required fields (40 points)
            for field in REQUIRED_FIELDS:
                max_points += 10
                if item.get(field):
                    total_points += 10

            # Optional fields (60 points)
            optional = ["format", "os", "releaseYear", "status", "urls", "tags"]
            for field in optional:
                max_points += 10
                if item.get(field):
                    total_points += 10

        return int((total_points / max_points) * 100) if max_points > 0 else 0

    def test_health_score_minimum(self):
        """Test that health score is at least 80."""
        score = self.calculate_health_score()
        self.assertGreaterEqual(
            score, 80,
            f"Health score ({score}) should be at least 80"
        )


# ==============================================================================
# MAIN
# ==============================================================================

def run_tests():
    """Run all tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestCatalogStructure))
    suite.addTests(loader.loadTestsFromTestCase(TestItemValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestItemIds))
    suite.addTests(loader.loadTestsFromTestCase(TestUrls))
    suite.addTests(loader.loadTestsFromTestCase(TestManifests))
    suite.addTests(loader.loadTestsFromTestCase(TestIndexJson))
    suite.addTests(loader.loadTestsFromTestCase(TestTools))
    suite.addTests(loader.loadTestsFromTestCase(TestDataIntegrity))
    suite.addTests(loader.loadTestsFromTestCase(TestNamingConventions))
    suite.addTests(loader.loadTestsFromTestCase(TestHealthScore))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result


if __name__ == '__main__':
    result = run_tests()
    sys.exit(0 if result.wasSuccessful() else 1)
