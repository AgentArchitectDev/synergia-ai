# =========================================================
# PROGRESS MANAGER
# =========================================================

class ProgressManager:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        self.progress = 0
        self.status = "IDLE"

    # =====================================================
    # UPDATE
    # =====================================================

    def update(

        self,

        percent,

        status
    ):

        self.progress = percent
        self.status = status

        print(

            f"\n[{percent}%] {status}"
        )

    # =====================================================
    # GET STATUS
    # =====================================================

    def get_status(self):

        return {

            "progress": self.progress,

            "status": self.status
        }


# =========================================================
# GLOBAL INSTANCE
# =========================================================

progress_manager = ProgressManager()
