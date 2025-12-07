#!/usr/bin/env python3
"""
The Perfectionist — Modern Desktop Widget (Copilot Enhanced)
Requires: pip install PyQt6
"""

import sys, os, subprocess, threading
from PyQt6 import QtWidgets, QtGui, QtCore
from pathlib import Path

APP_TITLE = "The Perfectionist"
SCRIPT = os.path.join(os.path.dirname(__file__), "../core/cleaner.py")

# Path to your packaged app or script
# For a .app bundle (PyInstaller output):
APP_PATH = str(Path.home() / "Desktop" / "The_Perfectionist" / "ui" / "dist" / "The Perfectionist.app")
# For a Python script fallback:
SCRIPT_PATH = str(Path.home() / "Desktop" / "The_Perfectionist" / "ui" / "perfectionist_widget.py")

def add_app_to_login_items(app_path):
    # Use AppleScript to add the app to Login Items
    script = f'''
    tell application "System Events"
        if not (exists login item "{os.path.basename(app_path)}") then
            make login item at end with properties {{path:"{app_path}", hidden:false}}
        end if
    end tell
    '''
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Added to Login Items: {app_path}")
    else:
        print(f"❌ Failed to add to Login Items: {result.stderr}")

class GlowWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_TITLE)
        self.setAcceptDrops(True)
        self.setFixedSize(140, 140)
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.opacity = 0.7
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.pulse)
        self.pulse_up = True
        self.pulse_value = 0
        self.drag_over = False
        self.cleaning = False
        self.success = False

        # subtle glow animation
        self.timer.start(60)

        # click-drag window movement
        self.offset = None

        # Close button
        self.close_btn_rect = QtCore.QRect(115, 10, 16, 16)

    def paintEvent(self, event):
        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        # background circle
        gradient = QtGui.QRadialGradient(70, 70, 70)
        gradient.setColorAt(0, QtGui.QColor(60, 60, 70, 255))
        gradient.setColorAt(1, QtGui.QColor(25, 25, 30, 220))
        p.setBrush(QtGui.QBrush(gradient))
        p.setPen(QtCore.Qt.PenStyle.NoPen)
        p.drawEllipse(0, 0, 140, 140)

        # glow ring (brighter on drag-over)
        glow_alpha = 180 if self.drag_over else 120 + int(self.pulse_value)
        glow_color = QtGui.QColor(0, 220, 255, glow_alpha)
        pen = QtGui.QPen(glow_color, 6)
        p.setPen(pen)
        p.drawEllipse(8, 8, 124, 124)

        # icon glyph or checkmark
        font = QtGui.QFont("Helvetica Neue", 36, QtGui.QFont.Weight.Bold)
        p.setFont(font)
        p.setPen(QtGui.QColor(255, 255, 255, 240))
        if self.success:
            p.drawText(self.rect(), QtCore.Qt.AlignmentFlag.AlignCenter, "✅")
        elif self.cleaning:
            p.drawText(self.rect(), QtCore.Qt.AlignmentFlag.AlignCenter, "🧹")
        else:
            p.drawText(self.rect(), QtCore.Qt.AlignmentFlag.AlignCenter, "✨")

        # Close button (top right)
        p.setPen(QtGui.QColor(200, 200, 200, 180))
        p.setBrush(QtGui.QColor(60, 60, 60, 180))
        p.drawEllipse(self.close_btn_rect)
        font2 = QtGui.QFont("Arial", 10, QtGui.QFont.Weight.Bold)
        p.setFont(font2)
        p.setPen(QtGui.QColor(255, 255, 255, 220))
        p.drawText(self.close_btn_rect, QtCore.Qt.AlignmentFlag.AlignCenter, "×")

    def pulse(self):
        step = 5
        if self.pulse_up:
            self.pulse_value += step
            if self.pulse_value >= 120:
                self.pulse_up = False
        else:
            self.pulse_value -= step
            if self.pulse_value <= 0:
                self.pulse_up = True
        self.update()

    # --- drag and drop handling ---
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.drag_over = True
            self.update()

    def dragLeaveEvent(self, event):
        self.drag_over = False
        self.update()

    def dropEvent(self, event):
        self.drag_over = False
        self.update()
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isdir(path) or os.path.isfile(path):
                threading.Thread(target=self.run_cleaner, args=(path,), daemon=True).start()

    # --- move window by click-drag ---
    def mousePressEvent(self, event):
        if self.close_btn_rect.contains(event.pos()):
            self.close()
        elif event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        self.offset = None

    # --- run the perfectionist engine ---
    def run_cleaner(self, path):
        self.cleaning = True
        self.success = False
        self.timer.stop()
        self.setToolTip(f"Cleaning {os.path.basename(path)}…")
        self.update()
        subprocess.run([sys.executable, SCRIPT], env={**os.environ, "PERFECTIONIST_PATH": path})
        self.setToolTip("Done.")
        self.cleaning = False
        self.success = True
        self.update()
        QtCore.QTimer.singleShot(1200, self.reset_success)
        self.timer.start(60)

    def reset_success(self):
        self.success = False
        self.update()

if __name__ == "__main__":
    # Prefer the .app if it exists, else fallback to the script
    if os.path.exists(APP_PATH):
        add_app_to_login_items(APP_PATH)
    else:
        add_app_to_login_items(SCRIPT_PATH)

    app = QtWidgets.QApplication(sys.argv)
    w = GlowWidget()
    w.show()
    sys.exit(app.exec())