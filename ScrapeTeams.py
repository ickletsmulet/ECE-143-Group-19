from bs4 import BeautifulSoup
import requests
import numpy as np
import csv


# Creating a dictionary of URLs for each year from 1989 to 2018 (30 years).
baseURL_left = "https://www.basketball-reference.com/leagues/NBA_"
baseURL_right = ".html"
URL = {}
for year in range(1989, 2019):
    URL[year] = baseURL_left + str(year) + baseURL_right

# This part scrapes data from the NBA database and creates a list
# of lists of each team's win rate
total_table = []
for year in URL:
    print("Getting stats from " + str(year))
    source = requests.get(URL[year]).text
    soup = BeautifulSoup(source, 'lxml')
    section = soup.findAll('div', {'class': 'standings_divs'})
    table_year = []
    for sec in section:
        player_table = sec.findAll('table', {'class': 'stats_table'})
        for Btable in player_table:
            full_table = Btable.find('tbody').findAll('tr', {'class': 'full_table'})
            for table in full_table:
                team = table.find('th', {'data-stat': "team_name"})
                team_name = team.find('a').get_text()
                stats = table.findAll('td', {'class': 'right'})
                wl_pct = table.find('td', {'data-stat': "win_loss_pct"}).get_text()
                temp = [team_name, wl_pct]
                table_year.append(temp)
    total_table.append(table_year)
    filename = "TeamStats" + str(year) + ".csv"
    with open(filename, "w") as csv:
        for team in table_year:
            csv.write(str(team[0]) + "," + str(team[1]))
            csv.write("\n")
print(total_table)
print("Done")
