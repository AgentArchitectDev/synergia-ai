import sys
import json
from datetime import datetime

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QComboBox, QLabel
)
from PyQt6.QtCore import QThread, pyqtSignal

from ai.models.models_manager import ModelsManager
from ai.providers.ollama_connector import OllamaConnector
from ai.memory.memory_manager import MemoryManager


# =========================================================
# STREAM WORKER
# =========================================================
class StreamWorker(QThread):
    token_signal = pyqtSignal(str)

    def __init__(self, model, messages):
        super().__init__()
        self.model = model
        self.messages = messages
        self.connector = OllamaConnector()

    def run(self):
        def callback(token):
            self.token_signal.emit(token)

        self.connector.chat_stream(
            self.model,
            self.messages,
            callback
        )


# =========================================================
# MAIN PANEL
# =========================================================
class AILabPanel(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SYNERGIA AI LAB")
        self.resize(900, 650)

        self.models_manager = ModelsManager()
        self.memory = MemoryManager()

        self.init_ui()
        self.load_models()

    # =====================================================
    # UI
    # =====================================================
    def init_ui(self):
        layout = QVBoxLayout()

        # -------------------------
        # MODEL SELECTOR
        # -------------------------
        self.label = QLabel("Modelo IA:")
        layout.addWidget(self.label)

        self.model_selector = QComboBox()
        layout.addWidget(self.model_selector)

        # -------------------------
        # LANGUAGE SELECTOR
        # -------------------------
        self.lang_label = QLabel("Idioma:")
        layout.addWidget(self.lang_label)

        self.lang_selector = QComboBox()
        self.lang_selector.addItems(["Español", "English"])
        layout.addWidget(self.lang_selector)

        # -------------------------
        # INPUT BOX
        # -------------------------
        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Escribí tu prompt...")
        layout.addWidget(self.input_box)

        # -------------------------
        # ACTION BUTTON
        # -------------------------
        self.run_button = QPushButton("Ejecutar IA")
        self.run_button.clicked.connect(self.run_prompt)
        layout.addWidget(self.run_button)

        # -------------------------
        # EXTRA FEATURES
        # -------------------------
        self.export_button = QPushButton("Exportar historial")
        self.export_button.clicked.connect(self.export_history)
        layout.addWidget(self.export_button)

        self.history_button = QPushButton("Ver historial")
        self.history_button.clicked.connect(self.show_history)
        layout.addWidget(self.history_button)

        self.compare_button = QPushButton("Comparar modelos")
        self.compare_button.clicked.connect(self.compare_models)
        layout.addWidget(self.compare_button)

        # -------------------------
        # OUTPUT
        # -------------------------
        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.setLayout(layout)

    # =====================================================
    # LOAD MODELS
    # =====================================================
    def load_models(self):
        models = self.models_manager.get_model_names()
        self.model_selector.addItems(models)

    # =====================================================
    # RUN PROMPT
    # =====================================================
    def run_prompt(self):
        prompt = self.input_box.toPlainText()
        model = self.model_selector.currentText()
        language = self.lang_selector.currentText()

        self.output_box.clear()

        # 🌍 LANGUAGE CONTROL
        if language == "English":
            prompt = f"""
You must respond in English.

{prompt}
"""

        messages = [
            {"role": "user", "content": prompt}
        ]

        # 🧠 MEMORY SAVE
        self.memory.save_prompt(prompt)

        self.worker = StreamWorker(model, messages)
        self.worker.token_signal.connect(self.update_output)
        self.worker.start()

    # =====================================================
    # STREAM OUTPUT
    # =====================================================
    def update_output(self, token):
        self.output_box.insertPlainText(token)

    # =====================================================
    # EXPORT HISTORY
    # =====================================================
    def export_history(self):
        data = self.memory.get_context(limit=100)

        file_json = f"ai/memory/export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_txt = file_json.replace(".json", ".txt")

        with open(file_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        with open(file_txt, "w", encoding="utf-8") as f:
            for item in data:
                f.write(f"PROMPT: {item['prompt']}\n")
                f.write(f"RESPONSE: {item.get('response','')}\n")
                f.write("\n--------------------\n")

        self.output_box.setPlainText(
            f"EXPORT OK:\n\n{file_json}\n{file_txt}"
        )

    # =====================================================
    # SHOW HISTORY
    # =====================================================
    def show_history(self):
        history = self.memory.get_context(limit=50)

        self.output_box.clear()

        for item in history:
            self.output_box.append("🧠 PROMPT:")
            self.output_box.append(item["prompt"])
            self.output_box.append("\n🤖 RESPONSE:")
            self.output_box.append(str(item.get("response", "")))
            self.output_box.append("\n----------------------\n")

    # =====================================================
    # MULTI MODEL COMPARISON
    # =====================================================
    def compare_models(self):
        prompt = self.input_box.toPlainText()

        models = [
            self.model_selector.currentText(),
            "mistral:latest",
            "phi3:mini"
        ]

        self.output_box.clear()

        for model in models:
            self.output_box.append(f"\n\n===== {model} =====\n")

            messages = [
                {"role": "user", "content": prompt}
            ]

            connector = OllamaConnector()

            def callback(token):
                self.output_box.insertPlainText(token)

            connector.chat_stream(model, messages, callback)
