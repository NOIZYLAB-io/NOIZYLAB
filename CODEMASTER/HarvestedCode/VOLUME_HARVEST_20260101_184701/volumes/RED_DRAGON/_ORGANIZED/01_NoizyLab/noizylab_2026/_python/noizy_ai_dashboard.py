import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt, QTimer

# Simulated minion/task data
class Minion:
    def __init__(self, minion_id, squad, task, status):
        self.minion_id = minion_id
        self.squad = squad
        self.task = task
        self.status = status
        self.progress = 0
        self.turbo_mode = False
        self.start_time = time.time()

    def update_progress(self):
        if self.status == 'working':
            self.progress = min(100, self.progress + (2 if self.turbo_mode else 1))
            if self.progress >= 100:
                self.status = 'completed'

class MinionDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('🥷 Noizy.AI Minion Dashboard')
        self.setGeometry(100, 100, 600, 450)
        self.minions = [
            Minion('FRONTEND-001', 'Development', 'UI Build', 'working'),
            Minion('AI-VOICE-001', 'AI', 'Voice Synthesis', 'idle'),
            Minion('QA-001', 'QA', 'Testing', 'working'),
            Minion('MARKETING-001', 'Marketing', 'Campaign', 'completed'),
        ]
        self.layout = QVBoxLayout()
        self.title = QLabel('🥷 <span style="color:#0072ff">Noizy.AI Minion Dashboard</span>')
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('font-size: 28px; font-weight: bold; background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00c6ff, stop:1 #0072ff); color: white; border-radius: 8px; padding: 12px;')
        self.title.setTextFormat(Qt.RichText)
        self.layout.addWidget(self.title)
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet('background: #181c24; color: #e0e0e0; border-radius: 8px; font-size: 16px;')
        self.layout.addWidget(self.list_widget)
        self.refresh_button = QPushButton('🔄 Refresh')
        self.refresh_button.setStyleSheet('background: #0072ff; color: white; font-weight: bold; border-radius: 6px; padding: 8px;')
        self.refresh_button.clicked.connect(self.refresh)
        self.layout.addWidget(self.refresh_button)
        self.turbo_button = QPushButton('⚡ Activate Turbo Mode')
        self.turbo_button.setStyleSheet('background: #00c6ff; color: white; font-weight: bold; border-radius: 6px; padding: 8px;')
        self.turbo_button.clicked.connect(self.activate_turbo)
        self.layout.addWidget(self.turbo_button)
        self.setLayout(self.layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_minions)
        self.timer.start(1000)
        self.refresh()

    def refresh(self):
        self.list_widget.clear()
        for minion in self.minions:
            item = QListWidgetItem()
            widget = QWidget()
            h_layout = QHBoxLayout()
            label = QLabel(f"<span style='font-size:20px;'>{get_squad_icon(minion.squad)}</span> <b>{minion.minion_id}</b> <span style='color:#00c6ff'>[{minion.squad}]</span> - <span style='color:#fff'>{minion.task}</span>")
            label.setTextFormat(Qt.RichText)
            status = QLabel(f"Status: <b>{minion.status}</b>")
            status.setTextFormat(Qt.RichText)
            progress = QProgressBar()
            progress.setValue(minion.progress)
            progress.setMaximum(100)
            progress.setMinimum(0)
            progress.setStyleSheet('QProgressBar {background: #222; border-radius: 4px;} QProgressBar::chunk {background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00c6ff, stop:1 #0072ff); border-radius: 4px;}')
            if minion.turbo_mode:
                status.setStyleSheet('color: #00c6ff; font-weight: bold;')
            h_layout.addWidget(label)
            h_layout.addWidget(status)
            h_layout.addWidget(progress)
            widget.setLayout(h_layout)
            item.setSizeHint(widget.sizeHint())
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, widget)
def get_squad_icon(squad):
    icons = {
        'Development': '🎨',
        'AI': '🧠',
        'QA': '✅',
        'Marketing': '📢',
        'Voice': '🔊',
        'Legal': '⚖️',
        'Content': '📝',
        'Partnership': '🤝',
        'Infrastructure': '🛠️',
        'Talent': '🎭'
    }
    return icons.get(squad, '🤖')

    def update_minions(self):
        for minion in self.minions:
            minion.update_progress()
        self.refresh()

    def activate_turbo(self):
        for minion in self.minions:
            minion.turbo_mode = True
        self.refresh()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dashboard = MinionDashboard()
    dashboard.show()
    sys.exit(app.exec_())
