def toplama(a,b):
    return a + b
def fark(a,b):
    return a- b
def karsilama():
    print("programa hosgeldin")
    islem = input("+,-")
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    match islem:
        case "+":
            print(toplama(sayi1,sayi2))
        case "-":
            print(fark(sayi1,sayi2))
        case _ :
            print("hatali işlem seçimi")    
if __name__=="__main__":
    karsilama()