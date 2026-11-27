"""Price RMSE: a file challenge.

Participants upload one `submission.csv` (house_id, price). The platform calls
`Env().evaluate(path_to_that_file)` and reads the score from the returned dict.
The metric is RMSE, lower is better (`metrics` in challenge.toml).
"""
import csv
import math
import os


def _agent_error(message):
    """A submission in the wrong shape is the participant's to fix: answer with
    an agent error. An exception raised here would be blamed on the challenge."""
    return {
        "agent_results": [{
            "agent_index": 0,
            "is_agent_code_error": True,
            "agent_code_error_message": message,
        }]
    }


class Env:
    def __init__(self):
        y_test_path = os.path.join(os.path.dirname(__file__), "y_test.csv")
        with open(y_test_path, "r") as f:
            self.ground_truth = {
                row["house_id"]: float(row["price"]) for row in csv.DictReader(f)
            }

    def evaluate(self, submission_path):
        """Score a submission CSV against the ground truth."""
        with open(submission_path, "r") as f:
            reader = csv.DictReader(f)
            columns = reader.fieldnames or []
            if "house_id" not in columns or "price" not in columns:
                return _agent_error(
                    "submission.csv must have 'house_id' and 'price' columns "
                    f"(found: {columns})"
                )
            predictions = {row["house_id"]: row["price"] for row in reader}

        squared = []
        for house_id, truth in self.ground_truth.items():
            try:
                predicted = float(predictions[house_id])
            except (KeyError, ValueError):
                # No score: a failed submission must not look like RMSE 0.
                return _agent_error(
                    f"Missing or non-numeric price for house_id '{house_id}'"
                )
            squared.append((predicted - truth) ** 2)

        rmse = math.sqrt(sum(squared) / len(squared))
        return {
            "agent_results": [{
                "agent_index": 0,
                "score": round(rmse, 6),
                "steps": len(squared),
                "info_message": f"RMSE: {rmse:.4f}",
            }]
        }
