barang=[]
harga=[]
def df():
    print("\n")
    print("---Daftar Barang---")
    print("[1] Pensil")
    print("[2] Buku     ")
    print("[3] Penghapus")
    print("\n")
jumlahbarang = int(input("Masukkan jumlah barang belanja: "))
df()
if jumlahbarang > 0:
    jumlah = 0
    if jumlahbarang == 1:
        for x in range(1, 1 + 1, 1):
            nomorbarang = int(input("Masukkan nomor barang: "))
            if nomorbarang == 1:
                namabarang = "Pensil"
                hargabarang = 2000
            else:
                if nomorbarang == 2:
                    namabarang = "Buku     "
                    hargabarang = 6000
                else:
                    if nomorbarang == 3:
                        namabarang = "Penghapus"
                        hargabarang = 3000
                    else:
                        print("Anda salah memasukkan nomor")
            barang.append(namabarang)
            harga.append(hargabarang)
            jumlah = jumlah + hargabarang
            i=1
    else:
        if jumlahbarang == 2:
            for x in range(1, 2 + 1, 1):
                nomorbarang = int(input("Masukkan nomor barang: "))
                if nomorbarang == 1:
                    namabarang = "Pensil"
                    hargabarang = 2000
                else:
                    if nomorbarang == 2:
                        namabarang = "Buku     "
                        hargabarang = 6000
                    else:
                        if nomorbarang == 3:
                            namabarang = "Penghapus"
                            hargabarang = 3000
                        else:
                            print("Anda salah memasukkan nomor")
                barang.append(namabarang)
                harga.append(hargabarang)
                jumlah = jumlah + hargabarang
                i=2
        else:
            if jumlahbarang == 3:
                for x in range(1, 3 + 1, 1):
                    nomorbarang = int(input("Masukkan nomor barang: "))
                    if nomorbarang == 1:
                        namabarang = "Pensil"
                        hargabarang = 2000
                    else:
                        if nomorbarang == 2:
                            namabarang = "Buku     "
                            hargabarang = 6000
                        else:
                            if nomorbarang == 3:
                                namabarang = "Penghapus"
                                hargabarang = 3000
                            else:
                                print("Anda salah memasukkan nomor")
                    barang.append(namabarang)
                    harga.append(hargabarang)
                    jumlah = jumlah + hargabarang
                    i=3
            else:
                print("Anda salah memasukkan jumlah")
    totalharga = jumlah
else:
    print("Anda salah memasukkan jumlah")
print("\n")
print("-----Nota Pembelian Toko Alat Tulis-----")
print("\n")
print("No","\t","Nama Barang","\t","\t","Harga")
print("---------------------------------------")
def pertama():
    for i in range(len(barang)):
        pass
    for i in range(len(barang)):
        pass
    for i in range(len(harga)):
        print(i+1,"\t",barang[i],"\t","\t",harga[i])
pertama()
print("---------------------------------------")
print("\t","Total","\t","\t","\t",totalharga)