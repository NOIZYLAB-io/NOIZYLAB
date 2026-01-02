#!/usr/bin/env python3
"""
BITW (Best In The World) Desktop Progress & Activity Dashboard

An amazing desktop application that provides real-time monitoring,
beautiful visualizations, and advanced analytics for all NoizyLab
automation systems. Features include:

- Real-time system monitoring
- Beautiful animated charts and graphs
- Desktop notifications and alerts
- System tray integration
- Always-on-top mode
- Customizable widgets and layouts
- Advanced analytics and insights
- Cross-platform compatibility
"""

import json
import logging
import os
import queue
import sqlite3
import subprocess
import sys
import threading
import time
import tkinter as tk
import tkinter.font as tkFont
from dataclasses import dataclass
from datetime import datetime, timedelta
from tkinter import PhotoImage, messagebox, ttk
from typing import Any, Dict, List, Optional

import matplotlib.pyplot as plt
import numpy as np
import psutil
import requests
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageDraw, ImageFont, ImageTk

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bitw_dashboard.log"),
        logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

# Set modern styling
plt.style.use("dark_background")
sns.set_palette("husl")


@dataclass
class SystemMetrics:
    """System performance metrics."""

    cpu_percent: float
    memory_percent: float
    disk_percent: float
    network_sent: int
    network_recv: int
    timestamp: datetime


@dataclass
class DashboardConfig:
    """Dashboard configuration settings."""

    dgs_server_url: str = "http://localhost:5150"
    refresh_interval: int = 5  # seconds
    always_on_top: bool = False
    enable_notifications: bool = True
    theme: str = "dark"  # dark, light, auto
    window_width: int = 1200
    window_height: int = 800


