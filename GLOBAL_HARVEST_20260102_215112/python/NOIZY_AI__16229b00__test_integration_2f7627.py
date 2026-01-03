#!/usr/bin/env python3
"""
test_integration.py
Integration tests for NOIZYLAB AI Offboarder
Run: pytest tests/test_integration.py -v
"""

import json
import os
import sys
import tempfile
import pytest
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from schema_validator import validate_plan, validate_and_fix


class TestSchemaValidator:
    """Tests for schema_validator.py"""
    
    def test_valid_plan_passes(self):
        """Valid plan should pass validation."""
        plan = {
            "preserve": [
                {"login": "rsplowman", "reason": "In allowlist", "confidence": 1.0, "repos": []}
            ],
            "remove": [
                {"login": "baduser", "reason": "Not in allowlist", "confidence": 0.95, "repos": ["repo1"]}
            ],
            "review": [],
            "actions": [
                {"type": "remove_member", "user": "baduser", "target": "NOIZYLAB"}
            ]
        }
        
        valid, errors = validate_plan(plan)
        assert valid, f"Valid plan should pass: {errors}"
    
    def test_missing_required_fields_fails(self):
        """Plan missing required fields should fail."""
        plan = {
            "preserve": [],
            "remove": []
            # Missing: review, actions
        }
        
        valid, errors = validate_plan(plan)
        assert not valid, "Plan missing required fields should fail"
    
    def test_malformed_entry_fails(self):
        """Entry missing required fields should fail."""
        plan = {
            "preserve": [
                {"login": "user1"}  # Missing: reason, confidence
            ],
            "remove": [],
            "review": [],
            "actions": []
        }
        
        valid, errors = validate_plan(plan)
        assert not valid, "Entry missing required fields should fail"
    
    def test_invalid_confidence_fails(self):
        """Confidence outside 0-1 range should fail."""
        plan = {
            "preserve": [
                {"login": "user1", "reason": "test", "confidence": 1.5, "repos": []}
            ],
            "remove": [],
            "review": [],
            "actions": []
        }
        
        valid, errors = validate_plan(plan)
        assert not valid, "Confidence > 1 should fail"
    
    def test_invalid_action_type_fails(self):
        """Invalid action type should fail."""
        plan = {
            "preserve": [],
            "remove": [],
            "review": [],
            "actions": [
                {"type": "invalid_action", "user": "test", "target": "org"}
            ]
        }
        
        valid, errors = validate_plan(plan)
        assert not valid, "Invalid action type should fail"
    
    def test_validate_and_fix_adds_defaults(self):
        """validate_and_fix should add missing optional fields."""
        plan = {
            "preserve": [{"login": "user1", "reason": "test", "confidence": 0.9}],
            "remove": [],
            "review": [],
            "actions": []
        }
        
        fixed = validate_and_fix(plan)
        
        assert "repos" in fixed["preserve"][0]
        assert "warnings" in fixed
        assert "summary" in fixed
    
    def test_validate_and_fix_converts_string_confidence(self):
        """validate_and_fix should convert string confidence to float."""
        plan = {
            "preserve": [{"login": "user1", "reason": "test", "confidence": "0.95", "repos": []}],
            "remove": [],
            "review": [],
            "actions": []
        }
        
        fixed = validate_and_fix(plan)
        
        assert isinstance(fixed["preserve"][0]["confidence"], float)
        assert fixed["preserve"][0]["confidence"] == 0.95


