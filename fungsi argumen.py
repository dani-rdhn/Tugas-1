# def myfun(x,y,z):
#     print("x:", x)
#     print("y:", y)
#     print("z:", z)

# myfun(x=50,y=100,z=100)
#=======================================================

# def atlit(nama, negara, juara):
#     print(nama, negara, juara)

# atlit("usain bolt","afrika","juara 1")
# atlit(nama="usain bolt",negara="afrika",juara="juara 1")
#=======================================================

# def datadiri(nama, umur, berat, tinggi):
#     print(nama, umur, berat, tinggi)

# datadiri(nama="usain",umur="20",berat="70 kg",tinggi="175 cm")
#=======================================================

# def faktorial(n):
#     if n==0:
#         return 1
#     else:
#         return(n*faktorial(n-1))

# print("faktorial 4!=4*3! adalah = ", faktorial(4))
# print("faktorial 5!=5*4! adalah = ", faktorial(5))
# print("faktorial 6!=6*5! adalah = ", faktorial(6))
#=======================================================

# print(*[x for x in range(5)])
# print(int(input('masukkan angka = ')))
#=======================================================

# x = int(input("Masukkan angka : "))
# n = 1
# if x <= 1:
#         print("Error, masukkan kembali dengan benar")
# elif x >= 98:
#         print("Error, masukkan kembali dengan benar")
# else:
#         for i in range(1, x+1):
#                 n = n*i
#         print("Hasil faktorialnya adalah", n)
#=======================================================

# isi_list = ["apel","pisang","mangga"]
# print(isi_list[0])
# print(isi_list[0:2])
# =======================================================

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas #Mengembalikan nilai luas

# #Memanggil Fungsi
# #Misalkan dengan panjang = 10 dan lebar = 5
# print("Luas Persegi Panjang adalah", luas_persegi_panjang(10,5))
# =======================================================

# luas_persegi_panjang = lambda x,y : print(x * y)
# print('luas persegi ppanjang adalah')
# luas_persegi_panjang(3,4)
# =======================================================

# list_data = [1,2,3,4,5,6,7,8,9,10]
# result_map_kuadrat = map(lambda item : item*item, list_data) #untuk data yang dikuadratkan
# result_filter_genap = filter(lambda item : item %2 == 0, list_data) #untuk data yang genap
# result_filter_ganjil = filter(lambda item : item %2 != 0, list_data) #untuk data yang ganjil

# print("list = ", list_data)
# print("list dengan isi dikuadratkan = ", list(result_map_kuadrat))
# print("list dengan isi genap = ", list(result_filter_genap))
# print("list dengan isi ganjil = ", list(result_filter_ganjil))

