import random
baslangic = 1
bitis = 250
tutulan = random.randint(baslangic,bitis)

tahminSayisi = 10
taban = baslangic
tavan = bitis
while tahminSayisi >= 1:
    metin = f"{taban} - {tavan} aralığında bir tam sayı giriniz"
    tahmin = int(input(metin))
    if tahmin == tutulan:
        print("bildiniz tebrikler")
        break
    else:
        tahminSayisi -= 1
        if tahminSayisi == 0:
            print("tahmin hakkınız doldu bilemediniz")
            break
        elif tahmin > tutulan:
            print("daha küçük bir sayı ile deneyiniz")
            tavan = tahmin
        elif tahmin < tutulan:
            print("daha büyük bir sayı ile deneyiniz")
            taban = tahmin
        print("kalan tahmin hakkınız",tahminSayisi)

