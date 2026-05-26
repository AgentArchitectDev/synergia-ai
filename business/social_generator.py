from pathlib import Path

from ai.providers.ollama_provider import (
    OllamaProvider
)


# =========================================================
# SOCIAL GENERATOR
# =========================================================

print(

    "[SOCIAL GENERATOR LOADED]"
)


# =========================================================
# GENERATE SOCIAL
# =========================================================

def generate_social(

    prompt,

    project_path,

    model
):

    provider = OllamaProvider()

    # =====================================================
    # AI PROMPT
    # =====================================================

    ai_prompt = f"""

    Crear estrategia completa de redes sociales para:

    {prompt}

    Generar:

    - Instagram
    - TikTok
    - Facebook
    - campañas
    - hashtags
    - reels
    - copies
    - calendario contenido
    - ideas virales
    - automatización social

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

        / "social"

        / "social.txt"
    )

    with open(

        output_file,

        "w",

        encoding="utf-8"
    ) as f:

        f.write(response)

    print(

        f"\n[SOCIAL GENERATED]\n{output_file}"
    )
