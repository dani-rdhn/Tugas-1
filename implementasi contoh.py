class Node:
    def __init__(self, title, singer):
        self.data_title = title
        self.data_singer = singer
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def enqueue(self, new_val_title, new_val_singer):
        newNode = Node(new_val_title, new_val_singer)
        newNode.next = None
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = newNode
        newNode.prev = last
        return

    def play_current(self, p):
        n = self.head
        if p == 1:
            return n.data_title, n.data_singer
        else:
            for i in range(p-1):
                n = n.next
            return n.data_title, n.data_singer

    def play_next(self, p):
        n = self.head
        for i in range(p):
            n = n.next
        return n.data_title, n.data_singer

    def play_prev(self, p):
        n = self.head
        for i in range(p-1):
            n = n.next
        n = n.prev
        return n.data_title, n.data_singer

    def display(self):
        if self.head is None:
            print("Tidak Ada Lagu")
            return
        else:
            n = self.head
            count = 1
            while n is not None:
                print(f"{count}. {n.data_title}, {n.data_singer}", end="\n")
                n = n.next
                count += 1

if __name__ == "__main__":
    print("""
--- PLAYLIST MUSIC PLAYER ---
1. Buat playlist kamu
2. Putar lagu
3. Putar selanjutnya
4. Putar sebelumnya
5. Lihat playlist kamu""")
    dll = DoublyLinkedList()
    pointer = 1
    while True:
        menu = int(input("\nPilih menu: "))
        if menu == 1:
            song_count = int(input("Masukkan jumlah lagu dalam playlist: "))
            for i in range(1, song_count+1):
                input_song_sing = input(f"Masukkan lagu ke-{i} (judul, singer): ").split(", ")
                dll.enqueue(input_song_sing[0], input_song_sing[1])
            print("\nPlaylist sudah dibuat...")
        elif menu == 2:
            print(f"Kamu sedang memutar lagu {dll.play_current(pointer)[0]} dari {dll.play_current(pointer)[1]} ")
        elif menu == 3:
            print(f"Kamu sedang memutar lagu {dll.play_next(pointer)[0]} dari {dll.play_next(pointer)[1]} ")
            pointer += 1
        elif menu == 4:
            print(f"Kamu sedang memutar lagu {dll.play_prev(pointer)[0]} dari {dll.play_prev(pointer)[1]} ")
            pointer -= 1
        elif menu == 5:
            print("\n~~~ Playlist Kamu ~~~")
            dll.display()   
        elif menu == 6:
            break

# 1
# 6
# Okinawa, 92914
# Easy On Me, Adele
# Lucky, Jason Mraz
# Sad, Maroon 5
# MONEY, LISA
# Sick Feeling, Boy Pablo