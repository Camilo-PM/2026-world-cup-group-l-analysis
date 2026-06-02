# FIFA World Cup 2026 - Group L Analysis

## Overview

This project analyzes the teams competing in **Group L of the FIFA World Cup 2026** using recent match performance data. The objective is to evaluate each team's current form, attacking efficiency, defensive solidity, and overall competitive strength before the tournament begins.

The analysis is based on the last 10 matches played by each team and generates a series of performance metrics that can be used to compare the teams objectively.

### Teams Analyzed

* Croatia 🇭🇷
* England 🏴
* Ghana 🇬🇭
* Panama 🇵🇦

---

## Project Objectives

* Collect and process recent match data for all Group L teams.
* Evaluate attacking and defensive performance.
* Measure recent form and consistency.
* Generate comparative rankings using a custom Power Score metric.
* Create visualizations and Tableau dashboards for interactive exploration.

---

## Data Sources

Data was collected from publicly available football statistics sources and processed using Python.

Metrics are calculated from each team's last 10 competitive and international matches.

---

## Methodology

The project follows a complete data analysis workflow:

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Statistical Analysis
5. Data Visualization
6. Tableau Dashboard Creation

---

## Metrics Used

### Performance Metrics

* Matches Played
* Wins
* Draws
* Losses
* Goals Scored
* Goals Conceded
* Goal Difference

### Advanced Indicators

* Goals For per Game
* Goals Against per Game
* Win Rate
* Form Index
* Defense Index
* Power Score

The **Power Score** combines offensive output, defensive performance, and recent results to estimate overall team strength.

---

## Group L Results

| Team    | Power Score |
| ------- | ----------: |
| Croatia |       23.21 |
| England |       19.97 |
| Panama  |       13.41 |
| Ghana   |        8.51 |

### Key Findings

#### Croatia

* Highest Power Score in the group.
* Strong balance between attack and defense.
* 80% win rate over the last 10 matches.
* Enters the tournament as the statistical favorite.

#### England

* Excellent defensive record.
* Strong attacking output.
* Second-highest Power Score.
* Expected to compete directly with Croatia for first place.

#### Panama

* Demonstrated consistency and resilience.
* Stronger recent form than expected.
* Could challenge for qualification if able to maintain defensive discipline.

#### Ghana

* Lowest Power Score among the four teams.
* Inconsistent recent performances.
* Will likely need significant improvement to advance.

---

## Project Structure

```text
Group L/
│
├── configs/
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── reports/
│   └── figures/
│
├── src/
│   ├── collect_data.py
│   ├── clean_data.py
│   ├── analysis.py
│   ├── visualize.py
│   └── create_tableau_file.py
│
└── README.md
```

---

## Visualizations

The project includes:

* Team Form Ranking
* Goal Difference Comparison
* Attack vs Defense Analysis

Generated figures are stored in:

```text
reports/figures/
```

---

## Tableau Dashboard

Interactive dashboard:

**[Add Tableau Public Link Here]**

---

## Repository

GitHub Repository:

https://github.com/Camilo-PM/2026-world-cup-group-l-analysis

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Tableau Public

---

## Conclusion

Based on recent performance metrics, Croatia and England emerge as the strongest teams in Group L and appear to be the most likely candidates to advance to the knockout stage.

Panama enters the tournament as a potential surprise contender, while Ghana faces the challenge of improving its recent form to remain competitive.

The analysis demonstrates how data-driven methods can provide objective insights into team performance and World Cup expectations.
