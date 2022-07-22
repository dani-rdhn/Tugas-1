import numpy as np
from numpy.core.fromnumeric import reshape

arr = np.empty((0,6), str,int)
for x in range(5):
    nama = str(input("Masukkan nama : "))
    nik = float(input("Masukkan NIM : "))
    n_tgs_quiz = float(input("Masukkan Nilai Tugas dan Quiz : "))
    n_praktikum = float(input("Masukkan Nilai Praktikum : "))
    n_uts = float(input("Masukkan Nilai UTS : "))
    n_uas = float(input("Masukkan Nilai UAS : "))
    arr = np.append(arr, np.array([nama,nik,n_tgs_quiz,n_praktikum,n_uts,n_uas]))
a = arr.reshape(5,6)
print("\n","Nama\t", "Nik\t", "Tugas dan Quiz\t", "UTS\t", "UAS\t", "Total\t", "Index\t","\n")
index1 = arr[2]*0.2 + arr[3]*0.2 + arr[4]*0.3 + arr[5]*0.3
index2 = arr[8]*0.2 + arr[9]*0.2 + arr[10]*0.3 + arr[11]*0.3
index3 = arr[14]*0.2 + arr[15]*0.2 + arr[16]*0.3 + arr[17]*0.3
index4 = arr[20]*0.2 + arr[21]*0.2 + arr[22]*0.3 + arr[23]*0.3
index5 = arr[26]*0.2 + arr[27]*0.2 + arr[28]*0.3 + arr[29]*0.3
if index1 >= 80:
    print("A")
elif index1 >= 70:
    print("B")
elif index1 >= 60:
    print("BC")
elif index1 >= 50:
    print("C")
elif index1 <= 49:
    print("e")
else:
    print("salah")

if index2 >= 80:
    print("A")
elif index2 >= 70:
    print("B")
elif index2 >= 60:
    print("BC")
elif index2 >= 50:
    print("C")
elif index2 <= 49:
    print("e")
else:
    print("salah")

if index3 >= 80:
    print("A")
elif index3 >= 70:
    print("B")
elif index3 >= 60:
    print("BC")
elif index3 >= 50:
    print("C")
elif index3 <= 49:
    print("e")
else:
    print("salah")

if index4 >= 80:
    print("A")
elif index4 >= 70:
    print("B")
elif index4 >= 60:
    print("BC")
elif index4 >= 50:
    print("C")
elif index4 <= 49:
    print("e")
else:
    print("salah")

if index5 >= 80:
    print("A")
elif index5 >= 70:
    print("B")
elif index5 >= 60:
    print("BC")
elif index5 >= 50:
    print("C")
elif index5 <= 49:
    print("e")
else:
    print("salah")

b = arr[0:6]
c = arr[6:12]
d = arr[12:18]
e = arr[18:24]
f = arr[24:30]
print(b)
print(c)
print(d)
print(e)
print(f)
