# =========================================================
# FILE:
# ai/router/multi_model_engine.py
# =========================================================

from ai.providers.ollama_provider import (
    ollama_provider
)


# =========================================================
# MULTI MODEL ENGINE
# =========================================================

class MultiModelEngine:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        print(

            "[MULTI MODEL ENGINE LOADED]"
        )

    # =====================================================
    # RUN ALL
    # =====================================================

    def run_all(

        self,

        prompt,

        heavy_mode=False
    ):

        # =================================================
        # LIGHT MODELS
        # =================================================

        if not heavy_mode:

            models = [

                "llama3.2:3b",

                "mistral:latest",

                "phi3:mini"
            ]

        # =================================================
        # HEAVY MODELS
        # =================================================

        else:

            models = [

                "llama3:8b",

                "gemma3:4b",

                "qwen2.5-coder:7b"
            ]

        results = []

        # =================================================
        # EXECUTION
        # =================================================

        for model in models:

            print(f"\n>>> RUNNING: {model}")

            try:

                response = ollama_provider.generate(

                    model_name=model,

                    prompt=prompt
                )

                if not response:

                    response = "[NO RESPONSE]"

            except Exception as e:

                response = (

                    f"[ERROR]: {str(e)}"
                )

            results.append({

                "model": model,

                "response": response
            })

        return results


# =========================================================
# GLOBAL INSTANCE
# =========================================================

multi_model_engine = MultiModelEngine()
