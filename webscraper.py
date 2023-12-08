import pandas as pd
import numpy as np
from scipy.stats import zscore

import requests
import os
from bs4 import BeautifulSoup

# Set Playoff Years from 2020 to 2023
years = list(range(2016, 2025))

# {} used to vary dates in loop
url_start = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

# Replace brackets with specific years based on list
for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    # Create HTML files for each year
    with open("topPicksHTML/Playoffs-{}_topPicks.html".format(year), "wb") as f:
        f.write(data.content)
        
# using a loop, parse each html for each year in years list
dfs = []
for year in years:
    url = url_start.format(year)
    data = requests.get(url)
    soup = BeautifulSoup(data.content, "html.parser")
    topPicks_table = soup.find("table", {"id": "per_game_stats"})
    topPicks_df = pd.read_html(str(topPicks_table))[0]
    topPicks_df = topPicks_df[topPicks_df.Rk != "Rk"]
    topPicks_df["Year"] = year

    dfs.append(topPicks_df)

    # Save all contents into one csv files into new folder called topPicksCSV
    topPicks_df.to_csv("topPicksCSV/Playoffs-{}_topPicks.csv".format(year), index=False)
    
# combine all dataframes into one
df = pd.concat(dfs)
df.to_csv("topPicksCSV/Playoffs-Master_topPicks.csv", index=False)

print(df.head())