"""
This program is used to scrape and average all NBA
players' stats who played from 1989 to 2018 (30 years).
"""

# Imports
from bs4 import BeautifulSoup
import requests
import numpy as np
import csv

# This part creates a dictionary of URLs for each year from 1989 to 2018.
baseURL_left = "https://www.basketball-reference.com/leagues/NBA_"
baseURL_right = "_advanced.html"
URL = {}
for year in range(1989, 2019):
    URL[year] = baseURL_left + str(year) + baseURL_right

# Scraping NBA data to get each player's stats
total_table = []
for year in URL:
    print("Getting stats from " + str(year))
    source = requests.get(URL[year]).text
    soup = BeautifulSoup(source, 'lxml')
    player_table = soup.find('table', {'class': 'sortable stats_table'})
    full_table = player_table.find('tbody').findAll('tr', {'class': 'full_table'})
    for table in full_table:
        player_name = table.find('td', {'data-stat': "player"}).get_text()
        stats = table.findAll('td', {'class': 'right'})
        temp = [player_name]

        # Cleaning up empty columns and adding data to overall table
        column = 0
        for stat in stats:
            column += 1
            if column == 16 or column == 21:
                continue
            playerstats = stat.get_text()
            if not playerstats:
                playerstats = "0"
                temp.append(playerstats)
            else:
                temp.append(playerstats)
            total_table.append(temp)
    print("Done")

# Averaging player career stats
print("Calculating players' career stats")
player_dict = {}
for player in total_table:
    if player[0] not in player_dict:
        player_dict[player[0]] = [player[1:]]
    else:
        player_dict[player[0]].extend([player[1:]])
for player, stats in player_dict.items():
    for stat in stats:
        for i in range(len(stat)):
            stat[i] = float(stat[i])
    avg = np.around(np.mean(np.array(stats), axis=0), decimals=3).tolist()
    player_dict[player] = avg

# Exporting data to csv file
print("Writing to AvgPlayerStats.csv")
with open("AvgPlayerStats.csv", 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile, delimiter=',')
    for player, stats in player_dict.items():
        csv_writer.writerow([player] + stats)
print("All tasks complete")
