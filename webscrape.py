import requests
from bs4 import BeautifulSoup

def webscrape(root):
    pass

# URL of the website to scrape (replace with your target URL)
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the HTML content of the page
    print(response.text)
else:
    print("Failed to retrieve the page.")
