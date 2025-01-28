ortalama = float(input("Ortalama giriniz"))
belgeAlmaDurumu = (ortalama >= 70)

tesekkurAlmaDurumu = (85 > ortalama >= 70)
# ((85 > ortalama) and (ortalama >= 70))

takdirAlmaDurumu = (100 >= ortalama >= 85)
# ((100 >= ortalama) and (ortalama >= 85))

print("herhangi bir belge alma durumunuz :",belgeAlmaDurumu)
print("teşekkür belgesi alma durumunuz :", tesekkurAlmaDurumu)
print("takdir belgesi alma durumunuz :",takdirAlmaDurumu)