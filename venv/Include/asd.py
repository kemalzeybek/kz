import re
import os

f=open('deneme.txt', 'r')
hikaye = f.read()
f.close()
print(hikaye)
silinecekler = (re.findall("(<|>)", hikaye))
print(silinecekler)


x = (re.search(">", hikaye))

y = (re.search("<", hikaye))


print("---")
print(y)
print("---")
print(y.start())
print("y end")
print(y.end())

print("-----------")
z = y.start()
k = hikaye.replace(hikaye[z], "")
print(k)
print(k[2])
