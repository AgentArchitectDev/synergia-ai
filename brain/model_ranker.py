import json
import os


class ModelRanker:

    def __init__(self):

        self.file = "ai/brain/model_ranking.json"

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:
                json.dump({}, f)

    # =====================================================
    # UPDATE SCORE
    # =====================================================
    def update(self, model, score=1):

        with open(self.file, "r") as f:
            data = json.load(f)

        if model not in data:

            data[model] = {
                "score": 0,
                "uses": 0
            }

        data[model]["score"] += score
        data[model]["uses"] += 1

        with open(self.file, "w") as f:
            json.dump(data, f, indent=2)

    # =====================================================
    # BEST MODEL
    # =====================================================
    def best_model(self):

        with open(self.file, "r") as f:
            data = json.load(f)

        if not data:
            return None

        best = max(

            data.items(),

            key=lambda x: x[1]["score"]
        )

        return best[0]


model_ranker = ModelRanker()
