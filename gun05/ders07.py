class Ogrenci():
    kurs = "Btk Akademi Python Kursu"
    bolum = ""

ogrenci1 = Ogrenci()
print(ogrenci1.kurs)
# ogrenci1.bolum = "makina"
print(ogrenci1.bolum)
ogrenci1.ad = "ertuna"
print(vars(ogrenci1))
print(vars(Ogrenci))
ogrenci2 = Ogrenci()
print(vars(ogrenci2))