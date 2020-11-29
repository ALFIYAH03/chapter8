
#chapter8
#latihan4


list1 = ["Menu:",
"A. Tambah data sayur",
"B. Hapus data sayur",
"C. Tampilkan data sayur"]

for c in list1:
    print(c)

pil = input("pilihan anda : ")

print("_______________________")

a = ["bayam", "tomat", "cabai" , "wortel" , "bawang", "kangkung", "kacang"]


if pil == "A":
    syrtmb = input("nama sayur yang ingin ditambahakan = ")
    a.append(syrtmb)
    print("perubahan data = ", a)
elif pil == "B":
    try:
        dele = input("nama sayur yang ingin dihapus = ")
        a.remove(dele)
    except ValueError:
        print("data tidak ditemukan")
elif pil == "C":
    print(a)
else:
    print("input tidak valid")
