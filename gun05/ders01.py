dosya = open("deneme.txt")
# icerik = dosya.read()
# print(type(icerik))
# print(icerik)
# print(icerik[:6])
# print("///"*10)
# icerik2 = dosya.read()
# print(icerik2)
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())
satirlar = dosya.readlines()
for satir in satirlar:
    print(satir, end="")
dosya.close()