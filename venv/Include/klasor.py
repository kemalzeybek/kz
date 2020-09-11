#md klasör ismi klasör oluşturur . dizin=os.listdir()   bulunduğun dizindeki elemanları arraye atar.

import os

os.system("md Yeni_Klasor")
print("Klasör başarılı bir şekilde oluşturuldu.")
print (os.listdir("."))

dizin=os.listdir()

print(dizin[3])