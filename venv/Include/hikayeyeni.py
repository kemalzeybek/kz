import re
import os

f=open('hikaye.txt', 'r')
hikaye = f.read()
f.close()
print(hikaye)
print("--------")

print(re.search("p", hikaye))
print("--------")

silinecekler = (re.findall("(<|>)", hikaye))

print("--------")

print(hikaye.replace("<p>", "fsdfasdf"))
yenihikaye = (hikaye.replace("<p>", "fsdfasdf"))
print("--------")
print(yenihikaye)










