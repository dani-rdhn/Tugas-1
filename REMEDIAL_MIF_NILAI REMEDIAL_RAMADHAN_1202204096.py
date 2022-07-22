print("=== PROGRAM SEDERHANA NILAI REMEDIAL MAHASISWA ===")

data_mhs = {
    "Nama"  : "Dani",
    "NIM"   : "1202204096",
    "Kelas" : "SI-44-07",
    "Nilai UAS" : 70,
    "Status"    : "Belum lulus"
}

print("\nNilai UAS Sebelum Remedial")
for key, val in data_mhs.items():
    print(key, ":", val)

print("\nNilai UAS Setelah Remedial")
data_mhs["Nilai UAS"] = 80
data_mhs["Status"] = "Lulus"
for key, val in data_mhs.items():
    print(key, ":", val)