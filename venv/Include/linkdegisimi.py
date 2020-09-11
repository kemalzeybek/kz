#kayıtlı txt deki linki istediğin linkle değiştirme


import re
import os
f=open('denemehikaye.txt', 'r')
hikaye = f.read()
f.close()
print(hikaye)
print("----------")
hikayeyeni = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', 'yenisite">', hikaye)


print(hikayeyeni)