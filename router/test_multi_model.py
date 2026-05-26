from ai.router.multi_model_engine import (
    multi_model_engine
)

prompt = """

crear estrategia completa para una
pizzería premium moderna

"""

results = multi_model_engine.run_all(
    prompt
)

print("\n\n===== RESULTS =====\n")

for model, response in results.items():

    print("\n")
    print("=" * 80)

    print(f"\nMODEL: {model}\n")

    print(response)
