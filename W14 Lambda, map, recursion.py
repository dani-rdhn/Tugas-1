import numpy as np
from functools import reduce
# def f1():
#     print("bisa berhasil")

# f1()

# nilai = lambda a,b : a*b
# print(nilai(2,2))

# x = lambda a : a*5
# print(x(2))

# y = lambda a : a-10
# print(y(12))

# z = lambda a,b,c : a+b+c
# print(z(1,2,3))
# # -------------------------------------------------------

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(3)
# print(mydoubler(11))
# # -------------------------------------------------------

# def kalidua(n):
#     return n*2

# angka = (1,2,3,4)
# hasilMapObject = map(kalidua, angka)
# print("hasil dari map adalah ", hasilMapObject)
# hasil = list(hasilMapObject)
# print(hasil)
# # -------------------------------------------------------

# def tri_recursion(k):
#     if (k>0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("contoh recursion")
# tri_recursion(7)
# # -------------------------------------------------------

# arr = np.zeros((5,7))
# print(arr)

angka = [1,2,3,4,5,6,7,8,9,10]
genap = list(filter(lambda n : n%2==0, angka))   # filter angka genap
print(genap)
kali = list(map(lambda n : n*2, genap))         # mengkalikan semua angka pada list yang sudah difilter
print(kali)
tambah_semua = reduce(lambda a,b : a+b, kali)   # Menjumlahkan semua angka di dalam list
print(tambah_semua)