import requests
from bs4 import BeautifulSoup
url="https://www.nobroker.in/"
res=requests.get(url=url)
#print(res._content)
html_content=res.content
soup=BeautifulSoup(html_content,'html.parser')
print(soup.title.text)

print(soup.find_all('ul'))
