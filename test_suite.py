#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Comprehensive Test Suite
Tests all systems in NOIZYLAB
"""

import importlib.util
import json
import sys
from pathlib import Path
from typing import Dict, List

class TestSuite:
    """Comprehensive test suite for all systems"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.test_results = {}
        self.passed = 0
        self.failed = 0

    def test_file_exists(self, filename: str) -> bool:
        """Test if file exists"""
        file_path = self.base_dir / filename
        return file_path.exists()

    def test_file_imports(self, filename: str) -> bool:
        """Test if file can be imported"""
        try:
            file_path = self.base_dir / filename
            if not file_path.exists():
                return False

            spec = importlib.util.spec_from_file_location("test_module", file_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return True
            return False
        except Exception:
            return False

    def test_file_syntax(self, filename: str) -> bool:
        """Test file syntax"""
        try:
            file_path = self.base_dir / filename
            with open(file_path, 'r') as f:
                compile(f.read(), filename, 'exec')
            return True
        except SyntaxError:
            return False
        except Exception:
            return False

    def test_config_files(self) -> Dict[str, bool]:
        """Test configuration files"""
        results = {}
        config_files = [
            "super_ultimate_config.json",
            "ultimate_config.json",
            "domains_and_emails_master.json",
            "email_templates.json"
        ]

        for config_file in config_files:
            file_path = self.base_dir / config_file
            if file_path.exists():
                try:
                    with open(file_path, 'r') as f:
                        json.load(f)
                    results[config_file] = True
                except json.JSONDecodeError:
                    results[config_file] = False
            else:
                results[config_file] = None  # Optional file

        return results

    def test_directories(self) -> Dict[str, bool]:
        """Test required directories"""
        results = {}
        directories = [
            "knowledge_base",
            "solutions_database",
            "learning_database",
            "web_cache",
            "tutorials_database",
            "3d_models_database",
            "iot_database",
            "languages_database",
            "experts_database",
            "analytics_database",
            "testing_database"
        ]

        for directory in directories:
            dir_path = self.base_dir / directory
            results[directory] = dir_path.exists()

        return results

    def test_core_systems(self) -> Dict[str, bool]:
        """Test core systems"""
        results = {}
        core_systems = [
            "SUPER_ULTIMATE_SYSTEM.py",
            "ultimate_master_system.py",
            "noizylab_ai_trainer.py",
            "universal_problem_solver.py",
            "advanced_ai_engine.py",
            "email_master_control.py",
            "cloud_integration.py",
            "mobile_app_generator.py"
        ]

        for system in core_systems:
            exists = self.test_file_exists(system)
            syntax = self.test_file_syntax(system) if exists else False
            results[system] = exists and syntax

        return results

    def test_integration_systems(self) -> Dict[str, bool]:
        """Test integration systems"""
        results = {}
        integration_systems = [
            "web_integration.py",
            "video_tutorials.py",
            "3d_models.py",
            "iot_device_support.py",
            "multi_language_support.py",
            "expert_network.py",
            "analytics_dashboard.py",
            "automated_testing.py"
        ]

        for system in integration_systems:
            exists = self.test_file_exists(system)
            syntax = self.test_file_syntax(system) if exists else False
            results[system] = exists and syntax

        return results

    def run_all_tests(self):
        """Run all tests"""
        print("\n" + "="*80)
        print("🧪 COMPREHENSIVE TEST SUITE")
        print("="*80)

        # Test core systems
        print("\n1️⃣  Testing Core Systems...")
        core_results = self.test_core_systems()
        for system, result in core_results.items():
            status = "✅" if result else "❌"
            print(f"  {status} {system}")
            if result:
                self.passed += 1
            else:
                self.failed += 1

        # Test integration systems
        print("\n2️⃣  Testing Integration Systems...")
        integration_results = self.test_integration_systems()
        for system, result in integration_results.items():
            status = "✅" if result else "❌"
            print(f"  {status} {system}")
            if result:
                self.passed += 1
            else:
                self.failed += 1

        # Test config files
        print("\n3️⃣  Testing Configuration Files...")
        config_results = self.test_config_files()
        for config, result in config_results.items():
            if result is None:
                print(f"  ⏭️  {config} (optional)")
            else:
                status = "✅" if result else "❌"
                print(f"  {status} {config}")
                if result:
                    self.passed += 1
                elif result is False:
                    self.failed += 1

        # Test directories
        print("\n4️⃣  Testing Directories...")
        dir_results = self.test_directories()
        for directory, exists in dir_results.items():
            status = "✅" if exists else "⏳"
            print(f"  {status} {directory}")
            if exists:
                self.passed += 1

        # Summary
        print("\n" + "="*80)
        print("📊 TEST SUMMARY")
        print("="*80)
        print(f"  ✅ Passed: {self.passed}")
        print(f"  ❌ Failed: {self.failed}")
        print(f"  📊 Total: {self.passed + self.failed}")

        if self.failed == 0:
            print("\n🎉 ALL TESTS PASSED!")
        else:
            print(f"\n⚠️  {self.failed} test(s) failed")

        print("="*80)

if __name__ == "__main__":
    suite = TestSuite()
    suite.run_all_tests()

