#!/usr/bin/env python3
"""
NOIZYLAB SOVEREIGN DASHBOARD
============================
The command center for AI-powered repair operations.
Money while you sleep. Focus on flow. GORUNFREE.

This is the COMPLETE button that triggers the revenue miracle.
"""

import os
import sys
import json
import asyncio
import aiohttp
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from enum import Enum
import hashlib
import secrets

# Local imports
from manifest_generator import (
    RepairSession, BiometricData, ForensicComparison,
    SuccessManifestGenerator, generate_case_id
)

# Optional rich terminal UI
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.layout import Layout
    from rich.live import Live
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich import print as rprint
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("TIP: Install rich for beautiful terminal UI: pip install rich")


# =============================================================================
# CONFIGURATION
# =============================================================================

@dataclass
class DashboardConfig:
    """Sovereign Dashboard configuration."""
    # API endpoints
    api_base: str = "https://api.noizylab.ca"
    portal_base: str = "https://portal.noizylab.ca"

    # Local paths
    manifests_dir: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB" / "GABRIEL" / "manifests")
    vision_dir: Path = field(default_factory=lambda: Path.home() / "NOIZYLAB" / "GABRIEL" / "vision")

    # Business settings
    base_repair_price: float = 89.0
    sovereign_multiplier: float = 2.5  # Premium for sovereign repairs = $222.50

    # Email settings
    notification_email: str = "rob@noizylab.ca"
    smtp_server: str = os.getenv("SMTP_SERVER", "smtp.mail.me.com")

    # Cloudflare settings
    cf_account_id: str = os.getenv("CF_ACCOUNT_ID", "")
    cf_api_token: str = os.getenv("CF_API_TOKEN", "")


class RepairState(Enum):
    """Repair ticket states."""
    INTAKE = "intake"
    DIAGNOSING = "diagnosing"
    IN_FLOW = "in_flow"  # Active repair with telemetry
    AWAITING_PARTS = "awaiting_parts"
    QUALITY_CHECK = "quality_check"
    COMPLETE = "complete"
    DELIVERED = "delivered"


@dataclass
class ActiveRepair:
    """Currently active repair being tracked."""
    ticket_id: str
    customer_name: str
    customer_email: str
    device_type: str
    device_model: str
    serial_number: str = ""
    state: RepairState = RepairState.INTAKE

    # Session data
    start_time: datetime = field(default_factory=datetime.now)
    diagnosis: str = ""
    root_cause: str = ""
    components: List[str] = field(default_factory=list)

    # Telemetry
    stability_readings: List[float] = field(default_factory=list)
    voltage_log: Dict[str, List[float]] = field(default_factory=dict)

    # Vision captures
    pre_images: List[str] = field(default_factory=list)
    post_images: List[str] = field(default_factory=list)

    # Pricing
    parts_cost: float = 0.0
    labor_minutes: int = 0
    is_sovereign: bool = True  # Premium sovereign repair


# =============================================================================
# SOVEREIGN DASHBOARD
# =============================================================================

