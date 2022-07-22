angka_tebakan = 3 #Set angka jawaban sebagai 3
jumlah_tebakan = 0 #Set 0 karena tebakan dimulai dari 0
kesempatan_menebak = 5 #Set 5 kali untuk menebak
nama = input("Masukkan nama kamu: ")

while jumlah_tebakan < kesempatan_menebak:
    tebakan = int(input("Coba tebak angka 1-10: "))
    jumlah_tebakan += 1 #Setiap ada input, jumlah tebakan bertambah 1
    if tebakan > angka_tebakan:
        print("Angka yang ditebak terlalu besar! Coba lagi :D")
    elif tebakan < angka_tebakan:
        print("Angka yang ditebak terlalu kecil! Coba lagi ._.")
    elif tebakan == angka_tebakan:
        print("Wih " + nama + " menebak dengan benar! Angka tersebut adalah", angka_tebakan, ".", "Jumlah tebakanmu sebanyak",
        jumlah_tebakan, "kali.")
        break
else:
    print("Yah kamu gagal menebak :( Mulai lagi jika ingin mencoba! Jawabannya adalah", angka_tebakan, ".")