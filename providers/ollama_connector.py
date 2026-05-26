import requests
import json


class OllamaConnector:
    """
    Conector directo a Ollama con streaming real
    SYNERGIA CORE NEXT PRO
    """

    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    # =====================================================
    # STREAM CHAT
    # =====================================================
    def chat_stream(self, model, messages, callback):
        """
        callback(token: str)
        """

        url = f"{self.base_url}/api/chat"

        payload = {
            "model": model,
            "messages": messages,
            "stream": True
        }

        try:
            response = requests.post(url, json=payload, stream=True)
            response.raise_for_status()

            for line in response.iter_lines():
                if not line:
                    continue

                try:
                    data = json.loads(line.decode("utf-8"))

                    if "message" in data:
                        token = data["message"].get("content", "")
                        if token:
                            callback(token)

                except Exception:
                    continue

        except Exception as e:
            callback(f"\n[ERROR OLLAMA]: {str(e)}")
