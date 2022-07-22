n=5
f=1
if n==0:
    f=1
elif n>=1:
    for i in range(1, n+1):
        f = f*i
else:
    print("Kembali mengisi bilangan yang benar")

print("Hasil Faktorialnya adalah : ", n)