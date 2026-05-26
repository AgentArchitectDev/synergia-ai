from ai.providers.registry import MODELS
from ai.providers.ollama_provider import generate

import json
import re


class AIOrchestrator:

    # =========================================
    # HERO SIMPLE
    # =========================================

    def generate_hero(
        self,
        business
    ):

        prompt = f"""

        Crear hero premium para:

        {business}

        devolver:
        title
        subtitle
        button

        """

        response = generate(

            model=MODELS["copy"],

            prompt=prompt
        )

        return response

    # =========================================
    # HTML COMPLETO
    # =========================================

    def generate_html(
        self,
        description
    ):

        prompt = f"""

        Crear HTML premium moderno.

        descripción:

        {description}

        requisitos:

        - diseño moderno
        - responsive
        - dark mode
        - sección hero
        - cards
        - footer
        - html completo
        - css incluido
        - visual premium

        """

        response = generate(

            model=MODELS["frontend"],

            prompt=prompt
        )

        return response

    # =========================================
    # GENERAR PAGE JSON
    # =========================================

    def generate_page(
        self,
        business
    ):

        prompt = f"""

        Crear JSON de página web para:

        {business}

        devolver SOLO JSON válido.

        estructura:

        {{
          "blocks":[
            {{
              "type":"navbar",
              "data":{{
                "logo":"SYNERGIA"
              }}
            }},
            {{
              "type":"hero",
              "data":{{
                "title":"...",
                "subtitle":"...",
                "button":"..."
              }}
            }},
            {{
              "type":"cards",
              "data":{{
                "title":"..."
              }}
            }},
            {{
              "type":"footer",
              "data":{{
                "copyright":"..."
              }}
            }}
          ]
        }}

        """

        response = generate(

            model=MODELS["frontend"],

            prompt=prompt
        )

        return response

    # =========================================
    # GENERAR Y LIMPIAR JSON
    # =========================================

    def generate_clean_json(
        self,
        business
    ):

        raw = self.generate_page(
            business
        )

        try:

            match = re.search(
                r"\{.*\}",
                raw,
                re.DOTALL
            )

            if match:

                clean = match.group(0)

                parsed = json.loads(clean)

                return parsed

            return {
                "status": "error",
                "detail": "No se encontró JSON"
            }

        except Exception as e:

            return {
                "status": "error",
                "detail": str(e),
                "raw": raw
            }

    # =========================================
    # GENERAR MULTI PAGE SITE
    # =========================================

    def generate_site_structure(
        self,
        business
    ):

        prompt = f"""

        Crear estructura JSON para sitio web completo.

        negocio:

        {business}

        devolver SOLO JSON válido.

        estructura:

        {{
          "site_name":"...",
          "pages":[
            {{
              "slug":"home",
              "title":"Inicio"
            }},
            {{
              "slug":"about",
              "title":"Nosotros"
            }},
            {{
              "slug":"services",
              "title":"Servicios"
            }},
            {{
              "slug":"contact",
              "title":"Contacto"
            }}
          ]
        }}

        """

        response = generate(

            model=MODELS["copy"],

            prompt=prompt
        )

        return response

    # =========================================
    # GENERAR SEO
    # =========================================

    def generate_seo(
        self,
        business
    ):

        prompt = f"""

        Crear SEO profesional para:

        {business}

        devolver:

        - meta title
        - meta description
        - keywords

        """

        response = generate(

            model=MODELS["seo"],

            prompt=prompt
        )

        return response

    # =========================================
    # GENERAR TEXTOS DE CARDS
    # =========================================

    def generate_services(
        self,
        business
    ):

        prompt = f"""

        Crear 3 servicios premium para:

        {business}

        devolver:
        - titulo
        - descripción corta

        """

        response = generate(

            model=MODELS["copy"],

            prompt=prompt
        )

        return response

    # =========================================
    # GENERAR CTA
    # =========================================

    def generate_cta(
        self,
        business
    ):

        prompt = f"""

        Crear CTA premium para:

        {business}

        devolver:
        - titulo
        - subtitulo
        - botón

        """

        response = generate(

            model=MODELS["copy"],

            prompt=prompt
        )

        return response

    # =========================================
    # GENERAR ESTILO VISUAL
    # =========================================

    def generate_style(
        self,
        business
    ):

        prompt = f"""

        Crear estilo visual para:

        {business}

        devolver:
        - colores
        - tipografía
        - estilo visual
        - tipo de diseño

        """

        response = generate(

            model=MODELS["ux"],

            prompt=prompt
        )

        return response


# =============================================
# INSTANCIA GLOBAL
# =============================================

ai = AIOrchestrator()
