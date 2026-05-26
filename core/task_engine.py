from ai.core.progress_manager import (
    progress_manager
)


# =========================================================
# TASK ENGINE
# =========================================================

class TaskEngine:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.tasks = []

    # =====================================================
    # ADD TASK
    # =====================================================

    def add_task(

        self,

        name,

        func
    ):

        self.tasks.append(

            {

                "name": name,

                "func": func
            }
        )

    # =====================================================
    # RUN TASKS
    # =====================================================

    def run(self):

        total = len(self.tasks)

        for i, task in enumerate(self.tasks):

            percent = int(

                ((i + 1) / total) * 100
            )

            progress_manager.update(

                percent,

                f"RUNNING: {task['name']}"
            )

            task["func"]()

        progress_manager.update(

            100,

            "ALL TASKS COMPLETED"
        )


# =========================================================
# GLOBAL INSTANCE
# =========================================================

task_engine = TaskEngine()
