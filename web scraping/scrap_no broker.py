import requests
from bs4 import BeautifulSoup
url="https://www.bawakoof.com/"
res=requests.get(url=url)
#print(res.content)
html_content=res.content
soup=BeautifulSoup(html_content,'html.parser')
#print(soup.title.text)

print(soup.find_all('div',class_="productCardboard"))
