"""
This program is used to scrape the matches played and their results
and separate into a different file for each year between 1989 and
2019 for all NBA teams (31 years).
The website used is https://www.basketball-reference.com
"""

# Imports
from bs4 import BeautifulSoup
import requests

# This part creates a dictionary of URLs
baseURL_left = "https://www.basketball-reference.com/leagues/NBA_2018_games-"
baseURL_right = ".html"
month_list = ['october', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june']
URL = {}
for month in month_list:
    URL[month] = baseURL_left + str(month) + baseURL_right

# Starts scraping
for year in range(1989, 2020):
    initURL_left = "https://www.basketball-reference.com//leagues/NBA_"
    initURL_right = "_games.html"
    initURL = initURL_left + str(year) + initURL_right
    init_source = requests.get(initURL).text
    init_soup = BeautifulSoup(init_source, 'lxml')
    init_container = init_soup.find('div', {'id': 'content'})
    month_sec = init_container.find('div', {'class': 'filter'}).findAll('div')
    month_list = []
    for sec in month_sec:
        c_month = sec.find('a').get_text()
        month_list.append(c_month.lower())
    # This part creates a dictionary of URLs
    baseURL_left = "https://www.basketball-reference.com/leagues/NBA_"
    baseURL_mid = "_games-"
    baseURL_right = ".html"
    URL = {}
    for month in month_list:
        URL[month] = baseURL_left + str(year) + baseURL_mid + str(month) + baseURL_right
    # This part scrapes results of every game for test years.
    total_table = []
    for month in URL:
        print("Getting stats from " + str(month))
        source = requests.get(URL[month]).text
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('table', {'class': 'suppress_glossary sortable stats_table'})
        section = table.find('tbody').findAll('tr')
        for sec in section:
            if sec.get_text() != 'Playoffs':
                team = sec.findAll('td', {'class': 'left'})
                visit_team_name = team[0].find('a').get_text()
                home_team_name = team[1].find('a').get_text()
                visit_score = sec.find('td', {'data-stat': "visitor_pts"}).get_text()
                home_score = sec.find('td', {'data-stat': "home_pts"}).get_text()
                if visit_score > home_score:
                    result = 'Visiting'
                elif visit_score < home_score:
                    result = 'Home'
                temp = [visit_team_name, home_team_name, result]
                total_table.append(temp)

    filename = "GameResults" + str(year) + ".csv"
    len_table = len(total_table)
    with open(filename, "w") as csv:
        for i in range(len_table):
            visit = total_table[len(total_table) - i - 1][0]
            home = total_table[len(total_table) - i - 1][1]
            result = total_table[len(total_table) - i - 1][2]
            csv.write(visit + "," + home + "," + result)
            csv.write("\n")
print("Done")
