# class kubus:
#     def __init__(self,sisi): #constructor menggunakan method bawaan Python yang bernama init 
#         self.sisi = sisi
             
#     def tampilkansisi(self):
#         print(self.sisi)
    
#     def luas(self):
#         print("luas =", self.sisi **2)
#     def volume(self):
#         print("volue =", self.sisi**3)
#     def luas_permukaan(self):
#         print ("luas permukaan =", self.sisi*6)
        
# kubus1=kubus(4)
# kubus1.tampilkansisi()
# kubus1.luas()
# kubus1.volume()
# kubus1.luas_permukaan()
# #----------------------------------------------------------------------------

# class orang: 
#     def __init__(self,nama,nim):
#         self.nm = nama
#         self.np = nim

#     def tampilkan(self):
#         print ("nama:", self.nm,"\nnim:", self.np)

# class mahasiswa(orang):
#     pass

# orang=orang("fitri", "1234556")
# orang.tampilkan()

# fitri=mahasiswa("anisa","19990422")
# fitri.tampilkan()
#----------------------------------------------------------------------------


class Hero:
    jumlahHero = 0

    def __init__(self, inputName, inputHealth, inputAttack): #constructor menggunakan method bawaan Python yang bernama init 
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        Hero.jumlahHero += 1
             
    def namanya(self):
        print('namanya adalah = ' + self.name)
    
    def healthup(self,up):
        self.health += up 

    def attackup(self):
        print("attacknya adalah = " + self.attack)
   
hero1 = Hero('diluc', 20000, 1900)
hero2 = Hero('keqing', 19000, 2200)

hero1.namanya()

hero1.healthup(200)
print(hero1.health)

print(hero1.name)

print(hero2.__dict__)
#----------------------------------------------------------------------------

class nasabah:
    def __init__ (self,no,nm,rek):
        self.NoNasabah=no
        self.NamaNasabah=nm
        self.NomerRek=rek
    def tampilkan(self):
        print ("Nomer Nasabah:", self.NoNasabah, "Nama Nasabah:", self.NamaNasabah, "Rekening Nasabah:", self.NomerRek)
class rekening():
    def __init__ (self,rek,sal):
        self.rekeninh=rek
        self.saldo=sal
    def ambil(self):
        ambil_uang=int(input("ambil uang senilai : "))
        hasil=self.saldo-ambil_uang
        self.saldo = hasil
        print ("jumlah penarikan", ambil_uang, "sisa", hasil)
    def setor(self):
        setor_uang=int(input("menyetor sebesar : "))
        hasil=self.saldo+setor_uang
        self.saldo = hasil
        print("jumlah setoran", setor_uang, "sisa",hasil)
    def cek_saldo(self):
        print ("saldo", self.saldo)
        
fitri=nasabah("1", "Fitri Anisa","170411100014")
fitri.tampilkan() 

fitri_rek=rekening("170411100014", 100000)
fitri_rek.ambil()
fitri_rek.setor()
fitri_rek.cek_saldo()
#----------------------------------------------------------------------------