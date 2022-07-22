# total = 625
# i = 2
# a = 0

# while a <= total:
#     a = i**2
#     i += 1
#     if i % 4 == 0:
#         continue
#     elif i % 3 == 0:
#         continue
#     elif a <= 20:
#         continue
#     print(i)

# for n in range(1, 26):
#     square = n**2
#     print(n)


tahunAwal = input("Tahun Awal Peminjaman: ")
bulanAwal = input("Bulan Awal Peminjaman: ")
tanggalAwal = input("Tanggal Awal Peminjaman: ")
tahunAkhir = input("Tahun Akhir Peminjaman: ")
bulanAkhir = input("Bulan Akhir Peminjaman: ")
tanggalAkhir = input("Tanggal Akhir Peminjaman: ")
jenis = input("Jenis Buku: ")

# lanjutkan codenya atau algoritmanya di bawah ini (tidak satu baris)
if int(tahunAkhir) - int(tahunAwal) > 1:
    if int(bulanAkhir) - int(bulanAwal) >= 1:
        durasi = int(tahunAkhir)-int(tahunAwal)*12*30 + \
            (((int(bulanAkhir)-int(bulanAwal)*30)+int(tanggalAkhir))-int(tanggalAwal))
    else:
        durasi = int(tahunAkhir)-int(tahunAwal)*12*30 + \
            (int(tanggalAkhir)-int(tanggalAwal))

    if int(tahunAkhir) - int(tahunAwal) < 0:
        durasi = (int(bulanAkhir)+12-int(bulanAwal)) * \
            30+int(tanggalAkhir)-int(tanggalAwal)

    if int(tahunAkhir) - int(tahunAwal) == 0:
        durasi = int(tanggalAkhir)-int(tanggalAwal)

    else:
        durasi = (int(bulanAkhir)-int(bulanAwal)) * \
            30+int(tanggalAkhir)-int(tanggalAwal)

if jenis == "R":
    lama = 14
    denda = 2000
elif jenis == "T":
    lama = 30
    denda = 1500
elif jenis == "B":
    lama = 7
    denda = 1200
else:
    lama = 3
    denda = 1000

total = (durasi-lama)*denda

print(f'Total denda = {total} Rupiah')
