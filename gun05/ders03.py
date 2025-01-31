import os
import time

# dosya_adi = "deneme.txt"
# with open(dosya_adi, "w") as dosya:
#     dosya.write("sınıf başarı sırası 1")
#
# with open(dosya_adi, "r") as dosya:
#     print(dosya.read())

dosya_adi = "deneme3.txt"
if not(os.path.exists(dosya_adi)):
    # os.makedirs(dosya_adi)
    dosya = open(dosya_adi,"x")
    print("doys oluşturuldu")
    dosya.close()
else:
    print("dosya zaten mevcut oluşturumaya gerek yok")

time.sleep(5)
if os.path.exists(dosya_adi):
    os.remove(dosya_adi)
    print("dosya silindi")
else:
    print("dosya yok ki silelim")