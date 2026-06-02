import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import FINAL_DIR, BASE_DIR


def main():
    input_path = FINAL_DIR / "group_L_summary.csv"
    report_path = BASE_DIR / "reports" / "group_L_report.md"

    report_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"No existe el archivo: {input_path}")
        return

    df = pd.read_csv(input_path, sep=";")

    best_team = df.sort_values("Power Score", ascending=False).iloc[0]
    best_attack = df.sort_values("Goals_For", ascending=False).iloc[0]
    best_defense = df.sort_values("Goals_Against", ascending=True).iloc[0]
    best_form = df.sort_values("Points_Form", ascending=False).iloc[0]

    report = f"""# FIFA World Cup 2026 - Group J Analysis

## Project Overview

This project analyzes the recent form of the national teams in Group J of the FIFA World Cup 2026.

The analysis is based on each team's most recent available matches, using data collected from local FBref HTML files.

Teams analyzed:

{", ".join(df["team"].tolist())}

---

## Key Findings

- Highest Power Score: {best_team["team"]} with {best_team["Power Score"]}.
- Best attacking record: {best_attack["team"]} with {best_attack["Goals_For"]} goals scored.
- Best defensive record: {best_defense["team"]} with {best_defense["Goals_Against"]} goals conceded.
- Best recent form: {best_form["team"]} with {best_form["Points_Form"]} points.

---

## Team Summary

| Team | Matches | Wins | Draws | Losses | GF | GA | GD | Points Form | Form Index | Power Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
"""

    for _, row in df.iterrows():
        report += (
            f"| {row['team']} "
            f"| {row['Matches']} "
            f"| {row['Wins']} "
            f"| {row['Draws']} "
            f"| {row['Losses']} "
            f"| {row['Goals_For']} "
            f"| {row['Goals_Against']} "
            f"| {row['Goal_Difference']} "
            f"| {row['Points_Form']} "
            f"| {row['Form Index']} "
            f"| {row['Power Score']} |\n"
        )

    report += """

---

## Visualizations

The project generates the following visualizations:

- ranking_form.png
- goal_difference.png
- attack_vs_defense.png

These charts are saved in:

reports/figures/

---

## Notes

New Zealand has 9 matches available in the collected dataset, while the other teams have 10. This should be considered when comparing form and performance indicators.

---

## Methodology

1. Local HTML files are collected from FBref.
2. Match data is extracted and cleaned with Python.
3. Team-level metrics are calculated.
4. Visualizations are generated with Matplotlib.
5. A Markdown report is created automatically.
"""

    report_path.write_text(report, encoding="utf-8")

    print(f"Reporte guardado en: {report_path}")


if __name__ == "__main__":
    main()