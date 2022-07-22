x = int(input("Masukkan angka : "))
n = 1
if x <= 1:
        print("Error, masukkan kembali dengan benar")
elif x >= 98:
        print("Error, masukkan kembali dengan benar")
else:
        for i in range(1, x+1):
                n = n*i
        print("Hasil faktorialnya adalah", n)
