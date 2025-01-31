class Ogrenci():
    pass

ogrenci1 = Ogrenci()
ogrenci1.ad = "ertuna"
ogrenci1.soyad = "aykaç"
print(ogrenci1, ogrenci1.ad, ogrenci1.soyad)
print(vars(ogrenci1))
ogrenci2 = Ogrenci()
ogrenci2.ad = "iclal"
ogrenci2.soyad = "yiğitoğlu"
ogrenci2.bolum = "mekatronik"
print(ogrenci2, ogrenci2.ad, ogrenci2.soyad, ogrenci2.bolum)
print(vars(ogrenci2))