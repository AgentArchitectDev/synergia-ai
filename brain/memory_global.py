import json
import os
from datetime import datetime


class GlobalMemory:

    def __init__(self):

        self.file = "ai/brain/memory_global.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    # =====================================================
    # SAVE
    # =====================================================
    def save(

        self,

        prompt,
        response,
        model,
        agent="GENERAL"
    ):

        with open(self.file, "r") as f:
            data = json.load(f)

        entry = {

            "timestamp": datetime.now().isoformat(),

            "prompt": prompt,

            "response": response,

            "model": model,

            "agent": agent
        }

        data.append(entry)

        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)

    # =====================================================
    # GET LAST
    # =====================================================
    def get_last(self, limit=20):

        with open(self.file, "r") as f:
            data = json.load(f)

        return data[-limit:]


memory_global = GlobalMemory()
