class Kitap():
    ad = ""
    yazar = ""
    basim_yili = ""

kitap_listesi = []
for i in range(5):
    kitap = Kitap()
    kitap.ad = input("Kitap adını giriniz")
    kitap_listesi.append(kitap)

for i in kitap_listesi:
    print(i.ad)