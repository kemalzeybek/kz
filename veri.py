import requests
from bs4 import BeautifulSoup
headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
link = "http://www.sekshikayem.info/kuzenimin-ami-seftali-kadar-lezetliydi.html"
r = requests.get(link, headers=headersparam)
soup = BeautifulSoup(r.content,"lxml", from_encoding='UTF-8')
print(soup)

http://www.otuzbizhikaye.info/bakireligim-gitmisti-olsun-ama/




print(re.sub("<p>","", hikaye))




print(re.search(">", hikaye))
x = (re.search(">", hikaye))
y = (re.search("<", hikaye))
print (x.end())
print(y.start())
z = y.start()
k = hikaye.replace(hikaye[y], "")
print(k)
