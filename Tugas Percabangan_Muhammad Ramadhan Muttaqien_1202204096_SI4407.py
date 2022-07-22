tanggal = int(input("Masukkan Tanggal : "))
bulan = int(input("Masukkan Bulan : "))
tahun = int(input("Masukkan Tahun : "))
print("Saya lahir" , tanggal,"-",bulan,"-",tahun) 
angkaSaya = (tanggal*1)+(bulan*10)+tahun
print(angkaSaya)
if angkaSaya % 400 == 0 :
    print("merupakan tahun kabisat," , angkaSaya + 2021)
elif angkaSaya % 100 == 0:
    print("bukan tahun kabisat," , angkaSaya - 2021)
elif angkaSaya % 4 == 0:
    print("merupakan tahun kabisat," , angkaSaya + 2021)
else:
    print("bukan tahun kabisat," , angkaSaya - 2021)
