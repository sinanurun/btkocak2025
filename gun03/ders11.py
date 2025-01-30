yemekler = {"Çorbalar":{"etli":["işkembe","kelle paça","tavuk suyu"],
                        "bakliyatli":["mercimek","ezoegelin"],
                        "sebzeli":["domates","brokoli"]},
            "Kebaplar":{"acılı":["adana","beyti"],
                        "acısız":["urfa","mardin"],
                        "dürümler":["ciger","adana"]},
            "icecekler":["çay","kahve"]
        }
print(yemekler["Çorbalar"]["etli"])
yemekler["Çorbalar"]["etli"].append("Bayram Çorbası")
print(yemekler["Çorbalar"]["etli"])
serbetli_tatli = ["Baklava"]
yemekler["tatlilar"]= {"şerbetlitatlilar":serbetli_tatli}
print(yemekler)
yemekler["tatlilar"]["sütlütatlılar"]=["puding"]
print(yemekler)
serbetli_tatli.append("şeker pare")
print(yemekler)