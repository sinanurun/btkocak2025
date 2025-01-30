import random
rastgele = random.randrange(1,1000)
print("tutulan sayı",rastgele)
tahminSayisi = 10
taban = 0
tavan = 1001
while tahminSayisi >= 1:
    tahmin =random.randrange(taban,tavan)
    # tahmin =int(input("sayı giriniz"))
    print(tahmin , end=" ")
    cevap = input("+,-,=")
    if cevap == "=":
        print("Tebrikler")
        break
    elif cevap == "+" :
        print("daha küçük")
        tavan = tahmin
    elif cevap == "-":
        print("daha büyük")
        taban = tahmin
    tahminSayisi -= 1
    print("kalan hakkınız", tahminSayisi)
# import random
# baslangic = 1
# bitis = 250
# tutulan = random.randint(baslangic,bitis)
#
# tahminSayisi = 10
# taban = baslangic
# tavan = bitis
# while tahminSayisi >= 1:
#     metin = f"{taban} - {tavan} aralığında bir tam sayı giriniz"
#     tahmin = int(input(metin))
#     if tahmin == tutulan:
#         print("bildiniz tebrikler")
#         break
#     else:
#         tahminSayisi -= 1
#         if tahminSayisi == 0:
#             print("tahmin hakkınız doldu bilemediniz")
#             break
#         elif tahmin > tutulan:
#             print("daha küçük bir sayı ile deneyiniz")
#             tavan = tahmin
#         elif tahmin < tutulan:
#             print("daha büyük bir sayı ile deneyiniz")
#             taban = tahmin
#         print("kalan tahmin hakkınız",tahminSayisi)
#
