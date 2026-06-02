from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]

input_file = BASE_DIR / "data" / "final" / "group_L_summary.csv"
output_file = BASE_DIR / "data" / "final" / "group_L_tableau.csv"

df = pd.read_csv(input_file, sep=None, engine="python")
df.columns = df.columns.str.strip()

print("Columnas detectadas:")
print(df.columns.tolist())

df = df.rename(columns={
    "team": "Team",
    "Goals For": "Goals_For",
    "Goals Against": "Goals_Against",
    "Goal Difference": "Goal_Difference",
    "Points_Form": "Points",
    "Goals For per Game": "Goals_For_Per_Game",
    "Goals Against per Game": "Goals_Against_Per_Game",
    "Win Rate": "Win_Rate",
    "Form Index": "Form_Index",
    "Defense Index": "Defense_Index",
    "Power Score": "Power_Score"
})

columns_order = [
    "Team",
    "Matches",
    "Wins",
    "Draws",
    "Losses",
    "Goals_For",
    "Goals_Against",
    "Goal_Difference",
    "Points",
    "Goals_For_Per_Game",
    "Goals_Against_Per_Game",
    "Win_Rate",
    "Form_Index",
    "Defense_Index",
    "Power_Score"
]

df = df[columns_order]

df.to_csv(
    output_file,
    index=False,
    sep=";",
    encoding="utf-8-sig"
)

print(f"Archivo Tableau guardado en: {output_file}")