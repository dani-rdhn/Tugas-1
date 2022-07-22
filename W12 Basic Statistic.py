import numpy as np
nilai = np.random.randint(low=40, high=100, size=7) # Jumlah data ganjil
nilaiSort = np.sort(nilai, axis=None)
print("Nilai sebelum diurutkan", nilai)
print("Nilai setelah diurutkan", nilaiSort)
print("Nilai median", np.median(nilai))
