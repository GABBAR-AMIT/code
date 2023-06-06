import requests
from bs4 import BeautifulSoup
url="https://versus.com/en/nvidia-geforce-gtx-750-ti-vs-zotac-geforce-gtx-1050-mini"
res=requests.get(url=url)
#print(res._content)
html_content=res.content
soup=BeautifulSoup(html_content,'html.parser')
print(soup.title.text)

for i in soup.find_all('div id'):
    print(i.text)
