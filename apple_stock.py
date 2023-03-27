import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'

# Make a request to the website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the stock prices
table = soup.find('table', {'data-test': 'historical-prices'})

# Find all the rows in the table
rows = table.find_all('tr')

# Loop through each row to get stock prices
for row in rows[1:-1]:
    # Get the date and closing price
    date = row.find_all('td')[0].text
    close_price = row.find_all('td')[4].text

    # Print the stock price to the screen
    print(date + ' - $' + close_price)
