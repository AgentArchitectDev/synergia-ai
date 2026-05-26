import requests


class ModelsManager:
    """
    Detecta modelos disponibles en Ollama local
    """

    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    # =====================================================
    # FETCH MODELS
    # =====================================================
    def get_models(self):
        try:
            url = f"{self.base_url}/api/tags"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            models = []
            for m in data.get("models", []):
                models.append({
                    "name": m.get("name"),
                    "size": m.get("size"),
                    "modified": m.get("modified_at")
                })

            return models

        except Exception as e:
            print(f"[ModelsManager] Error: {e}")
            return []

    # =====================================================
    # SIMPLE LIST (UI FRIENDLY)
    # =====================================================
    def get_model_names(self):
        return [m["name"] for m in self.get_models()]
