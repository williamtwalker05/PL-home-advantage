# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:32:56 2026

@author: will0
"""

import os
from urllib.request import urlretrieve

RAW_DIR = "data/raw" #Stores the folder path in a variable

os.makedirs(RAW_DIR, exist_ok=True) #creates but doesnt crash if already exists

seasons = [f"{y}{y+1}" for y in range(15,25)] #creates 1516,1617, etc

for code in seasons:
    url = f"https://www.football-data.co.uk/mmz4281/{code}/E0.csv"
    filepath = os.path.join(RAW_DIR, f"E0_{code}.csv")
    urlretrieve(url, filepath)
    print(f"Downloaded {code} -> {filepath}")