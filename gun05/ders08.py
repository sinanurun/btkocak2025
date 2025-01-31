class Kitap():
    ad = ""
    yazar = ""
    yayinevi = ""
    kitap_turu = ""
    sayfa = ""
    basim_yili = ""

kitap1 = Kitap()
kitap1.ad = "ince memet"
kitap1.yazar = "yaşar kemal"

print(kitap1.ad, kitap1.yazar)
kitap_bilgileri1 = vars(kitap1)
print(kitap_bilgileri1)
print(vars(Kitap))