"""
This program is used to scrape NBA data and separate into a different
file for each year between 1989 and 2019 for all NBA players (31 years).
The website used is https://www.basketball-reference.com
"""

# Imports
from bs4 import BeautifulSoup
import requests
import csv

# This part creates a dictionary of URLs
baseURL_left = "https://www.basketball-reference.com/leagues/NBA_"
baseURL_right = "_advanced.html"
URL = {}
for year in range(1989, 2020):
    URL[year] = baseURL_left + str(year) + baseURL_right

# This part scrapes data from the NBA database and creates a table for all stats
for year in URL:
    print("Getting stats from " + str(year))
    source = requests.get(URL[year]).text
    soup = BeautifulSoup(source, 'lxml')
    player_table = soup.find('table', {'class': 'sortable stats_table'})
    full_table = player_table.find('tbody').findAll('tr', {'class': 'full_table'})
    total_table = []
    for table in full_table:
        player_name = table.find('td', {'data-stat': "player"}).get_text()
        stats = table.findAll('td', {'class': 'right'})
        team = table.find('td', {'data-stat': "team_id"}).get_text()
        temp = [player_name, team]

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

    # Exporting data to csv file
    filename = "AvgPlayerStats" + str(year) + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(total_table)
    print("Done")
print("All tasks complete")