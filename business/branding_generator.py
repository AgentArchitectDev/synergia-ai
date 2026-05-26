from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# BRANDING GENERATOR
# =========================================================

print(

    "[BRANDING GENERATOR LOADED]"
)


# =========================================================
# GENERATE BRANDING
# =========================================================

def generate_branding(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear branding profesional para:

    {prompt}

    Generar:

    - naming
    - slogans
    - identidad visual
    - colores
    - branding moderno
    - concepto de marca
    - estilo visual
    - tono comunicacional

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

        / "branding"

        / "branding.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[BRANDING GENERATED]\n{output_file}"
    )
