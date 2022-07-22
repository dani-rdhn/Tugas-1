a = int(input("Masukkan nilai a = "))
b = int(input("Masukkan nilai b = "))
print("Nilai Semula a,b = ", a,",",b)
def tukar(a,b):
    temp = a
    a = b
    b = temp
    print("di dalam fungsi a,b =", a,",",b)
  
tukar(a,b)
print("Sesudah keluar fungsi a,b = ", a,",",b)