from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# DOCS GENERATOR
# =========================================================

print(

    "[DOCS GENERATOR LOADED]"
)


# =========================================================
# GENERATE DOCS
# =========================================================

def generate_docs(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear documentación profesional para:

    {prompt}

    Generar:

    - propuesta comercial
    - pitch
    - presupuesto
    - documentación técnica
    - roadmap
    - objetivos
    - estrategia negocio
    - presentación profesional

    """

    # =====================================================
    # GENERATE
    # =====================================================

    response = provider.generate(

        prompt=ai_prompt,

        model=model
    )

    # =====================================================
    # SAVE TXT
    # =====================================================

    output_file = (

        Path(project_path)

        / "docs"

        / "docs.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[DOCS GENERATED]\n{output_file}"
    )
