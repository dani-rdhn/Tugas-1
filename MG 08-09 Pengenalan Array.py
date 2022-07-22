#LIST
# buah = ["mangga","jambu","durian","salak","cempedak","duku","rambutan"]
# sayuran = ["wortel, kentang, kol"]
# buah.remove("durian")       # menghilangkan durian pada list
# print(buah)
# buah.pop(0)                 # menghilangkan indeks 0
# print(buah)
# del buah[2]                 # menghilangkan indeks 2
# print(buah)
# buah.append("kelengkeng")   # menambahkan kelengkeng pada indeks terakhir                                           
# print(buah)
# buah[3] = "pisang"          # menambahkan pisang pada indeks ke 3
# print(buah)
# print(buah[0])              # hanya print indeks ke-0 pada list
# buah.insert(0,"jeruk")      # menambahkan kata jeruk pada indeks ke-0
# print(buah)
# buah.extend(sayuran)        # menyatukan list sayuran ke list buah
# print(buah)
# ---------------------------------------------------------------------------------------------------------------------------------------

# x = [1,2,3,4,5,6]
# y = [5,10]
# z = [0,0,0,0,0,0]
# z[1] = x[1] * y[0]
# z[2] = x[2] * y[1]  
# print(z)
# ---------------------------------------------------------------------------------------------------------------------------------------

# angka = [1,2,3,4,5,1,3,4,5,6,7,8,9,5,4,3,2,3,4,5,3,2,3,4,2,43,34,8,9,5,4,3,2,3,4,5,3,5,1,3,4,5,6,6,7,8,9,5,4,3,2,3,4,5,3,2,3,4,2,43]
# umur = [23,24,35,2,3,5,6,7,8,9,0,34,12,52,65,76,45,34,65,76,34,76,34,76,87,34,65,34,64,33,11,23,34,23,45,65,76,33,43,54,34,56]
# print(len(angka))
# print(len(umur))
# print(len(angka) - len(umur))
# for i in range(10):
#     print(i, end=" ")
# ---------------------------------------------------------------------------------------------------------------------------------------

# nilaiUTS=[40,34,56,40,90,30]
# for i in range(len(nilaiUTS)):
#     nilaiUTS[i] = nilaiUTS[i] + 20
#     if (nilaiUTS[i] >= 95):
#         nilaiUTS[i] = 95

# print(nilaiUTS) 
# ---------------------------------------------------------------------------------------------------------------------------------------

# buah = ["pisang", "mangga", "jeruk"]
# print("buah sebelum ditambah : ", buah)
# print("jumlah buah sebelum ditambah", len(buah))
# inputBuah = input("Masukkan nama buah baru : " )
# buah.append(inputBuah)
# print("buah setelah ditambah : ", buah)
# print("jumlah buah setelah ditambah : ", len(buah))
# print(buah)
# ---------------------------------------------------------------------------------------------------------------------------------------

#TUPLE
# angka = (1,2,3,4,5)                         # data adalah tuple dan integer
# buah = ("pisang", "mangga", "jeruk")        # data adalah tuple dan string
# makanan = (["pisang", "mangga", "jeruk"], ["wortel", "kentang", "kol"]) #data adalah tuple dengan isinya list
# print(angka)
# print(buah)
# print(makanan)
# print(makanan[0])


#SETS
a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = set(range(1,11))
d = set(range(5))
print(c)
print(d)

print(a|b)
gabungan = a.union(b)
print(gabungan)

print(a&b)
irisan = a.intersection(b)
print(irisan)

#DICTIONARY
nama_dict = {
    "key" = "value"
    "nama" = "dani"
    "nim" = 1202204096
    "hobi" = ["game", "musik"]
    
}