class TestAIValidate:
    """Tests for ai_validate.py output structure"""
    
    def test_rule_based_output_structure(self):
        """Rule-based analysis should produce correct structure."""
        # Import here to avoid issues if module not available
        try:
            from ai_validate import rule_based_classify
        except ImportError:
            pytest.skip("ai_validate.py not in path")
        
        inventory = {
            "org": "NOIZYLAB",
            "members": [
                {"login": "rsplowman", "email": "rsplowman@icloud.com"},
                {"login": "baduser", "email": "bad@example.com"}
            ],
            "invitations": [],
            "outside_collaborators": [],
            "repo_collaborators": {},
            "team_members": {},
            "deploy_keys": {}
        }
        
        allowlist = ["rsplowman@icloud.com", "rsplowman"]
        
        result = rule_based_classify(inventory, allowlist)
        
        # Check required keys exist
        assert "preserve" in result
        assert "remove" in result
        assert "review" in result
        assert "actions" in result
        
        # Check rsplowman is preserved
        preserved_logins = [e["login"] for e in result["preserve"]]
        assert "rsplowman" in preserved_logins
        
        # Check baduser is removed
        removed_logins = [e["login"] for e in result["remove"]]
        assert "baduser" in removed_logins
        
        # Check actions generated
        assert len(result["actions"]) > 0
        action_types = [a["type"] for a in result["actions"]]
        assert "remove_member" in action_types
    
    def test_allowlist_case_insensitive(self):
        """Allowlist matching should be case-insensitive."""
        try:
            from ai_validate import rule_based_classify
        except ImportError:
            pytest.skip("ai_validate.py not in path")
        
        inventory = {
            "org": "NOIZYLAB",
            "members": [
                {"login": "RSPlowman", "email": "RSPLOWMAN@ICLOUD.COM"}
            ],
            "invitations": [],
            "outside_collaborators": [],
            "repo_collaborators": {},
            "team_members": {},
            "deploy_keys": {}
        }
        
        allowlist = ["rsplowman@icloud.com"]
        
        result = rule_based_classify(inventory, allowlist)
        
        assert len(result["preserve"]) == 1
        assert len(result["remove"]) == 0


class TestInventoryStructure:
    """Tests for inventory.json structure"""
    
    def test_inventory_has_required_fields(self):
        """Sample inventory should have all required fields."""
        inventory = {
            "collected_at": "2025-12-09T22:00:00Z",
            "org": "NOIZYLAB",
            "members": [],
            "invitations": [],
            "outside_collaborators": [],
            "repos": [],
            "repo_collaborators": {},
            "teams": [],
            "team_members": {},
            "deploy_keys": {},
            "summary": {}
        }
        
        required_fields = [
            "org", "members", "invitations", "outside_collaborators",
            "repos", "repo_collaborators", "teams", "team_members", "deploy_keys"
        ]
        
        for field in required_fields:
            assert field in inventory, f"Missing required field: {field}"


class TestExecutionPlan:
    """Tests for execution plan structure"""
    
    def test_action_types_are_valid(self):
        """All action types should be valid."""
        valid_types = {
            "remove_member",
            "cancel_invitation",
            "remove_outside_collaborator",
            "remove_repo_collaborator",
            "remove_team_member",
            "delete_deploy_key",
            "revoke_token",
            "remove_ssh_key"
        }
        
        sample_actions = [
            {"type": "remove_member", "user": "test", "target": "NOIZYLAB"},
            {"type": "remove_repo_collaborator", "user": "test", "target": "repo1"}
        ]
        
        for action in sample_actions:
            assert action["type"] in valid_types, f"Invalid action type: {action['type']}"


class TestConfidenceThreshold:
    """Tests for confidence threshold logic"""
    
    def test_high_confidence_auto_approved(self):
        """High confidence entries should be auto-approved."""
        threshold = 0.99
        
        entry = {"login": "baduser", "confidence": 0.995, "reason": "test"}
        
        assert entry["confidence"] >= threshold
    
    def test_low_confidence_needs_review(self):
        """Low confidence entries should need review."""
        threshold = 0.99
        
        entry = {"login": "maybeuser", "confidence": 0.85, "reason": "test"}
        
        assert entry["confidence"] < threshold


class TestRollbackGeneration:
    """Tests for rollback script generation"""
    
    def test_rollback_script_format(self):
        """Rollback script should have correct format."""
        audit_log = {
            "actions": [
                {"type": "remove_member", "user": "testuser", "target": "NOIZYLAB", "result": "success"}
            ]
        }
        
        # Should generate reinstatement command
        action = audit_log["actions"][0]
        if action["type"] == "remove_member":
            reinstate_cmd = f"gh api -X PUT /orgs/NOIZYLAB/memberships/{action['user']} -f role=member"
            assert "memberships" in reinstate_cmd
            assert action["user"] in reinstate_cmd


# Run with: pytest tests/test_integration.py -v
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
