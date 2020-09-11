import requests
import os
from bs4 import BeautifulSoup
headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
link = "http://www.sekshikayem.info/abimin-arkadasi-beni-gotten-parcaladi.html"
r = requests.get(link, headers=headersparam)
soup = BeautifulSoup(r.content,"lxml", from_encoding='UTF-8')
div = soup.find_all("div", attrs={"class" : "entry-content clearfix"})
print(div)
with open('file.txt', 'w') as f:
   f.write(str(div[0]))