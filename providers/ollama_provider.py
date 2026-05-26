import ollama
import time


# =========================================================
# OLLAMA PROVIDER
# =========================================================

print("[OLLAMA PROVIDER LOADED]")


class OllamaProvider:

    # =====================================================
    # GENERATE (ROBUSTO + DEBUG + FALLBACK)
    # =====================================================

    def generate(self, prompt, model="llama3.2:3b"):

        try:
            print("\n[OLLAMA CALL]")
            print(f"MODEL: {model}")

            start_time = time.time()

            # =================================================
            # CALL OLLAMA
            # =================================================

            response = ollama.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            end_time = time.time()

            duration = round(end_time - start_time, 2)

            print(f"[OLLAMA OK] time={duration}s")

            # =================================================
            # EXTRACT RESPONSE
            # =================================================

            content = response.get("message", {}).get("content", "")

            if not content:

                return "[OLLAMA ERROR] empty response"

            return content

        except Exception as e:

            print("\n[OLLAMA ERROR]")
            print(str(e))

            return f"[OLLAMA FAIL] {str(e)}"

    # =====================================================
    # SIMPLE GENERATE (compatibilidad futura)
    # =====================================================

    def simple(self, prompt):

        return self.generate(prompt)
