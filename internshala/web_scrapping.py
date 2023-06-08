import requests
from bs4 import BeautifulSoup
import html5lib

url="https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"

#Send an HTTP request to the webpage you want to scrape and retrieve its HTML content:
content = requests.get(url)

#fetching the content of html page
htmlcontent=content._content

#parsing raw html data
soup=BeautifulSoup(htmlcontent,'html.parser')

# fetching the title
title=soup.title
print(title.string)

#fecting the content of page
pagecontent=soup.get_text
print(pagecontent)

