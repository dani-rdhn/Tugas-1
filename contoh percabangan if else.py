total = 0
pensil = 2000
buku = 6000
penghapus = 3000
print("""" 
1. Pensil
2. Buku
3. Penghapus
0. selesaikan""")
banyak = int(input("Masukkan banyak barang belanjaan: "))
for i in range(banyak):
    barang = int(input("Masukkan barang yang dipilih = "))
    if barang==1:
        barang=2000
    elif barang==2:
        barang=6000
    elif barang==3:
        barang=3000
    total = total + i
print("jumlahnya: ", total)
    
print("No","\t", "Nama barang", "\t\t\t\t", "harga") 

totall= 0
banyak=int(input("Masukan Banyak Barang belanjaan:"))
for x in range (banyak):
     harga=int(input("Masukkan harga barang:"))
     totall = totall+harga
if totall >= 75000:
    total = totall-((totall)*0.2)
    print("Total belanjaan sebelum diskon RP.",totall)
    print("Total belanjaan setelah diskon RP.",total)

else:
     print("Total belanjaan yang harus dibayar RP.",totall)