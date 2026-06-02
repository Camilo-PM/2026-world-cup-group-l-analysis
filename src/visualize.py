import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import FINAL_DIR, BASE_DIR


def main():
    figures_dir = BASE_DIR / "reports" / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)

    input_path = FINAL_DIR / "group_L_summary.csv"

    if not input_path.exists():
        print(f"No existe el archivo: {input_path}")
        return

    df = pd.read_csv(input_path, sep=";")

    df = df.sort_values("Points_Form", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["team"], df["Points_Form"])
    plt.title("Group K - Points Form")
    plt.xlabel("Points")
    plt.tight_layout()
    plt.savefig(figures_dir / "ranking_form.png")
    plt.close()

    df = df.sort_values("Goal_Difference", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["team"], df["Goal_Difference"])
    plt.title("Group K - Goal Difference")
    plt.xlabel("Goal Difference")
    plt.tight_layout()
    plt.savefig(figures_dir / "goal_difference.png")
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.scatter(df["Goals_For"], df["Goals_Against"])

    for _, row in df.iterrows():
        plt.text(row["Goals_For"], row["Goals_Against"], row["team"])

    plt.title("Group K - Attack vs Defense")
    plt.xlabel("Goals For")
    plt.ylabel("Goals Against")
    plt.tight_layout()
    plt.savefig(figures_dir / "attack_vs_defense.png")
    plt.close()

    print(f"Figuras guardadas en: {figures_dir}")


if __name__ == "__main__":
    main()