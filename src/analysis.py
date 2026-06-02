import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import PROCESSED_DIR, FINAL_DIR


def main():
    FINAL_DIR.mkdir(parents=True, exist_ok=True)

    input_path = PROCESSED_DIR / "group_L_last_10_clean.csv"

    if not input_path.exists():
        print(f"No existe el archivo: {input_path}")
        return

    df = pd.read_csv(input_path)

    summary = df.groupby("team").agg(
        Matches=("team", "count"),
        Wins=("result_clean", lambda x: (x == "Win").sum()),
        Draws=("result_clean", lambda x: (x == "Draw").sum()),
        Losses=("result_clean", lambda x: (x == "Loss").sum()),
        Goals_For=("gf", "sum"),
        Goals_Against=("ga", "sum"),
        Goal_Difference=("goal_difference", "sum"),
        Avg_Goals_For=("gf", "mean"),
        Avg_Goals_Against=("ga", "mean"),
        Points_Form=("points", "sum"),
    ).reset_index()

    summary["Goals For per Game"] = (
        summary["Goals_For"] / summary["Matches"]
    ).round(2)

    summary["Goals Against per Game"] = (
        summary["Goals_Against"] / summary["Matches"]
    ).round(2)

    summary["Win Rate"] = (
        (summary["Wins"] / summary["Matches"]) * 100
    ).round(2)

    summary["Form Index"] = (
        summary["Points_Form"] / (summary["Matches"] * 3) * 100
    ).round(2)

    summary["Defense Index"] = (
        (1 / (summary["Avg_Goals_Against"] + 0.1)) * 10
    ).round(2)

    summary["Power Score"] = (
        summary["Points_Form"] * 0.4
        + summary["Goal_Difference"] * 0.3
        + summary["Goals_For"] * 0.2
        + summary["Defense Index"] * 0.1
    ).round(2)

    summary["Avg_Goals_For"] = summary["Avg_Goals_For"].round(2)
    summary["Avg_Goals_Against"] = summary["Avg_Goals_Against"].round(2)

    summary = summary.sort_values(
        by=["Power Score", "Points_Form"],
        ascending=False
    )

    output_path = FINAL_DIR / "group_L_summary.csv"

    summary.to_csv(
        output_path,
        index=False,
        sep=";",
        encoding="utf-8"
    )

    print(f"Resumen guardado en: {output_path}")
    print(summary)


if __name__ == "__main__":
    main()