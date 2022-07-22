import numpy as np

# # buat array dari list
# array = np.array([1,2,3,4,5])
# print(array)
# print(type(array))

# # buat array dua dimensi dengan karakter a b c d e dan 1 2 3 4 5
# array2 = np.array([['a','b','c','d','e'], [1,2,3,4,5]])
# print(array2)

# # array 3 dimensi dengan sumbu x,y,z 
# # di dalam sumbu z terdapat 2 array 2 dimensi dengan nilai 123, 456
# array3 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
# print(array3)

#DIMENSI ARRAY
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
# a = np.array(1)                                 # tidak ada dimensi
# print("hasil dari a :", a)
# print("jumlah dimensi a :", a.ndim)

# # An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
# b = np.array([1,2,3,4,5])                       # satu dimensi array 
# print("hasil dari b :", b)
# print("jumlah dimensi b :", b.ndim)

# # An array that has 1-D arrays as its elements is called a 2-D array. These are often used to represent matrix or 2nd order tensors.
# c = np.array([[1,2,3,4,5], [6,7,8,9,10]])       # dua dimensi array
# print("hasil dari c :", c)
# print("jumlah dimensi c :", c.ndim)

# # # An array that has 2-D arrays (matrices) as its elements is called 3-D array. These are often used to represent a 3rd order tensor.
# d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])    # tiga dimensi array
# print("hasil dari d :", d)
# print("jumlah dimensi d :", d.ndim)

# # AKSES ELEMEN DENGAN INDEX
# # a = np.array([[1,2,3], [4,5,6]])
# # print(a)
# print("indeks pada a yang diambil adalah :", a[0,0]) 
# print("indeks pada a yang diambil adalah :", a[0,1])
# print("indeks pada a yang diambil adalah :", a[1,1])

# # MENGIRIS ELEMEN ARRAY 2 DIMENSI
# a = np.array([[1,2,3,4], [5,6,7,8]])
# print(a)
# print(a[0, 0:3])

# angka = np.array([1,2,3,4,5])       # 1 dimensi
# for i in angka:
#     print(i, end =" ")

# angka1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])  # 2 dimensi
# for i in angka1:
#     print(i)

arr = np.empty((0,3), int)
arr = np.append(arr, np.array([[1,2,3]]), axis=0)
arr = np.append(arr, np.array([[4,5,6]]), axis=0)
angka = np.array([80,75,60,50,90])
hasil = angka*(30/100)
print(arr)
    
# for i in angka:
#     print("value =", i)