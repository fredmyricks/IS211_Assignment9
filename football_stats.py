import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/all/'

# Make a request to the website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the touchdown stats
table = soup.find('table', {'class': 'data'})

# Find all the rows in the table
rows = table.find_all('td')

# Loop through each row to get player stats
for row in rows[1:21]:
    # Get the player name, position, and team
    name = row.find('td', {'class': 'name'}).text
    position = row.find('td', {'class': 'position'}).text
    team = row.find('td', {'class': 'team'}).text

    # Get the total number of touchdowns
    touchdowns = row.find_all('td')[5].text

    # Print the player stats to the screen
    print(name + ' (' + position + ', ' + team + ') - ' + touchdowns + ' touchdowns')
