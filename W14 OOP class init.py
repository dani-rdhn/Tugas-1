class mahasiswa():
    def __init__(self, nama, nim, kelas, alamat):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.alamat = alamat

    def show(self):
        print("Nama\t:", self.nama)
        print("NIM\t:", self.nim)
        print("Kelas\t:", self.kelas)
        print("Alamat\t:", self.alamat)

mahasiswa1 = mahasiswa("Ananda", "1202190008", "SI-43-02", "Palangkaraya \n")
mahasiswa2 = mahasiswa("Xaximi", "12021902937", "SI-42-04", "Bogor \n",)
mahasiswa3 = mahasiswa("Rizal", "1202128729", "SI-43-01", "Bandung")

mahasiswa1.show()
mahasiswa2.show()
mahasiswa3.show()

class kalkulator:
    def __init__(self, bilangan1, bilangan2):
        self.angka_pertama = bilangan1
        self.angka_kedua = bilangan2

    def penjumlahan(self):
        print ("hasil operasi penjumlahan = ", self.angka_pertama + self.angka_kedua)
    def pengurangan(self):
        print ("hasil operasi penjumlahan = ", self.angka_pertama - self.angka_kedua)
    def perkalian(self):
        print("hasil operasi penjumlahan = ", self.angka_pertama * self.angka_kedua)
    def pembagian(self):
        print("hasil operasi penjumlahan = ", self.angka_pertama / self.angka_kedua)

print("Program kalkulator sederhana")
print("""   Main menu
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
5. Keluar""")
pilih = int(input("Pilihan anda (1/2/3/4/5) = ")) 

if pilih >= 5:
    print("keluar dari program")    
else:
    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : ")) 
    n = kalkulator(angka1,angka2)
    if pilih == 1:
        n.penjumlahan()
    elif pilih == 2:
        n.pengurangan()
    elif pilih == 3:
        n.perkalian()
    elif pilih == 4:
        n.pembagian()
    else:
        print("keluar")

