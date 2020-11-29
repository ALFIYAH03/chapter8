
#chapter8
#latihan7


def hargaTermahal(a):
    harga = list(a.values())
    harga.sort(reverse=True)
    hargaMahal = harga[0]
    for buah, harga in a.items():
        if harga == hargaMahal:
            return buah

buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}

print(hargaTermahal(buah))
