
#chapter8
#latihan8

def averageHarga(x):
    Harga = list(x.values())
    jumlah = 0
    pembagi = 0
    for i in Harga:
        jumlah = jumlah + i
        pembagi += 1
    average = jumlah/pembagi
    return average

buah ={'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' :6500}
print(averageHarga(buah))

