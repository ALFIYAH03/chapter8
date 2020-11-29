
#chapter8
#latihan9

try:
    
    for x,y in buah.items():
        print("{0}. {1} = {2}".format (number,x,y))
        number += 1

    choose = input("\nNama buah yang dibeli : ")
    if (choose in buah):
        kg = float (input('Berapa Kg             : '))
        print ('-'*30)
        print("Total harga          :",buah [choose]  * kg)
    else:
        print('\n{0} tidak ada dalam daftar buah' .format(choose))
except ValueError:
        print('data yang anda masukan bukan angka / salah')
        
