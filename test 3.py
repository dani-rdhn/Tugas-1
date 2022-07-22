print("Daftar suhu yang ingin dikonversi:")
print("1 Celcius","\n2 Kelvin","\n3 Reamur","\n4 Fahrenheit")
#S=Suhu
S=float(input("Masukkan Nomor: "))
#Celcius
if S==1:
    C=float(input("Masukkan Temperatur Celcius: "))
    K=C+273
    R=4/5*C
    F=9/5*(C+32)
    print("Kelvin: ",K)
    print("Reamur: ",R)
    print("Fahrenheit: ",F)
    #Kelvin
else:
    if S==2:
        K=float(input("Masukkan Temperatur Kelvin: "))
        C=K-273
        R=4/5*(K-273)
        F=(K-273)*9/5+32
        print("Celcius: ",C)
        print("Reamur: ",R)
        print("Fahrenheit: ",F)
#Reamur
    else:
        if S==3:
            R=float(input("Masukkan Temperatur Reamur: "))
            C=5/4*R
            K=5/4*(R+273)
            F=9/4*(R+32)
            print("Celcius: ",C)
            print("Kelvin: ",K)
            print("Fahrenheit: ",F)
#Fahrenheit
        else:
            if S==4:
                F=float(input("Masukkan Temperatur Fahrenheit: "))
                C=float(5)/9*(F-32)
                K=float(5)/9*(F-32)+273
                R=float(4)/9*(F-32)
                print("Celcius: ",C)
                print("Kelvin: ",K)
                print("Reamur: ",R)