def toplama(a,b):
    return a + b
def fark(a,b):
    return a- b
def islemYap(islem,sayi1,sayi2):
    match islem:
        case "+":
            print(toplama(sayi1, sayi2))
        case "-":
            print(fark(sayi1, sayi2))
        case _:
            print("hatali işlem seçimi")
def karsilama():
    print("programa hosgeldin")
    islem = input("+,-")
    def sayiAl():
        return int(input("sayi giriniz: "))
    sayi1 = sayiAl()
    sayi2 = sayiAl()
    islemYap(islem,sayi1,sayi2)

if __name__=="__main__":
    karsilama()