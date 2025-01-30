def ortalama(*args):
    print(args, type(args))
    print(*args)
    toplam = 0
    for i in args:
        toplam += i
    sonuc = toplam / len(args)
    return sonuc

sortalama = ortalama(1,2,3,4,6,5)
print(sortalama)