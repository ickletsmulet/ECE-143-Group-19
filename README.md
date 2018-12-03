ECE-143-Group-19

NBA Player Stats and Betting Odds

In this project, we scraped data from the NBA stats website and a betting oddsmaker website
to perform some data analysis tasks.
We trained a model to determine which NBA advanced stats are the most impactful, and used
players' advanced stats to predict NBA team's overall yearly win rates. We also predicted
the outcome of every match in a given year based on the advanced stats of the players on
each team's roster. Finally, we used all of the acquired knowledge to recommend the optimal
team to bet on for the highest payout. We did this by comparing the two teams' win probability
for a given match with the given betting odds and calculated the expected value of the payout
for betting on the home/visiting team.


To run the code, you must have several modules installed:
torchvision,
BeautifulSoup,
selenium,
requests


Depending on how you decide to download and save the csv data files,
the code may not find the necessary data files in the desginated paths.
In that case, change the code or the file locations to make the code work.


Some of the code's formatting may be messed up when viewed from GitHub. The code will
still work but it is best viewed in JupyerNotebook for cleaner formatting appearances.
