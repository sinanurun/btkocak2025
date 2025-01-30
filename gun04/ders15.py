def ogrenciKarti(*args,**kwargs):
    print(kwargs)
    print(type(kwargs))
    for bilgiler in kwargs:
        print(bilgiler, kwargs[bilgiler])
ogrenciKarti("YOK Kartı",oadi="defne",ogrenciNo=251)