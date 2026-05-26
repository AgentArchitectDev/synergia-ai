from pathlib import Path
from datetime import datetime

from ai.core.task_engine import (
    task_engine
)

from ai.core.ai_orchestrator import (
    ai_orchestrator
)

from ai.business.project_builder import (
    create_project_structure
)

from ai.business.website_generator import (
    generate_website
)

from ai.business.branding_generator import (
    generate_branding
)

from ai.business.social_generator import (
    generate_social
)

from ai.business.docs_generator import (
    generate_docs
)


# =========================================================
# BUSINESS GENERATOR
# =========================================================

print(

    "[BUSINESS GENERATOR LOADED]"
)


# =========================================================
# CREATE PROJECT
# =========================================================

def create_business_project(

    prompt
):

    # =====================================================
    # TIMESTAMP
    # =====================================================

    timestamp = datetime.now().strftime(

        "%Y%m%d_%H%M%S"
    )

    # =====================================================
    # PROJECT NAME
    # =====================================================

    project_name = (

        prompt.lower()

        .replace(" ", "_")

        [:30]
    )

    # =====================================================
    # CREATE STRUCTURE
    # =====================================================

    project_path = create_project_structure(

        f"{project_name}_{timestamp}"
    )

    print(

        f"\n[PROJECT CREATED]\n{project_path}"
    )

    # =====================================================
    # WEBSITE TASK
    # =====================================================

    def website_task():

        model = ai_orchestrator.select_model(

            "website"
        )

        print(

            f"\n[WEBSITE MODEL] {model}"
        )

        generate_website(

            prompt,

            project_path,

            model
        )

    # =====================================================
    # BRANDING TASK
    # =====================================================

    def branding_task():

        model = ai_orchestrator.select_model(

            "branding"
        )

        print(

            f"\n[BRANDING MODEL] {model}"
        )

        generate_branding(

            prompt,

            project_path,

            model
        )

    # =====================================================
    # SOCIAL TASK
    # =====================================================

    def social_task():

        model = ai_orchestrator.select_model(

            "social"
        )

        print(

            f"\n[SOCIAL MODEL] {model}"
        )

        generate_social(

            prompt,

            project_path,

            model
        )

    # =====================================================
    # DOCS TASK
    # =====================================================

    def docs_task():

        model = ai_orchestrator.select_model(

            "docs"
        )

        print(

            f"\n[DOCS MODEL] {model}"
        )

        generate_docs(

            prompt,

            project_path,

            model
        )

    # =====================================================
    # ADD TASKS
    # =====================================================

    task_engine.tasks = []

    task_engine.add_task(

        "WEBSITE",

        website_task
    )

    task_engine.add_task(

        "BRANDING",

        branding_task
    )

    task_engine.add_task(

        "SOCIAL",

        social_task
    )

    task_engine.add_task(

        "DOCS",

        docs_task
    )

    # =====================================================
    # RUN TASKS
    # =====================================================

    task_engine.run()

    # =====================================================
    # FINISHED
    # =====================================================

    print(

        "\n[BUSINESS PROJECT FINISHED]"
    )

    print(

        f"\nOUTPUT PATH:\n{project_path}"
    )

    return project_path
