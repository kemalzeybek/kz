#basliktaki p etiketini atıyor
import re
import os


f=open('baslik1.txt', 'r')
baslik = f.read()
f.close()
print(baslik)
print("--------")
x = baslik.replace("<p>", "")
x = baslik.replace("</p>", "")
print(x)
os.remove("baslik1.txt")
c = open("baslik1.txt", "a")
c.write(x)
c.close()
