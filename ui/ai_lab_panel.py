# =========================================================
# FILE:
# ai/ui/ai_lab_panel.py
# =========================================================

import threading

from PyQt6.QtWidgets import (

    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QComboBox,
    QLabel,
    QCheckBox
)

from PyQt6.QtCore import (

    QThread,
    pyqtSignal
)

from ai.models.models_manager import (
    ModelsManager
)

from ai.providers.ollama_connector import (
    OllamaConnector
)

from ai.providers.ollama_provider import (
    ollama_provider
)

from ai.memory.memory_manager import (
    MemoryManager
)

from ai.router.multi_model_engine import (
    multi_model_engine
)


# =========================================================
# STREAM THREAD
# =========================================================

class StreamWorker(QThread):

    token_signal = pyqtSignal(str)

    finished_signal = pyqtSignal()

    # =====================================================
    # INIT
    # =====================================================

    def __init__(

        self,

        model,

        messages
    ):

        super().__init__()

        self.model = model

        self.messages = messages

        self.connector = OllamaConnector()

    # =====================================================
    # RUN
    # =====================================================

    def run(self):

        def callback(token):

            self.token_signal.emit(token)

        self.connector.chat_stream(

            self.model,

            self.messages,

            callback
        )

        self.finished_signal.emit()


# =========================================================
# MAIN PANEL
# =========================================================

class AILabPanel(QWidget):

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        super().__init__()

        self.setWindowTitle(

            "SYNERGIA CORE NEXT PRO"
        )

        self.resize(1400, 900)

        # =================================================
        # CORE SYSTEMS
        # =================================================

        self.models_manager = ModelsManager()

        self.memory = MemoryManager()

        # =================================================
        # INIT UI
        # =================================================

        self.init_ui()

        self.load_models()

    # =====================================================
    # UI
    # =====================================================

    def init_ui(self):

        layout = QVBoxLayout()

        # =================================================
        # TITLE
        # =================================================

        self.title_label = QLabel(

            "SYNERGIA AI LAB v2"
        )

        layout.addWidget(

            self.title_label
        )

        # =================================================
        # MODEL LABEL
        # =================================================

        self.model_label = QLabel(

            "MODEL SELECTED:"
        )

        layout.addWidget(

            self.model_label
        )

        # =================================================
        # MODEL SELECTOR
        # =================================================

        self.model_selector = QComboBox()

        layout.addWidget(

            self.model_selector
        )

        # =================================================
        # MULTI MODEL
        # =================================================

        self.multi_model_checkbox = QCheckBox(

            "MULTI MODEL MODE"
        )

        layout.addWidget(

            self.multi_model_checkbox
        )

        # =================================================
        # HEAVY MODE
        # =================================================

        self.heavy_mode_checkbox = QCheckBox(

            "HEAVY MODELS"
        )

        layout.addWidget(

            self.heavy_mode_checkbox
        )

        # =================================================
        # PROMPT INPUT
        # =================================================

        self.input_box = QTextEdit()

        self.input_box.setPlaceholderText(

            "Escribí un prompt..."
        )

        layout.addWidget(

            self.input_box
        )

        # =================================================
        # RUN BUTTON
        # =================================================

        self.run_button = QPushButton(

            "RUN AI"
        )

        self.run_button.clicked.connect(

            self.run_prompt
        )

        layout.addWidget(

            self.run_button
        )

        # =================================================
        # OUTPUT
        # =================================================

        self.output_box = QTextEdit()

        self.output_box.setReadOnly(True)

        layout.addWidget(

            self.output_box
        )

        # =================================================
        # STATUS
        # =================================================

        self.status_label = QLabel(

            "STATUS: READY"
        )

        layout.addWidget(

            self.status_label
        )

        # =================================================
        # FINAL LAYOUT
        # =================================================

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

        if not prompt.strip():

            self.output_box.setPlainText(

                "ERROR: EMPTY PROMPT"
            )

            return

        # =================================================
        # CLEAR OUTPUT
        # =================================================

        self.output_box.clear()

        self.status_label.setText(

            "STATUS: RUNNING"
        )

        # =================================================
        # SAVE MEMORY
        # =================================================

        self.memory.save_prompt(prompt)

        # =================================================
        # MULTI MODEL MODE
        # =================================================

        if self.multi_model_checkbox.isChecked():

            threading.Thread(

                target=self.run_multi_model,

                args=(prompt,),

                daemon=True

            ).start()

        # =================================================
        # SINGLE MODEL MODE
        # =================================================

        else:

            model = self.model_selector.currentText()

            messages = [

                {
                    "role": "user",
                    "content": prompt
                }
            ]

            self.worker = StreamWorker(

                model,

                messages
            )

            self.worker.token_signal.connect(

                self.update_output
            )

            self.worker.finished_signal.connect(

                self.finished_response
            )

            self.worker.start()

    # =====================================================
    # MULTI MODEL THREAD
    # =====================================================

    def run_multi_model(self, prompt):

        results = multi_model_engine.run_all(

            prompt,

            heavy_mode=self.heavy_mode_checkbox.isChecked()
        )

        for item in results:

            block = (

                "\n"
                + "=" * 80
                + "\n\n"

                + f"MODEL: {item['model']}\n\n"

                + item["response"]

                + "\n\n"
            )

            self.output_box.append(block)

        self.status_label.setText(

            "STATUS: FINISHED"
        )

    # =====================================================
    # UPDATE STREAM
    # =====================================================

    def update_output(self, token):

        self.output_box.insertPlainText(token)

    # =====================================================
    # FINISHED
    # =====================================================

    def finished_response(self):

        self.status_label.setText(

            "STATUS: FINISHED"
        )
