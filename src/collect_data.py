import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import TEAMS, RAW_DIR, LAST_N_MATCHES


def flatten_columns(df):
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            "_".join([str(item) for item in col if str(item) != "nan"]).lower()
            for col in df.columns
        ]
    else:
        df.columns = [str(col).lower() for col in df.columns]

    return df


def clean_columns(df):
    df.columns = [
        str(col).strip().lower().replace(" ", "_")
        for col in df.columns
    ]
    return df


def find_match_tables(html_path):
    tables = pd.read_html(html_path)
    valid_tables = []

    for table in tables:
        table = flatten_columns(table)
        table = clean_columns(table)

        columns = table.columns.tolist()

        has_date = any("date" in col for col in columns)
        has_gf = any(col == "gf" or col.endswith("_gf") for col in columns)
        has_ga = any(col == "ga" or col.endswith("_ga") for col in columns)

        if has_date and has_gf and has_ga:
            valid_tables.append(table)

    return valid_tables


def get_column(df, target):
    for col in df.columns:
        if col == target or col.endswith(f"_{target}"):
            return col
    return None


def collect_team_matches(team_name, html_files):
    all_matches = []

    for html_file in html_files:
        html_path = Path(html_file)

        if not html_path.exists():
            print(f"Archivo no encontrado: {html_path}")
            continue

        tables = find_match_tables(html_path)

        for table in tables:
            table["team"] = team_name
            all_matches.append(table)

    if not all_matches:
        print(f"No se pudieron extraer datos para {team_name}")
        return None

    team_df = pd.concat(all_matches, ignore_index=True)

    date_col = get_column(team_df, "date")
    gf_col = get_column(team_df, "gf")
    ga_col = get_column(team_df, "ga")

    if not date_col or not gf_col or not ga_col:
        print(f"Columnas necesarias no encontradas para {team_name}")
        return None

    team_df[date_col] = pd.to_datetime(team_df[date_col], errors="coerce")
    team_df[gf_col] = pd.to_numeric(team_df[gf_col], errors="coerce")
    team_df[ga_col] = pd.to_numeric(team_df[ga_col], errors="coerce")

    team_df = team_df.dropna(subset=[date_col, gf_col, ga_col])
    team_df = team_df.sort_values(date_col, ascending=False)
    team_df = team_df.drop_duplicates()
    team_df = team_df.head(LAST_N_MATCHES)

    output_path = RAW_DIR / f"{team_name.lower().replace(' ', '_')}_last_10.csv"
    team_df.to_csv(output_path, index=False)

    print(f"{team_name}: {len(team_df)} partidos jugados guardados")

    return team_df


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for team_name, html_files in TEAMS.items():
        collect_team_matches(team_name, html_files)


if __name__ == "__main__":
    main()