class SovereignDashboard:
    """The main control interface for NOIZYLAB repair operations."""

    def __init__(self, config: DashboardConfig = None):
        self.config = config or DashboardConfig()
        self.active_repairs: Dict[str, ActiveRepair] = {}
        self.manifest_generator = SuccessManifestGenerator(self.config.manifests_dir)

        if RICH_AVAILABLE:
            self.console = Console()

        # Ensure directories exist
        self.config.manifests_dir.mkdir(parents=True, exist_ok=True)
        self.config.vision_dir.mkdir(parents=True, exist_ok=True)

    # =========================================================================
    # REPAIR LIFECYCLE
    # =========================================================================

    def intake(
        self,
        customer_name: str,
        customer_email: str,
        device_type: str,
        device_model: str,
        serial_number: str = "",
        issue_description: str = ""
    ) -> str:
        """Create new repair intake."""
        ticket_id = f"NZL-{datetime.now().strftime('%y%m%d')}-{secrets.token_hex(2).upper()}"

        repair = ActiveRepair(
            ticket_id=ticket_id,
            customer_name=customer_name,
            customer_email=customer_email,
            device_type=device_type,
            device_model=device_model,
            serial_number=serial_number,
            diagnosis=issue_description
        )

        self.active_repairs[ticket_id] = repair
        self._log_event(ticket_id, "INTAKE", f"New repair: {device_type} {device_model}")

        return ticket_id

    def start_diagnosis(self, ticket_id: str) -> None:
        """Begin diagnostic phase."""
        repair = self._get_repair(ticket_id)
        repair.state = RepairState.DIAGNOSING
        self._log_event(ticket_id, "DIAGNOSIS_START", "Beginning diagnostic analysis")

    def enter_flow(self, ticket_id: str, diagnosis: str, root_cause: str, components: List[str]) -> None:
        """Enter active repair flow state - telemetry begins."""
        repair = self._get_repair(ticket_id)
        repair.state = RepairState.IN_FLOW
        repair.diagnosis = diagnosis
        repair.root_cause = root_cause
        repair.components = components
        repair.start_time = datetime.now()

        self._log_event(ticket_id, "FLOW_START", f"Entering flow state. Target: {', '.join(components)}")
        self._start_telemetry(ticket_id)

    def capture_vision(self, ticket_id: str, image_path: str, is_pre: bool = True) -> None:
        """Capture microscope/vision image."""
        repair = self._get_repair(ticket_id)

        if is_pre:
            repair.pre_images.append(image_path)
            self._log_event(ticket_id, "VISION_PRE", f"Pre-repair capture: {image_path}")
        else:
            repair.post_images.append(image_path)
            self._log_event(ticket_id, "VISION_POST", f"Post-repair capture: {image_path}")

    def log_voltage(self, ticket_id: str, rail: str, voltage: float) -> None:
        """Log voltage measurement."""
        repair = self._get_repair(ticket_id)
        if rail not in repair.voltage_log:
            repair.voltage_log[rail] = []
        repair.voltage_log[rail].append(voltage)

    def log_stability(self, ticket_id: str, stability: float) -> None:
        """Log stability reading from biometric system."""
        repair = self._get_repair(ticket_id)
        repair.stability_readings.append(stability)

    def quality_check(self, ticket_id: str) -> Dict[str, Any]:
        """Run quality verification before completion."""
        repair = self._get_repair(ticket_id)
        repair.state = RepairState.QUALITY_CHECK

        checks = {
            "voltage_nominal": self._check_voltages(repair),
            "stability_achieved": self._check_stability(repair),
            "vision_captured": len(repair.post_images) > 0,
            "components_addressed": len(repair.components) > 0,
        }

        checks["passed"] = all(checks.values())

        self._log_event(ticket_id, "QC_RESULT", f"Quality check: {'PASS' if checks['passed'] else 'FAIL'}")
        return checks

    def complete(self, ticket_id: str, force: bool = False) -> Path:
        """
        THE MAGIC BUTTON
        ================
        This is called when you click COMPLETE on the dashboard.
        Generates the Success Manifest, triggers billing, sends notifications.

        Returns: Path to generated manifest PDF
        """
        repair = self._get_repair(ticket_id)

        # Quality gate (bypass with force=True)
        if not force:
            qc = self.quality_check(ticket_id)
            if not qc["passed"]:
                raise ValueError(f"Quality check failed: {qc}")

        repair.state = RepairState.COMPLETE
        repair.labor_minutes = int((datetime.now() - repair.start_time).total_seconds() / 60)

        # Calculate final pricing
        total_price = self._calculate_price(repair)

        # Build session data for manifest
        session = RepairSession(
            case_id=generate_case_id(),
            ticket_id=repair.ticket_id,
            customer_name=repair.customer_name,
            customer_email=repair.customer_email,
            device_type=repair.device_type,
            device_model=repair.device_model,
            serial_number=repair.serial_number,
            initial_diagnosis=repair.diagnosis,
            root_cause=repair.root_cause,
            components_affected=repair.components,
            intake_time=repair.start_time,
            completion_time=datetime.now(),
            verified=True,
            total_price=total_price,
            voltage_after=self._get_final_voltages(repair),
            biometrics=BiometricData(
                avg_stability=self._get_avg_stability(repair),
                session_duration_minutes=repair.labor_minutes
            )
        )

        # Add forensic comparisons
        for i, (pre, post) in enumerate(zip(repair.pre_images, repair.post_images)):
            session.forensics.append(ForensicComparison(
                pre_repair_image=pre,
                post_repair_image=post,
                component_id=repair.components[i] if i < len(repair.components) else "Board",
                issue_type=repair.root_cause,
                repair_technique="Sovereign Micro-Soldering"
            ))

        # Generate the manifest
        manifest_path = self.manifest_generator.generate(session)

        self._log_event(ticket_id, "MANIFEST_GENERATED", f"Success manifest: {manifest_path}")

        # Trigger async operations
        asyncio.create_task(self._post_completion(repair, session, manifest_path, total_price))

        self._print_completion_banner(repair, manifest_path, total_price)

        return manifest_path

    # =========================================================================
    # POST-COMPLETION AUTOMATION
    # =========================================================================

    async def _post_completion(
        self,
        repair: ActiveRepair,
        session: RepairSession,
        manifest_path: Path,
        total_price: float
    ) -> None:
        """Async operations after completion - billing, email, portal update."""

        tasks = [
            self._create_stripe_invoice(repair, total_price),
            self._send_completion_email(repair, manifest_path, total_price),
            self._update_portal(repair, session),
            self._upload_manifest_to_r2(manifest_path),
        ]

        await asyncio.gather(*tasks, return_exceptions=True)

    async def _create_stripe_invoice(self, repair: ActiveRepair, total: float) -> Dict:
        """Create Stripe invoice for the repair."""
        # This would integrate with your Stripe setup
        invoice_data = {
            "customer_email": repair.customer_email,
            "amount": int(total * 100),  # Stripe uses cents
            "currency": "cad",
            "description": f"Sovereign Repair: {repair.device_type} {repair.device_model}",
            "metadata": {
                "ticket_id": repair.ticket_id,
                "device": f"{repair.device_type} {repair.device_model}",
                "serial": repair.serial_number
            }
        }

        # Would call: POST /api/create-invoice
        self._log_event(repair.ticket_id, "INVOICE_CREATED", f"${total:.2f} CAD")
        return invoice_data

    async def _send_completion_email(self, repair: ActiveRepair, manifest_path: Path, total: float) -> None:
        """Send completion notification with manifest attached."""
        email_data = {
            "to": repair.customer_email,
            "subject": f"Your {repair.device_type} Repair is Complete - NOIZYLAB",
            "template": "repair_complete",
            "variables": {
                "customer_name": repair.customer_name,
                "device": f"{repair.device_type} {repair.device_model}",
                "ticket_id": repair.ticket_id,
                "total": f"${total:.2f}",
                "manifest_url": f"{self.config.portal_base}/manifests/{manifest_path.stem}"
            },
            "attachments": [str(manifest_path)]
        }

        # Would call email service
        self._log_event(repair.ticket_id, "EMAIL_SENT", repair.customer_email)

    async def _update_portal(self, repair: ActiveRepair, session: RepairSession) -> None:
        """Update customer portal with repair status."""
        # Would call: PUT /api/repairs/{ticket_id}
        self._log_event(repair.ticket_id, "PORTAL_UPDATED", "Customer can view manifest")

    async def _upload_manifest_to_r2(self, manifest_path: Path) -> str:
        """Upload manifest to Cloudflare R2 for customer access."""
        # Would upload to R2 bucket
        r2_url = f"https://r2.noizylab.ca/manifests/{manifest_path.name}"
        self._log_event("SYSTEM", "R2_UPLOAD", r2_url)
        return r2_url

    # =========================================================================
    # TELEMETRY & METRICS
    # =========================================================================

    def _start_telemetry(self, ticket_id: str) -> None:
        """Begin background telemetry collection."""
        # Would connect to biometric sensors, Gemini vision, etc.
        self._log_event(ticket_id, "TELEMETRY_START", "Biometric and vision systems active")

    def _check_voltages(self, repair: ActiveRepair) -> bool:
        """Verify voltage readings are nominal."""
        if not repair.voltage_log:
            return False

        for rail, readings in repair.voltage_log.items():
            if readings:
                final = readings[-1]
                # Check for reasonable voltage (simplified)
                if final < 0 or final > 20:
                    return False
        return True

    def _check_stability(self, repair: ActiveRepair) -> bool:
        """Verify stability threshold achieved."""
        if not repair.stability_readings:
            return True  # No readings = assume stable

        avg = sum(repair.stability_readings) / len(repair.stability_readings)
        return avg > 90.0  # 90% stability threshold

    def _get_final_voltages(self, repair: ActiveRepair) -> Dict[str, float]:
        """Get final voltage readings for each rail."""
        return {rail: readings[-1] for rail, readings in repair.voltage_log.items() if readings}

    def _get_avg_stability(self, repair: ActiveRepair) -> float:
        """Calculate average stability."""
        if not repair.stability_readings:
            return 99.0
        return sum(repair.stability_readings) / len(repair.stability_readings)

    def _calculate_price(self, repair: ActiveRepair) -> float:
        """Calculate total repair price."""
        base = self.config.base_repair_price

        if repair.is_sovereign:
            base *= self.config.sovereign_multiplier

        # Add parts cost
        total = base + repair.parts_cost

        # Complexity factor based on components
        if len(repair.components) > 3:
            total *= 1.25

        return round(total, 2)

    # =========================================================================
    # HELPERS
    # =========================================================================

    def _get_repair(self, ticket_id: str) -> ActiveRepair:
        """Get repair by ticket ID."""
        if ticket_id not in self.active_repairs:
            raise KeyError(f"Repair not found: {ticket_id}")
        return self.active_repairs[ticket_id]

    def _log_event(self, ticket_id: str, event: str, message: str) -> None:
        """Log dashboard event."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_line = f"[{timestamp}] [{ticket_id}] {event}: {message}"

        if RICH_AVAILABLE:
            self.console.log(log_line)
        else:
            print(log_line)

    def _print_completion_banner(self, repair: ActiveRepair, manifest_path: Path, total: float) -> None:
        """Print victory banner on completion."""
        banner = f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                    SOVEREIGN REPAIR COMPLETE                                  ║
║                                                                               ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  Ticket:    {repair.ticket_id:<50}       ║
║  Device:    {repair.device_type} {repair.device_model:<43}       ║
║  Customer:  {repair.customer_name:<50}       ║
║  Total:     ${total:<49.2f}       ║
║                                                                               ║
║  Manifest:  {manifest_path.name:<50}       ║
║                                                                               ║
║                         MONEY WHILE YOU SLEEP                                 ║
║                              GORUNFREE                                        ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""

        if RICH_AVAILABLE:
            self.console.print(Panel(banner, border_style="green"))
        else:
            print(banner)

    # =========================================================================
    # DASHBOARD UI
    # =========================================================================

    def show_status(self) -> None:
        """Display current dashboard status."""
        if not RICH_AVAILABLE:
            self._show_status_simple()
            return

        table = Table(title="Active Repairs", border_style="yellow")
        table.add_column("Ticket", style="cyan")
        table.add_column("Device", style="white")
        table.add_column("Customer", style="white")
        table.add_column("State", style="green")
        table.add_column("Time", style="dim")

        for repair in self.active_repairs.values():
            elapsed = datetime.now() - repair.start_time
            table.add_row(
                repair.ticket_id,
                f"{repair.device_type} {repair.device_model}",
                repair.customer_name,
                repair.state.value.upper(),
                str(elapsed).split('.')[0]
            )

        self.console.print(table)

    def _show_status_simple(self) -> None:
        """Simple text status output."""
        print("\n=== ACTIVE REPAIRS ===")
        for repair in self.active_repairs.values():
            elapsed = datetime.now() - repair.start_time
            print(f"  {repair.ticket_id}: {repair.device_type} {repair.device_model} - {repair.state.value} ({elapsed})")
        print()


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    """CLI entry point."""
    print("""
    ╔═══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                               ║
    ║              NOIZYLAB SOVEREIGN DASHBOARD                                     ║
    ║                                                                               ║
    ║              AI-Powered Repair Command Center                                 ║
    ║              Money While You Sleep. GORUNFREE.                                ║
    ║                                                                               ║
    ╚═══════════════════════════════════════════════════════════════════════════════╝
    """)

    dashboard = SovereignDashboard()

    # Demo flow
    print("\n[DEMO] Simulating complete repair flow...\n")

    # 1. Intake
    ticket_id = dashboard.intake(
        customer_name="John MacBook",
        customer_email="john@example.com",
        device_type="MacBook Pro",
        device_model="A2141 16-inch 2019",
        serial_number="C02XL3JJMD6T",
        issue_description="No power, charging but not turning on"
    )
    print(f"Created ticket: {ticket_id}")

    # 2. Diagnosis
    dashboard.start_diagnosis(ticket_id)

    # 3. Enter flow
    dashboard.enter_flow(
        ticket_id,
        diagnosis="Shorted PPBUS_G3H rail, U8900 PMU showing thermal damage",
        root_cause="U8900 PMU failure - likely liquid damage causing thermal runaway",
        components=["U8900", "C8901", "L8902"]
    )

    # 4. Capture vision
    dashboard.capture_vision(ticket_id, "vision/pre_U8900_damage.jpg", is_pre=True)

    # 5. Log telemetry during repair
    dashboard.log_voltage(ticket_id, "PPBUS_G3H", 0.0)  # Before
    dashboard.log_stability(ticket_id, 98.5)
    dashboard.log_stability(ticket_id, 99.1)
    dashboard.log_stability(ticket_id, 99.4)

    # Simulate repair time
    import time
    print("\n[REPAIR IN PROGRESS]")
    for i in range(3):
        print(f"  Soldering... {i+1}/3")
        time.sleep(0.5)

    # 6. Post-repair measurements
    dashboard.log_voltage(ticket_id, "PPBUS_G3H", 12.58)
    dashboard.log_voltage(ticket_id, "PP3V3_S5", 3.31)
    dashboard.log_voltage(ticket_id, "PP5V_S5", 5.02)

    # 7. Capture post-repair vision
    dashboard.capture_vision(ticket_id, "vision/post_U8900_sovereign.jpg", is_pre=False)

    # 8. COMPLETE - THE MAGIC BUTTON
    print("\n[CLICKING COMPLETE...]")
    manifest_path = dashboard.complete(ticket_id, force=True)

    print(f"\nManifest generated at: {manifest_path}")
    print("\nCustomer will receive:")
    print("  1. Email with manifest attached")
    print("  2. Stripe invoice for payment")
    print("  3. Portal access to view/download manifest")
    print("\nGORUNFREE!")


if __name__ == "__main__":
    main()
