from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# WEBSITE GENERATOR
# =========================================================

print(

    "[WEBSITE GENERATOR LOADED]"
)


# =========================================================
# GENERATE WEBSITE
# =========================================================

def generate_website(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear estructura web profesional para:

    {prompt}

    Generar:

    - Landing page
    - Secciones
    - SEO
    - CTA
    - Diseño moderno
    - Estrategia web

    """

    # =====================================================
    # GENERATE
    # =====================================================

    response = provider.generate(

        prompt=ai_prompt,

        model=model
    )

    # =====================================================
    # SAVE
    # =====================================================

    output_file = (

        Path(project_path)

        / "website"

        / "website.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[WEBSITE GENERATED]\n{output_file}"
    )
