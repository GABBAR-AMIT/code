import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = 'https://www.augnw.com/'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Locate the relevant HTML elements and extract the data
article_titles = soup.find_all('h2', class_='article-title')

# Print the extracted titles
for title in article_titles:
    print(title.text.strip())
