from pathlib import Path

# ======================================
# BASE PATHS
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
FINAL_DIR = DATA_DIR / "final"

HTML_DIR = RAW_DIR / "html"

REPORTS_DIR = BASE_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# ======================================
# SETTINGS
# ======================================

LAST_N_MATCHES = 10

# ======================================
# TEAMS
# ======================================

TEAMS = {
    "Croatia": [
        HTML_DIR / "croatia.html",
        HTML_DIR / "croatia_2025.html",
    ],

    "England": [
        HTML_DIR / "england.html",
        HTML_DIR / "england_2025.html",
    ],

    "Ghana": [
        HTML_DIR / "ghana.html",
        HTML_DIR / "ghana_2025.html",
    ],

    "Panama": [
        HTML_DIR / "panama.html",
        HTML_DIR / "panama_2025.html",
    ],
}

# ======================================
# OUTPUT FILES
# ======================================

RAW_MATCHES_FILE = RAW_DIR / "group_l_last_10_raw.csv"

CLEAN_MATCHES_FILE = (
    PROCESSED_DIR / "group_l_last_10_clean.csv"
)

SUMMARY_FILE = FINAL_DIR / "group_l_summary.csv"

TABLEAU_FILE = FINAL_DIR / "group_l_tableau.csv"