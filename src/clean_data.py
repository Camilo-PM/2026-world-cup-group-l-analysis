import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import RAW_DIR, PROCESSED_DIR


def standardize_result(value):
    if pd.isna(value):
        return None

    value = str(value).lower()

    if value.startswith("w"):
        return "Win"
    elif value.startswith("d"):
        return "Draw"
    elif value.startswith("l"):
        return "Loss"

    return None


def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    files = list(RAW_DIR.glob("*_last_10.csv"))

    if not files:
        print("No se encontraron archivos CSV en data/raw/")
        return

    df_list = []

    for file in files:
        df = pd.read_csv(file)
        df_list.append(df)

    df = pd.concat(df_list, ignore_index=True)

    df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]

    required_columns = ["team", "date", "opponent", "gf", "ga", "result"]
    available_columns = [col for col in required_columns if col in df.columns]
    df = df[available_columns]

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["gf"] = pd.to_numeric(df["gf"], errors="coerce")
    df["ga"] = pd.to_numeric(df["ga"], errors="coerce")

    df["goal_difference"] = df["gf"] - df["ga"]
    df["result_clean"] = df["result"].apply(standardize_result)

    df["points"] = df["result_clean"].map({
        "Win": 3,
        "Draw": 1,
        "Loss": 0
    })

    df = df.dropna(subset=["date", "gf", "ga", "result_clean"])

    output_path = PROCESSED_DIR / "group_L_last_10_clean.csv"
    df.to_csv(output_path, index=False)

    print(f"Dataset limpio guardado en: {output_path}")


if __name__ == "__main__":
    main()

