"""Score the benchmark submission with env.py, as the platform does. No install needed.

    python challenges/house-prices/test_local.py
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from env import Env  # noqa: E402

# Change me with your data: the range benchmark/submission.csv must score in.
# Here an RMSE between 0 and 10 (the benchmark scores about 5.4).
EXPECTED_SCORE = (0, 10)


def main():
    result = Env().evaluate(str(HERE / "benchmark" / "submission.csv"))
    row = result["agent_results"][0]
    assert not row.get("is_agent_code_error"), row
    low, high = EXPECTED_SCORE
    assert low < row["score"] < high, f"benchmark score {row['score']} outside EXPECTED_SCORE {EXPECTED_SCORE}"
    print(row["info_message"])

    # A file in the wrong shape is reported to the participant, not raised.
    bad = Env().evaluate(str(HERE / "overview.md"))
    assert bad["agent_results"][0]["is_agent_code_error"], bad
    print("wrong-shape submission:", bad["agent_results"][0]["agent_code_error_message"])


if __name__ == "__main__":
    main()
