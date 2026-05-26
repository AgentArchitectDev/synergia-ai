# =========================================================
# AI ORCHESTRATOR - SYNERGIA CORE NEXT PRO
# =========================================================

print("[AI ORCHESTRATOR LOADED]")


class AIOrchestrator:

    # =====================================================
    # MODEL ROUTING INTELLIGENT
    # =====================================================

    def __init__(self):

        # MODO ESTABLE (IMPORTANTE PARA QUE NO SE CUELGUE)
        self.routing = {

            # 🚀 WEB GENERATION (rápido)
            "website": "llama3.2:3b",

            # 🎨 BRANDING (creativo)
            "branding": "gemma3:4b",

            # 📱 SOCIAL (rápido + estable)
            "social": "llama3.2:3b",

            # 📄 DOCS (redacción larga)
            "docs": "mistral:latest"
        }

    # =====================================================
    # SELECT MODEL
    # =====================================================

    def select_model(self, task_type):

        model = self.routing.get(

            task_type,

            "llama3.2:3b"
        )

        print(

            f"\n[ROUTER] task={task_type} → model={model}"
        )

        return model

    # =====================================================
    # FUTURO: SCORE SYSTEM (preparado)
    # =====================================================

    def score_model(self, model, score=1):

        # Placeholder para futuro ranking real
        return {
            "model": model,
            "score": score
        }


# =========================================================
# SINGLETON GLOBAL
# =========================================================

ai_orchestrator = AIOrchestrator()