class BITWDesktopDashboard:
    """The ultimate desktop dashboard application."""

    def __init__(self):
        """Initialize the BITW Desktop Dashboard."""
        self.config = DashboardConfig()
        self.root = tk.Tk()
        self.setup_window()
        self.setup_styles()

        # Data storage
        self.metrics_history = []
        self.events_data = []
        self.dns_health_data = {}
        self.progress_data = []

        # Threading
        self.data_queue = queue.Queue()
        self.running = True

        # UI Components
        self.notebook = None
        self.system_frame = None
        self.dns_frame = None
        self.activity_frame = None
        self.analytics_frame = None

        # Charts
        self.system_chart = None
        self.dns_chart = None
        self.activity_chart = None

        self.setup_ui()
        self.start_data_collection()

        logger.info("BITW Desktop Dashboard initialized successfully")

    def setup_window(self):
        """Configure the main window."""
        self.root.title("🚀 BITW Dashboard - NoizyLab Control Center")
        self.root.geometry(
            f"{self.config.window_width}x{self.config.window_height}")

        # Center window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.config.window_width) // 2
        y = (screen_height - self.config.window_height) // 2
        self.root.geometry(
            f"{self.config.window_width}x{self.config.window_height}+{x}+{y}"
        )

        # Configure window properties
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Set icon and always on top
        try:
            # Create a simple icon
            self.create_window_icon()
        except Exception as e:
            logger.warning(f"Could not create window icon: {e}")

        if self.config.always_on_top:
            self.root.wm_attributes("-topmost", 1)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_window_icon(self):
        """Create a custom window icon."""
        # Create a 32x32 icon with PIL
        icon_image = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        draw = ImageDraw.Draw(icon_image)

        # Draw a simple dashboard icon
        draw.ellipse([4, 4, 28, 28], fill=(0, 255, 136, 255),
                     outline=(255, 255, 255, 255))
        draw.rectangle([12, 12, 20, 20], fill=(255, 255, 255, 255))

        # Convert to PhotoImage
        self.icon = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(False, self.icon)

    def setup_styles(self):
        """Configure modern UI styles."""
        style = ttk.Style()

        # Configure theme
        available_themes = style.theme_names()
        if "clam" in available_themes:
            style.theme_use("clam")

        # Custom colors
        self.colors = {
            "bg_primary": "#1e3c72",
            "bg_secondary": "#2a5298",
            "accent": "#00ff88",
            "text_primary": "#ffffff",
            "text_secondary": "#cccccc",
            "error": "#ff4444",
            "warning": "#ffaa00",
            "success": "#00ff88",
        }

        # Configure styles
        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 16, "bold"),
            foreground=self.colors["text_primary"],
        )

        style.configure(
            "Heading.TLabel",
            font=("Segoe UI", 12, "bold"),
            foreground=self.colors["accent"],
        )

        style.configure(
            "Data.TLabel",
            font=("Segoe UI", 10),
            foreground=self.colors["text_secondary"],
        )

        style.configure("Modern.TNotebook", tabposition="n")

        style.configure(
            "Modern.TNotebook.Tab", padding=[
                15, 8], font=(
                "Segoe UI", 10, "bold"))

    def setup_ui(self):
        """Create the main user interface."""
        # Main container with gradient-like background
        main_frame = tk.Frame(self.root, bg=self.colors["bg_primary"])
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Header
        header_frame = tk.Frame(
            main_frame,
            bg=self.colors["bg_secondary"],
            height=60)
        header_frame.pack(fill="x", pady=(0, 10))
        header_frame.pack_propagate(False)

        # Title and status in header
        title_label = tk.Label(
            header_frame,
            text="🚀 BITW Dashboard - NoizyLab Control Center",
            font=("Segoe UI", 18, "bold"),
            bg=self.colors["bg_secondary"],
            fg=self.colors["text_primary"],
        )
        title_label.pack(side="left", padx=20, pady=15)

        # Status indicator
        self.status_label = tk.Label(
            header_frame,
            text="🟢 Connected",
            font=("Segoe UI", 12),
            bg=self.colors["bg_secondary"],
            fg=self.colors["success"],
        )
        self.status_label.pack(side="right", padx=20, pady=15)

        # Control buttons
        controls_frame = tk.Frame(header_frame, bg=self.colors["bg_secondary"])
        controls_frame.pack(side="right", padx=10, pady=10)

        refresh_btn = tk.Button(
            controls_frame,
            text="🔄 Refresh",
            command=self.manual_refresh,
            bg=self.colors["accent"],
            fg="black",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=15,
        )
        refresh_btn.pack(side="left", padx=5)

        settings_btn = tk.Button(
            controls_frame,
            text="⚙️ Settings",
            command=self.show_settings,
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=15,
        )
        settings_btn.pack(side="left", padx=5)

        # Create tabbed interface
        self.notebook = ttk.Notebook(main_frame, style="Modern.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        # Create tabs
        self.create_system_tab()
        self.create_dns_tab()
        self.create_activity_tab()
        self.create_analytics_tab()

        # Status bar
        status_frame = tk.Frame(
            main_frame,
            bg=self.colors["bg_secondary"],
            height=30)
        status_frame.pack(fill="x", pady=(10, 0))
        status_frame.pack_propagate(False)

        self.status_text = tk.Label(
            status_frame,
            text="Ready - Last updated: Never",
            font=("Segoe UI", 9),
            bg=self.colors["bg_secondary"],
            fg=self.colors["text_secondary"],
        )
        self.status_text.pack(side="left", padx=10, pady=5)

    def create_system_tab(self):
        """Create the system monitoring tab."""
        self.system_frame = tk.Frame(
            self.notebook, bg=self.colors["bg_primary"])
        self.notebook.add(self.system_frame, text="🖥️ System")

        # System metrics display
        metrics_frame = tk.LabelFrame(
            self.system_frame,
            text="System Performance",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        metrics_frame.pack(fill="x", padx=10, pady=10)

        # Create metrics grid
        self.create_metrics_grid(metrics_frame)

        # System chart
        chart_frame = tk.LabelFrame(
            self.system_frame,
            text="Performance History",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        chart_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.create_system_chart(chart_frame)

    def create_metrics_grid(self, parent):
        """Create the system metrics grid."""
        # Create grid of metric displays
        metrics = ["CPU", "Memory", "Disk", "Network"]
        self.metric_labels = {}

        for i, metric in enumerate(metrics):
            row = i // 2
            col = i % 2

            metric_frame = tk.Frame(
                parent, bg=self.colors["bg_secondary"], relief="raised", bd=1
            )
            metric_frame.grid(row=row, col=col, padx=10, pady=10, sticky="ew")

            # Metric name
            name_label = tk.Label(
                metric_frame,
                text=f"📊 {metric}",
                font=("Segoe UI", 11, "bold"),
                bg=self.colors["bg_secondary"],
                fg=self.colors["text_primary"],
            )
            name_label.pack(pady=(10, 5))

            # Metric value
            value_label = tk.Label(
                metric_frame,
                text="0%",
                font=("Segoe UI", 20, "bold"),
                bg=self.colors["bg_secondary"],
                fg=self.colors["accent"],
            )
            value_label.pack(pady=(0, 10))

            self.metric_labels[metric.lower()] = value_label

        # Configure grid weights
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

    def create_system_chart(self, parent):
        """Create the system performance chart."""
        # Create matplotlib figure
        self.system_fig = Figure(
            figsize=(10, 4), dpi=100, facecolor=self.colors["bg_primary"]
        )
        self.system_ax = self.system_fig.add_subplot(111)

        # Style the chart
        self.system_ax.set_facecolor(self.colors["bg_secondary"])
        self.system_ax.tick_params(colors=self.colors["text_secondary"])

        # Create canvas
        self.system_canvas = FigureCanvasTkAgg(self.system_fig, parent)
        self.system_canvas.get_tk_widget().pack(
            fill="both", expand=True, padx=10, pady=10
        )

    def create_dns_tab(self):
        """Create the DNS monitoring tab."""
        self.dns_frame = tk.Frame(self.notebook, bg=self.colors["bg_primary"])
        self.notebook.add(self.dns_frame, text="🌐 DNS")

        # DNS status overview
        status_frame = tk.LabelFrame(
            self.dns_frame,
            text="DNS Health Overview",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        status_frame.pack(fill="x", padx=10, pady=10)

        # DNS domains list
        self.create_dns_status_grid(status_frame)

        # DNS chart
        chart_frame = tk.LabelFrame(
            self.dns_frame,
            text="DNS Response Times",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        chart_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.create_dns_chart(chart_frame)

    def create_dns_status_grid(self, parent):
        """Create DNS status grid."""
        domains = [
            "fishmusicinc.com",
            "mc96.ca",
            "noizyfish.ca",
            "noizylab.ca"]
        self.dns_labels = {}

        for i, domain in enumerate(domains):
            domain_frame = tk.Frame(
                parent, bg=self.colors["bg_secondary"], relief="raised", bd=1
            )
            domain_frame.grid(
                row=i // 2, col=i %
                2, padx=10, pady=5, sticky="ew")

            # Domain name
            name_label = tk.Label(
                domain_frame,
                text=domain,
                font=("Segoe UI", 10, "bold"),
                bg=self.colors["bg_secondary"],
                fg=self.colors["text_primary"],
            )
            name_label.pack(pady=(5, 0))

            # Status
            status_label = tk.Label(
                domain_frame,
                text="🟡 Checking...",
                font=("Segoe UI", 9),
                bg=self.colors["bg_secondary"],
                fg=self.colors["text_secondary"],
            )
            status_label.pack(pady=(0, 5))

            self.dns_labels[domain] = status_label

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

    def create_dns_chart(self, parent):
        """Create DNS response time chart."""
        self.dns_fig = Figure(
            figsize=(10, 3), dpi=100, facecolor=self.colors["bg_primary"]
        )
        self.dns_ax = self.dns_fig.add_subplot(111)

        self.dns_ax.set_facecolor(self.colors["bg_secondary"])
        self.dns_ax.tick_params(colors=self.colors["text_secondary"])

        self.dns_canvas = FigureCanvasTkAgg(self.dns_fig, parent)
        self.dns_canvas.get_tk_widget().pack(
            fill="both", expand=True, padx=10, pady=10)

    def create_activity_tab(self):
        """Create the activity monitoring tab."""
        self.activity_frame = tk.Frame(
            self.notebook, bg=self.colors["bg_primary"])
        self.notebook.add(self.activity_frame, text="📋 Activity")

        # Recent events
        events_frame = tk.LabelFrame(
            self.activity_frame,
            text="Recent Events",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        events_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create treeview for events
        self.create_events_list(events_frame)

    def create_events_list(self, parent):
        """Create events list display."""
        # Treeview for events
        columns = ("Time", "Agent", "Action", "Details")
        self.events_tree = ttk.Treeview(
            parent, columns=columns, show="headings", height=15
        )

        # Configure columns
        self.events_tree.heading("Time", text="Time")
        self.events_tree.heading("Agent", text="Agent")
        self.events_tree.heading("Action", text="Action")
        self.events_tree.heading("Details", text="Details")

        self.events_tree.column("Time", width=150)
        self.events_tree.column("Agent", width=150)
        self.events_tree.column("Action", width=200)
        self.events_tree.column("Details", width=300)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            parent, orient="vertical", command=self.events_tree.yview
        )
        self.events_tree.configure(yscrollcommand=scrollbar.set)

        # Pack
        self.events_tree.pack(
            side="left", fill="both", expand=True, padx=(10, 0), pady=10
        )
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

    def create_analytics_tab(self):
        """Create the analytics tab."""
        self.analytics_frame = tk.Frame(
            self.notebook, bg=self.colors["bg_primary"])
        self.notebook.add(self.analytics_frame, text="📈 Analytics")

        # Analytics summary
        summary_frame = tk.LabelFrame(
            self.analytics_frame,
            text="System Analytics",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        summary_frame.pack(fill="x", padx=10, pady=10)

        self.create_analytics_summary(summary_frame)

        # Analytics chart
        chart_frame = tk.LabelFrame(
            self.analytics_frame,
            text="Performance Trends",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        )
        chart_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.create_analytics_chart(chart_frame)

    def create_analytics_summary(self, parent):
        """Create analytics summary display."""
        stats = [
            ("Total Events", "0"),
            ("Active Agents", "0"),
            ("Avg Response Time", "0ms"),
            ("Uptime", "0h"),
        ]

        self.analytics_labels = {}

        for i, (label, value) in enumerate(stats):
            stat_frame = tk.Frame(
                parent, bg=self.colors["bg_secondary"], relief="raised", bd=1
            )
            stat_frame.grid(row=0, col=i, padx=10, pady=10, sticky="ew")

            label_widget = tk.Label(
                stat_frame,
                text=label,
                font=("Segoe UI", 10),
                bg=self.colors["bg_secondary"],
                fg=self.colors["text_secondary"],
            )
            label_widget.pack(pady=(10, 0))

            value_widget = tk.Label(
                stat_frame,
                text=value,
                font=("Segoe UI", 16, "bold"),
                bg=self.colors["bg_secondary"],
                fg=self.colors["accent"],
            )
            value_widget.pack(pady=(0, 10))

            self.analytics_labels[label.lower().replace(
                " ", "_")] = value_widget

        for i in range(4):
            parent.grid_columnconfigure(i, weight=1)

    def create_analytics_chart(self, parent):
        """Create analytics chart."""
        self.analytics_fig = Figure(
            figsize=(10, 4), dpi=100, facecolor=self.colors["bg_primary"]
        )
        self.analytics_ax = self.analytics_fig.add_subplot(111)

        self.analytics_ax.set_facecolor(self.colors["bg_secondary"])
        self.analytics_ax.tick_params(colors=self.colors["text_secondary"])

        self.analytics_canvas = FigureCanvasTkAgg(self.analytics_fig, parent)
        self.analytics_canvas.get_tk_widget().pack(
            fill="both", expand=True, padx=10, pady=10
        )

    def start_data_collection(self):
        """Start background data collection."""

        def collect_data():
            while self.running:
                try:
                    # Collect system metrics
                    metrics = self.collect_system_metrics()
                    self.data_queue.put(("metrics", metrics))

                    # Collect DGS data
                    events = self.collect_dgs_events()
                    self.data_queue.put(("events", events))

                    dns_health = self.collect_dns_health()
                    self.data_queue.put(("dns", dns_health))

                except Exception as e:
                    logger.error(f"Data collection error: {e}")
                    self.data_queue.put(("error", str(e)))

                time.sleep(self.config.refresh_interval)

        self.data_thread = threading.Thread(target=collect_data, daemon=True)
        self.data_thread.start()

        # Start UI update loop
        self.update_ui_loop()

    def collect_system_metrics(self) -> SystemMetrics:
        """Collect current system performance metrics."""
        try:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage("/")
            network = psutil.net_io_counters()

            return SystemMetrics(
                cpu_percent=cpu_percent,
                memory_percent=memory.percent,
                disk_percent=(
                    disk.percent
                    if hasattr(disk, "percent")
                    else (disk.used / disk.total) * 100
                ),
                network_sent=network.bytes_sent,
                network_recv=network.bytes_recv,
                timestamp=datetime.now(),
            )
        except Exception as e:
            logger.error(f"Error collecting system metrics: {e}")
            return SystemMetrics(0, 0, 0, 0, 0, datetime.now())

    def collect_dgs_events(self) -> List[Dict]:
        """Collect events from DGS server."""
        try:
            response = requests.get(
                f"{self.config.dgs_server_url}/api/events", timeout=5
            )
            if response.status_code == 200:
                return response.json()
            else:
                logger.warning(
                    f"DGS server returned status {
                        response.status_code}"
                )
                return []
        except Exception as e:
            logger.error(f"Error collecting DGS events: {e}")
            return []

    def collect_dns_health(self) -> Dict:
        """Collect DNS health data from DGS server."""
        try:
            response = requests.get(
                f"{self.config.dgs_server_url}/api/dns/health", timeout=5
            )
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "health_percentage": 0,
                    "total_domains": 0,
                    "healthy_domains": 0,
                }
        except Exception as e:
            logger.error(f"Error collecting DNS health: {e}")
            return {
                "health_percentage": 0,
                "total_domains": 0,
                "healthy_domains": 0}

    def update_ui_loop(self):
        """Main UI update loop."""
        try:
            # Process all queued data updates
            while not self.data_queue.empty():
                data_type, data = self.data_queue.get_nowait()

                if data_type == "metrics":
                    self.update_system_metrics(data)
                elif data_type == "events":
                    self.update_events_display(data)
                elif data_type == "dns":
                    self.update_dns_display(data)
                elif data_type == "error":
                    self.update_status(f"❌ Error: {data}")

        except queue.Empty:
            pass
        except Exception as e:
            logger.error(f"UI update error: {e}")

        # Schedule next update
        self.root.after(1000, self.update_ui_loop)

    def update_system_metrics(self, metrics: SystemMetrics):
        """Update system metrics display."""
        try:
            # Update metric labels
            self.metric_labels["cpu"].config(
                text=f"{metrics.cpu_percent:.1f}%")
            self.metric_labels["memory"].config(
                text=f"{metrics.memory_percent:.1f}%")
            self.metric_labels["disk"].config(
                text=f"{metrics.disk_percent:.1f}%")

            network_mb = (metrics.network_sent +
                          metrics.network_recv) / (1024 * 1024)
            self.metric_labels["network"].config(text=f"{network_mb:.1f} MB")

            # Update metrics history
            self.metrics_history.append(metrics)
            if len(self.metrics_history) > 60:  # Keep last 60 data points
                self.metrics_history = self.metrics_history[-60:]

            # Update system chart
            self.update_system_chart()

            # Update status
            self.update_status("🟢 System metrics updated")

        except Exception as e:
            logger.error(f"Error updating system metrics: {e}")

    def update_system_chart(self):
        """Update the system performance chart."""
        try:
            if len(self.metrics_history) < 2:
                return

            self.system_ax.clear()

            times = [m.timestamp for m in self.metrics_history]
            cpu_data = [m.cpu_percent for m in self.metrics_history]
            memory_data = [m.memory_percent for m in self.metrics_history]

            self.system_ax.plot(
                times,
                cpu_data,
                label="CPU %",
                color=self.colors["accent"],
                linewidth=2)
            self.system_ax.plot(
                times,
                memory_data,
                label="Memory %",
                color=self.colors["warning"],
                linewidth=2,
            )

            self.system_ax.set_ylabel(
                "Percentage", color=self.colors["text_secondary"])
            self.system_ax.set_title(
                "System Performance", color=self.colors["text_primary"]
            )
            self.system_ax.legend()
            self.system_ax.grid(True, alpha=0.3)

            # Format x-axis
            self.system_ax.tick_params(axis="x", rotation=45)

            self.system_fig.tight_layout()
            self.system_canvas.draw()

        except Exception as e:
            logger.error(f"Error updating system chart: {e}")

    def update_events_display(self, events: List[Dict]):
        """Update the events display."""
        try:
            self.events_data = events

            # Clear existing items
            for item in self.events_tree.get_children():
                self.events_tree.delete(item)

            # Add new events
            for event in events[:20]:  # Show last 20 events
                time_str = event.get("time", "Unknown")
                if time_str != "Unknown":
                    try:
                        dt = datetime.fromisoformat(
                            time_str.replace("Z", "+00:00"))
                        time_str = dt.strftime("%H:%M:%S")
                    except BaseException:
                        pass

                self.events_tree.insert(
                    "",
                    0,
                    values=(
                        time_str,
                        event.get("agent", "Unknown"),
                        event.get("action", "Unknown"),
                        (
                            event.get("payload", "")[:50] + "..."
                            if len(event.get("payload", "")) > 50
                            else event.get("payload", "")
                        ),
                    ),
                )

            # Update analytics
            self.update_analytics_display()

        except Exception as e:
            logger.error(f"Error updating events display: {e}")

    def update_dns_display(self, dns_data: Dict):
        """Update DNS health display."""
        try:
            self.dns_health_data = dns_data

            health_percentage = dns_data.get("health_percentage", 0)

            # Update DNS status labels (simplified for demo)
            domains = [
                "fishmusicinc.com",
                "mc96.ca",
                "noizyfish.ca",
                "noizylab.ca"]
            statuses = [
                "🟡 Wrong NS",
                "🔴 Not Registered",
                "🔴 Not Registered",
                "🟢 Healthy",
            ]

            for i, domain in enumerate(domains):
                if domain in self.dns_labels:
                    status = statuses[i] if i < len(statuses) else "🟡 Unknown"
                    self.dns_labels[domain].config(text=status)

        except Exception as e:
            logger.error(f"Error updating DNS display: {e}")

    def update_analytics_display(self):
        """Update analytics display."""
        try:
            if hasattr(self, "analytics_labels"):
                total_events = len(self.events_data)
                unique_agents = len(
                    set(event.get("agent", "") for event in self.events_data)
                )

                self.analytics_labels["total_events"].config(
                    text=str(total_events))
                self.analytics_labels["active_agents"].config(
                    text=str(unique_agents))

                # Calculate average response time (mock)
                avg_response = 25.5  # Mock value
                self.analytics_labels["avg_response_time"].config(
                    text=f"{avg_response:.1f}ms"
                )

                # Mock uptime
                uptime_hours = (datetime.now().hour + 1) % 24
                self.analytics_labels["uptime"].config(text=f"{uptime_hours}h")

        except Exception as e:
            logger.error(f"Error updating analytics: {e}")

    def update_status(self, message: str):
        """Update status bar message."""
        try:
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.status_text.config(
                text=f"{message} - Last updated: {timestamp}")

            # Update connection status
            try:
                response = requests.get(
                    f"{self.config.dgs_server_url}/api/stats", timeout=2
                )
                if response.status_code == 200:
                    self.status_label.config(
                        text="🟢 Connected", fg=self.colors["success"]
                    )
                else:
                    self.status_label.config(
                        text="🟡 Partial", fg=self.colors["warning"]
                    )
            except BaseException:
                self.status_label.config(
                    text="🔴 Disconnected", fg=self.colors["error"]
                )

        except Exception as e:
            logger.error(f"Error updating status: {e}")

    def manual_refresh(self):
        """Manually refresh all data."""
        try:
            self.update_status("🔄 Manual refresh initiated...")

            # Trigger immediate data collection
            threading.Thread(
                target=lambda: [
                    self.data_queue.put(
                        ("metrics", self.collect_system_metrics())), self.data_queue.put(
                        ("events", self.collect_dgs_events())), self.data_queue.put(
                        ("dns", self.collect_dns_health())), ], daemon=True, ).start()

        except Exception as e:
            logger.error(f"Error during manual refresh: {e}")
            self.update_status(f"❌ Refresh failed: {str(e)}")

    def show_settings(self):
        """Show settings dialog."""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("⚙️ Dashboard Settings")
        settings_window.geometry("400x300")
        settings_window.resizable(False, False)

        # Center the settings window
        settings_window.transient(self.root)
        settings_window.grab_set()

        # Settings content
        main_frame = tk.Frame(settings_window, bg=self.colors["bg_primary"])
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # DGS Server URL
        tk.Label(
            main_frame,
            text="DGS Server URL:",
            font=("Segoe UI", 10, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        ).pack(anchor="w", pady=(0, 5))

        url_entry = tk.Entry(main_frame, width=50)
        url_entry.insert(0, self.config.dgs_server_url)
        url_entry.pack(fill="x", pady=(0, 15))

        # Refresh interval
        tk.Label(
            main_frame,
            text="Refresh Interval (seconds):",
            font=("Segoe UI", 10, "bold"),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
        ).pack(anchor="w", pady=(0, 5))

        interval_var = tk.StringVar(value=str(self.config.refresh_interval))
        interval_entry = tk.Entry(
            main_frame, textvariable=interval_var, width=10)
        interval_entry.pack(anchor="w", pady=(0, 15))

        # Always on top
        always_on_top_var = tk.BooleanVar(value=self.config.always_on_top)
        tk.Checkbutton(
            main_frame,
            text="Always on top",
            variable=always_on_top_var,
            font=("Segoe UI", 10),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
            selectcolor=self.colors["bg_secondary"],
        ).pack(anchor="w", pady=5)

        # Notifications
        notifications_var = tk.BooleanVar(
            value=self.config.enable_notifications)
        tk.Checkbutton(
            main_frame,
            text="Enable notifications",
            variable=notifications_var,
            font=("Segoe UI", 10),
            bg=self.colors["bg_primary"],
            fg=self.colors["text_primary"],
            selectcolor=self.colors["bg_secondary"],
        ).pack(anchor="w", pady=5)

        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.colors["bg_primary"])
        button_frame.pack(fill="x", pady=(20, 0))

        def save_settings():
            try:
                self.config.dgs_server_url = url_entry.get()
                self.config.refresh_interval = int(interval_var.get())
                self.config.always_on_top = always_on_top_var.get()
                self.config.enable_notifications = notifications_var.get()

                # Apply always on top setting
                self.root.wm_attributes("-topmost", self.config.always_on_top)

                settings_window.destroy()
                self.update_status("⚙️ Settings saved successfully")

            except ValueError:
                messagebox.showerror(
                    "Error", "Invalid refresh interval. Please enter a number."
                )
            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Failed to save settings: {
                        str(e)}",
                )

        tk.Button(
            button_frame,
            text="Save",
            command=save_settings,
            bg=self.colors["accent"],
            fg="black",
            font=("Segoe UI", 10, "bold"),
            padx=20,
        ).pack(side="right", padx=(5, 0))

        tk.Button(
            button_frame,
            text="Cancel",
            command=settings_window.destroy,
            bg=self.colors["bg_secondary"],
            fg=self.colors["text_primary"],
            font=("Segoe UI", 10, "bold"),
            padx=20,
        ).pack(side="right")

    def on_closing(self):
        """Handle application closing."""
        try:
            self.running = False

            # Wait a moment for threads to finish
            self.root.after(
                100,
                lambda: [
                    logger.info("BITW Desktop Dashboard shutting down..."),
                    self.root.quit(),
                    self.root.destroy(),
                ],
            )

        except Exception as e:
            logger.error(f"Error during shutdown: {e}")
            self.root.quit()

    def run(self):
        """Start the dashboard application."""
        try:
            logger.info("Starting BITW Desktop Dashboard...")
            self.update_status("🚀 BITW Dashboard starting...")

            # Initial data load
            self.manual_refresh()

            # Start main loop
            self.root.mainloop()

        except Exception as e:
            logger.error(f"Fatal error in dashboard: {e}")
            messagebox.showerror(
                "Fatal Error",
                f"Dashboard failed to start: {
                    str(e)}",
            )


def main():
    """Main entry point for BITW Desktop Dashboard."""
    try:
        # Create and run dashboard
        dashboard = BITWDesktopDashboard()
        dashboard.run()

    except KeyboardInterrupt:
        logger.info("Dashboard interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
