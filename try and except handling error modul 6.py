# while True:
#     try:
#         tanggal = int(input("tanggal lahir saya adalah : "))
#         break
#     except ValueError:
#         print("yang anda masukkan bukan angka")
#     except NameError:
#         print("yang anda masukkan bukan angka")

# print("tanggal yang anda masukkan adalah", tanggal)
# ----------------------------------------------------------------

# print("=== PROGRAM PERKALIAN ANGKA ===")
# while True:
#     try:
#         angka1 = int(input("masukkan angka pertama : "))
#         angka2 = int(input("masukkan angka kedua : "))
#         hasil = angka1*angka2
#         break
#     except:
#         print("bukan angka")

# print("hasilnya adalah", hasil)
# ----------------------------------------------------------------

# print("=== PROGRAM PEMBAGI ANGKA ===")
# while True:
#     try:
#         angka1 = int(input("masukkan angka pertama : "))
#         angka2 = int(input("masukkan angka kedua : "))
#         hasil = angka1/angka2
#         break
#     except ValueError:
#         print("bukan angka")
#     except ZeroDivisionError:
#         print("angka tidak boleh nol")

# print("hasilnya adalah", hasil)

# def hitung(x,y):
    
#     while True:
#         try:
#             return x + y 
#         except NameError:
#             print("str tidak bisa")
#         except ValueError:
#             print("nilai harus berupa angka, bukan huruf")
#         else:
#             print(x+y)
#             print("fungsi berhasil dijalankan")
#             break
#         finally:
#             print("fungsi ini akan selalu berjalan ketika selesai")

# x = int(input("masukkan angka pertama : "))
# y = int(input("masukkan angka kedua : "))
# hasil = print("hasilnya adalah", hitung(x,y))

# try:
#     x = int(input("Masukkan hanya angka :"))
#     10/x
#     raise ValueError("hanya boleh angka yang dimasukkan")
# except ZeroDivisionError:
#     print("terjadi error, masukkan angka selain 0")
# finally:
#     print("ini tetap berjalan")

# jenis-jenis except Error:
# 1. except IOError           # Error input-output/buka-tutup file
# 2. except ImportError       # Error import package
# 3. except ValueError        # Error harus angka ketika malah huruf yang dimasukkan
# 4. except ZeroDivisionError # Error ketika membagi bilangan dengan 0
# 5. except KeyboardInterrupt 
# 6. except EOFError
