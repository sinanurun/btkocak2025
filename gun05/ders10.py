class Ogrenci():
    bolum = "bilisim"
    kurs = "btk kursu"

    def __init__(self,ad, soyad, tc):
        print("öğrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc
        self.tamad = self.ad + self.soyad
        self.ortalama = None

ogr1 = Ogrenci("ali","can",123546)
print(ogr1.bolum)
print(ogr1.ad)
print(vars(ogr1))
print(vars(Ogrenci))

