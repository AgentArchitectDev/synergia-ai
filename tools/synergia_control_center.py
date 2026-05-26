import sys
import subprocess
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QFrame,
    QListWidget,
    QListWidgetItem,
)

from PyQt6.QtCore import Qt


PROJECT_PATH = Path(
    "/home/gerardoalbertobergoglio/Escritorio/DISCO_TRABAJO/SYNERGIA_CORE_NEXT_PRO"
)


class SynergiaControlCenter(QWidget):

    def __init__(self):
        super().__init__()

        self.current_mode = "DEV"

        self.setWindowTitle("SYNERGIA CONTROL CENTER")
        self.resize(1200, 750)

        self.init_ui()
        self.load_git_status()

    def init_ui(self):

        main_layout = QVBoxLayout()

        # HEADER
        header = QLabel("SYNERGIA CORE NEXT PRO")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 15px;
        """)

        main_layout.addWidget(header)

        # STATUS PANEL
        status_frame = QFrame()
        status_frame.setFrameShape(QFrame.Shape.StyledPanel)

        status_layout = QVBoxLayout()

        self.machine_label = QLabel("🖥️ MACHINE: MAQ2")
        self.project_label = QLabel(f"📂 PROJECT: {PROJECT_PATH}")
        self.mode_label = QLabel("⚙️ MODE: DEV")
        self.github_label = QLabel("🌐 GITHUB: CONNECTED")

        labels = [
            self.machine_label,
            self.project_label,
            self.mode_label,
            self.github_label,
        ]

        for label in labels:
            label.setStyleSheet("""
                font-size: 15px;
                padding: 4px;
            """)
            status_layout.addWidget(label)

        status_frame.setLayout(status_layout)

        main_layout.addWidget(status_frame)

        # MAIN CONTENT
        content_layout = QHBoxLayout()

        # SIDEBAR
        self.sidebar = QListWidget()
        self.sidebar.setMaximumWidth(240)

        self.sidebar.setStyleSheet("""
            font-size: 15px;
            padding: 8px;
        """)

        sections = [
            "🏠 Dashboard",
            "🧠 AI LAB",
            "🤖 AGENTS",
            "📊 GRAPH SYSTEM",
            "📂 PROJECTS",
            "💾 STORAGE",
            "🌐 SOCIAL ENGINE",
            "⚙ SETTINGS",
        ]

        for section in sections:
            QListWidgetItem(section, self.sidebar)

        content_layout.addWidget(self.sidebar)

        # RIGHT SIDE
        right_layout = QVBoxLayout()

        # BUTTONS
        buttons_layout = QHBoxLayout()

        self.pull_btn = QPushButton("⬇️ Pull")
        self.push_btn = QPushButton("⬆️ Push")
        self.obsidian_btn = QPushButton("🧠 Obsidian")
        self.code_btn = QPushButton("💻 VSCode")
        self.git_status_btn = QPushButton("📊 Git Status")
        self.dev_btn = QPushButton("🧪 DEV MODE")
        self.prod_btn = QPushButton("🚀 PROD MODE")
        self.clear_btn = QPushButton("🧹 CLEAR LOG")

        button_list = [
            self.pull_btn,
            self.push_btn,
            self.obsidian_btn,
            self.code_btn,
            self.git_status_btn,
            self.dev_btn,
            self.prod_btn,
            self.clear_btn,
        ]

        for btn in button_list:
            btn.setMinimumHeight(45)

            btn.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
            """)

            buttons_layout.addWidget(btn)

        right_layout.addLayout(buttons_layout)

        # TERMINAL OUTPUT
        self.output = QTextEdit()

        self.output.setReadOnly(True)

        self.output.setStyleSheet("""
            background-color: black;
            color: #00ff88;
            font-family: monospace;
            font-size: 13px;
        """)

        right_layout.addWidget(self.output)

        content_layout.addLayout(right_layout)

        main_layout.addLayout(content_layout)

        # SIGNALS
        self.pull_btn.clicked.connect(self.git_pull)
        self.push_btn.clicked.connect(self.git_push)
        self.obsidian_btn.clicked.connect(self.open_obsidian)
        self.code_btn.clicked.connect(self.open_vscode)
        self.git_status_btn.clicked.connect(self.load_git_status)

        self.dev_btn.clicked.connect(self.set_dev_mode)
        self.prod_btn.clicked.connect(self.set_prod_mode)

        self.clear_btn.clicked.connect(self.clear_console)

        self.sidebar.currentRowChanged.connect(self.change_module)

        self.setLayout(main_layout)

    # =========================
    # CONSOLE
    # =========================

    def clear_console(self):

        self.output.clear()

        self.output.append(
            "==============================\n"
            "SYNERGIA LOG SYSTEM RESET\n"
            "==============================\n"
        )

    def system_log(self, category, message):

        self.output.append(f"[{category}] {message}\n")

    # =========================
    # COMMAND RUNNER
    # =========================

    def run_command(self, command):

        try:

            result = subprocess.run(
                command,
                cwd=PROJECT_PATH,
                shell=True,
                capture_output=True,
                text=True,
            )

            output = result.stdout + "\n" + result.stderr

            self.output.append(f"$ {command}\n")
            self.output.append(output)
            self.output.append("\n")

        except Exception as e:

            self.output.append(f"ERROR: {e}\n")

    # =========================
    # GIT
    # =========================

    def load_git_status(self):

        self.run_command("git status")

    def git_pull(self):

        self.run_command("git pull origin main")

    def git_push(self):

        message = "SYNERGIA update"

        commands = [
            "git add .",
            f'git commit -m "{message}"',
            "git push origin main",
        ]

        for cmd in commands:
            self.run_command(cmd)

    # =========================
    # APPS
    # =========================

    def open_obsidian(self):

        try:

            subprocess.Popen([
                "obsidian",
                str(PROJECT_PATH / "docs")
            ])

            self.system_log("SYSTEM", "Obsidian abierto")

        except Exception as e:

            QMessageBox.critical(self, "Error", str(e))

    def open_vscode(self):

        try:

            subprocess.Popen([
                "code",
                str(PROJECT_PATH)
            ])

            self.system_log("SYSTEM", "VSCode abierto")

        except Exception as e:

            QMessageBox.critical(self, "Error", str(e))

    # =========================
    # MODES
    # =========================

    def set_dev_mode(self):

        self.current_mode = "DEV"

        self.mode_label.setText("⚙️ MODE: DEV")

        self.system_log("DEV", "DEV MODE ACTIVADO")

    def set_prod_mode(self):

        self.current_mode = "PROD"

        self.mode_label.setText("⚙️ MODE: PROD")

        self.system_log("PROD", "PROD MODE ACTIVADO")

    # =========================
    # MODULES
    # =========================

    def change_module(self, index):

        modules = {
            0: "🏠 DASHBOARD GENERAL",
            1: "🧠 AI LAB PANEL",
            2: "🤖 AGENT ENGINE PANEL",
            3: "📊 GRAPH SYSTEM PANEL",
            4: "📂 PROJECTS PANEL",
            5: "💾 STORAGE PANEL",
            6: "🌐 SOCIAL ENGINE PANEL",
            7: "⚙ SETTINGS PANEL",
        }

        module_name = modules.get(index, "UNKNOWN")

        self.output.append(
            "\n==============================\n"
            f"MODULE ACTIVE: {module_name}\n"
            f"MODE: {self.current_mode}\n"
            "==============================\n"
        )

        self.system_log("MODULE", f"{module_name} cargado")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = SynergiaControlCenter()

    window.show()

    sys.exit(app.exec())
