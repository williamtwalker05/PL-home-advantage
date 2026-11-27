# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 17:01:52 2026

@author: will0
"""

import pandas as pd

seasons = [f"{y}{y+1}" for y in range(15,25)]


cols = [
    "Date",      # match date
    "HomeTeam",  # home team name
    "AwayTeam",  # away team name
    "FTHG",      # full-time home goals
    "FTAG",      # full-time away goals
    "FTR",       # full-time result: H = home win, D = draw, A = away win
    "HS",        # home shots
    "AS",        # away shots
    "HST",       # home shots on target
    "AST",       # away shots on target
]
all_teams = set()
for code in seasons:
    df = pd.read_csv(f"data/raw/E0_{code}.csv")
    total = df[cols].isna().sum().sum()
    print(code, total)
    if total>0:
        print(df[cols].isna().sum())
    all_teams.update(df["HomeTeam"])
    sorted(all_teams)
print(all_teams)
