"""
This program scrapes NBA matches' data from a betting odds website
and saves all the years from 2009 to 2018 to a single file.
This code is only compatible with the Google Chrome browser.
The betting odds website is https://www.oddsportal.com
"""

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Setting up Selenium browser
chromepath = r"C:\Users\c1yeung\Desktop\chromedriver.exe"  # Path is different for your computer
options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome(chromepath, chrome_options=options)

# Setting up URLs to iterate
baseURL_left = "https://www.oddsportal.com/basketball/usa/nba-"
baseURL_right = "/results/#/page/"
URL = {}
for year in range(2008, 2018):
    URL[year] = baseURL_left + str(year) + "-" + str(int(year) + 1) + baseURL_right

# Scraping the data
finalodds = []
for year in URL:
    print("Now scraping the", str(year) + " to " + str(year + 1) + " NBA season")
    for page in range(1, 30):
        pageURL = URL[year] + str(page)
        browser.get(pageURL)
        time.sleep(2)
        source = browser.page_source
        soup = BeautifulSoup(source, 'lxml')
        odds_table = soup.find('table', {'class': 'table-main'})
        full_table = odds_table.find('tbody').findAll('tr', {'class': 'deactivate'})
        temp = []

        # Adding data to table
        for table in full_table:
            teamNames = table.find('td', {'class': 'table-participant'}).find('a').get_text()
            temp.append(teamNames)
            odds = table.findAll('td', {'class': 'odds-nowrp'})
            for odd in odds:
                gameOdds = odd.contents[0].get_text()
                temp.append(gameOdds)
            finalodds.append(temp)
            temp = []

# Close browser
browser.close()

# Formatting the data
formatted_odds = [[]]
for game in finalodds:
    teams = game[0].split(" - ")
    formatted_game = [teams[0], teams[1], game[1], game[2]]
    formatted_odds.append(formatted_game)
formatted_odds.remove([])

# Exporting the data into a csv file
with open("bettingOdds.csv", "w") as csv:
    for game in formatted_odds:
        csv.write(str(game[0]) + "," + str(game[1]) + "," + str(game[2]) + "," + str(game[3]))
        csv.write("\n")
