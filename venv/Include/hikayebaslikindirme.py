#hikayeyi ve basligi ayri ayri kayit ediyor.

import requests
import os
from bs4 import BeautifulSoup

headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

link = "http://www.sekshikayem.info/abimin-arkadasi-beni-gotten-parcaladi.html"

r = requests.get(link, headers=headersparam)

soup = BeautifulSoup(r.content,"lxml", from_encoding='UTF-8')

gelen_veri = soup.find_all("div", attrs={"class" : "entry-content clearfix"})

hikaye = (gelen_veri[0])
hikaye = hikaye.find_all("p")
hikayebaslik = hikaye[0]
print("Hikaye Baslik = " , hikayebaslik)
print(hikaye[1])
print("--------------")
print(hikayebaslik)
with open("baslik1.txt" , 'w') as f:
   f.write(str(hikayebaslik))
with open("hikaye1.txt" , 'w') as f:
   f.write(str(hikaye[1]))



