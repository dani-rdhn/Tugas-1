import numpy as np
from numpy.core.fromnumeric import reshape
# # while
# for x in range(5):
#     print(input(""))
# x = np.array([[], []])
# print(x)

arr = np.empty((0,6), int)
for x in range(5):
    nama = str(input("Masukkan nama : "))
    nik = float(input("Masukkan NIM : "))
    n_tgs_quiz = float(input("Masukkan Nilai Tugas dan Quiz : "))
    n_praktikum = float(input("Masukkan Nilai Praktikum : "))
    n_uts = float(input("Masukkan Nilai UTS : "))
    n_uas = float(input("Masukkan Nilai UAS : "))
    index = 
    arr = np.append(arr, np.array([nama,nik,n_tgs_quiz,n_praktikum,n_uts,n_uas]))
a = arr.reshape(5,6)
print(a)
# index = np.asarray(arr[2] * arr[3] * arr[4] * arr[5])
# print("nilai :", index)
# print("Nama\t\t", "Nik\t\t", "Tugas dan Quiz\t", "UTS\t", "UAS\t", "Total\t", "Index\t")
# print(arr[0],"\t\t",arr[1],"\t",arr[2],"\t\t",arr[3],"\t",arr[4],"\t",arr[5], "\t")

# step_n = 10
# steps = np.random.choice([-1, 0, 1], size=(1,2))
# for n in range(step_n-1):
#     step = np.random.choice([-1, 0, 1], size=(1,2))
#     print(steps)
#     steps = np.append(steps, step, axis=0)
#     #something will be checked after each n

# print(steps)

# steps = np.array([-1, 0, 1])
# print(steps)