

def invest(jumlah_pokok, rate, tahun):
    list = []
    list1 = []
    for i in range(tahun):
        jumlah_pokok = jumlah_pokok + jumlah_pokok * rate
        print(f"tahun {i+1} : ", jumlah_pokok)
        list.append(jumlah_pokok)
        list1.append(i+1)
        print(list)
        print(list1)


invest(100, 0.05, 4)


# print(100+100*0.05)
