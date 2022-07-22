#Membuat Class untuk Node
class Node:
    def __init__(self, name, number):
        self.data_name = name
        self.data_number = number
        self.next = None

#Inisiasi class untuk linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    #Menambahkan kontak
    def appendKontak(self, new_name, new_number):
        newNode = Node(new_name, new_number)
        newNode.next = None
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = newNode
        return

    #Mengubah Kontak
    def ubahData(self, kontak):
        n = self.head
        while n:
            if kontak in n.data_name:
                print(f"Nama Kontak {n.data_name} dengan nomor {n.data_number}")
                print("======================================================")
                input_name_number = input("Masukkan data baru (Nama, Nomor): ").split(", ")
                n.data_name = input_name_number[0]
                n.data_number = input_name_number[1]
                print("Berhasil Ubah Kontak")
            n = n.next

    #Mencari kontak
    def searchKontak(self, kontak):
        if self.head is None:
            print("Tidak ada nama pada kontak")
        else:
            n = self.head
            while n is not None:
                if kontak == n.data_name:
                    print(f"kontak {n.data_name} dengan nomor {n.data_number} ditemukan")
                n = n.next

    #Menampilkan Kontak
    def displayKontak(self):
        if self.head is None:
            print("Tidak Ada Isi Kontak")
            return
        else:
            n = self.head
            count = 1
            while n is not None:
                print(f"{count}. {n.data_name}, {n.data_number}", end="\n")
                n = n.next
                count += 1

if __name__ == "__main__":
    print("""
==================================
--- BUKU KONTAK TOKO MAJU JAYA ---
==================================

1. Buat Kontak Baru
2. Lihat isi Kontak
3. Cari Kontak dengan nama
4. Ubah Kontak
5. Exit""")
    dll = SinglyLinkedList()
    pointer = 1
    while True:
        menu = int(input("\nPilih menu: "))
        if menu == 1:
            input_name_number = input(f"Masukkan kontak baru (nama, nomor): ").split(", ")
            dll.appendKontak(input_name_number[0], input_name_number[1])
            print("Kontak sudah ditambahkan.")
        elif menu == 2:
            print("\n~~~ List Kontak ~~~")
            dll.displayKontak()   
        elif menu == 3:
            input_name = input("Cari kontak berdasarkan nama: ")
            dll.searchKontak(input_name)
        elif menu == 4:
            input_name = input("Ubah kontak berdasarkan nama: ")
            dll.ubahData(input_name)
        elif menu == 5:
            print("\nkeluar dari buku kontak\n")  
            break


#Adi, 089567849305
#jaya, 08128352805
#Cahya, 08968395025
#Joko, 08359242975