import os
import json
from datetime import datetime


class MemoryManager:
    """
    SYNERGIA MEMORY ENGINE (PRO)
    - Manejo de sesiones
    - Persistencia de prompts
    - Contexto de conversación
    """

    def __init__(self):
        self.base_path = "ai/memory"
        self.conversations_path = os.path.join(self.base_path, "conversations")
        self.sessions_path = os.path.join(self.base_path, "sessions")
        self.prompts_path = os.path.join(self.base_path, "prompts")

        self._ensure_dirs()
        self.current_session = self._create_session()

    # =====================================================
    # INIT STRUCTURE
    # =====================================================
    def _ensure_dirs(self):
        os.makedirs(self.conversations_path, exist_ok=True)
        os.makedirs(self.sessions_path, exist_ok=True)
        os.makedirs(self.prompts_path, exist_ok=True)

    def _create_session(self):
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_file = os.path.join(self.sessions_path, f"{session_id}.json")

        data = {
            "session_id": session_id,
            "created_at": datetime.now().isoformat(),
            "history": []
        }

        with open(session_file, "w") as f:
            json.dump(data, f, indent=2)

        return session_file

    # =====================================================
    # SAVE PROMPT (OBLIGATORIO)
    # =====================================================
    def save_prompt(self, prompt, response=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response
        }

        self._save_to_session(entry)
        self._save_global(entry)

    # =====================================================
    # SESSION STORAGE
    # =====================================================
    def _save_to_session(self, entry):
        with open(self.current_session, "r") as f:
            data = json.load(f)

        data["history"].append(entry)

        with open(self.current_session, "w") as f:
            json.dump(data, f, indent=2)

    # =====================================================
    # GLOBAL STORAGE
    # =====================================================
    def _save_global(self, entry):
        global_file = os.path.join(self.conversations_path, "global.json")

        if not os.path.exists(global_file):
            with open(global_file, "w") as f:
                json.dump([], f)

        with open(global_file, "r") as f:
            data = json.load(f)

        data.append(entry)

        with open(global_file, "w") as f:
            json.dump(data, f, indent=2)

    # =====================================================
    # CONTEXT (FUTURO AGENTES)
    # =====================================================
    def get_context(self, limit=10):
        with open(self.current_session, "r") as f:
            data = json.load(f)

        return data["history"][-limit:]
