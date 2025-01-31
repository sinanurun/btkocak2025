class Ogrenci():
    bolum = "bilisim"
    kurs = "btk kursu"

    def __init__(self,ad, soyad, tc):
        print("öğrenci oluşturuldu")
        self.ad = ad
        self.soyad = soyad
        self.tcno = tc
        self.ortalama = None
        # self.tamAd()

    def tamAd(self):
        self.tamad = self.ad + self.soyad
        return self.tamad

    def __str__(self):
        return self.tamad

ogr1 = Ogrenci("ali","can",123546)
# ogr1.tamAd()
# Ogrenci.tamAd(ogr1)
print(ogr1.tamad)
print(ogr1)

