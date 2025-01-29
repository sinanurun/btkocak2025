ogrenci_adi = "Eda"
ogrenci_soyadi = "Kırkar"
ogrenci_no = 231
ogrenci_cinsiyet = True
ogrenci_ortalama = 3.15

ogrenci1 = [ogrenci_adi, ogrenci_soyadi, ogrenci_no, ogrenci_cinsiyet, ogrenci_ortalama]
print(ogrenci1, type(ogrenci1))

ogrenci2 = ["zeynep","Işıklar",232,True,3.50]
print(ogrenci2, type(ogrenci2))

print(ogrenci1[0], type(ogrenci1[0]))
print(ogrenci2[0])
print(len(ogrenci1))
print(ogrenci1[:3])
print("zeynep" in ogrenci1)
print("Eda" in ogrenci1)

# for bilgi in ogrenci2:
#     print(bilgi)