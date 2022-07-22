from collections import defaultdict
from typing import ValuesView

class graph:
    def __init__(self): #Konstruktor
        self.graph = defaultdict(list)
        self.vertices_no = 0
        self.weights = {} 

    def insertVertex(self, vertex): #Method Create Vertex
        if vertex in self.graph:
            print(f"nilai {vertex} sudah ada di dalam graph!")
        else:
            self.graph[vertex] = []
            self.vertices_no += 1

    def insertEdge(self, ver1, ver2, weight): #Method Create Edge (Connecting Vertex)
        if ver1 not in self.graph:
            print(f"Nilai {ver1} tidak ada di dalam graph!")
        elif ver2 not in self.graph:
            print(f"Nilai {ver2} tidak ada di dalam graph!")
        else:
            self.graph[ver1].append(ver2)
            self.graph[ver2].append(ver1)
            self.weights[(ver1, ver2)] = weight
            self.weights[(ver2, ver1)] = weight

    def getGraph(self):
        return self.graph

    def checkRoute(self, initial, end): #Reference Djikstra Method (https://benalexkeen.com/implementing-djikstras-shortest-path-algorithm-with-python/)
        shortest_paths = {initial: (None, 0)} #Deklarasi shortest_path
        current_node = initial
        visited = set()

        jarak = 0
        while current_node != end:  #Set Looping
            visited.add(current_node) #Mencatat current_node ke yang sudah dikunjungi 
            destinations = self.graph[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_to_current_node #Penambahan Jarak Destinasi
                if next_node not in shortest_paths: #Kalau next_node tidak di shortest path
                    shortest_paths[next_node] = (current_node, weight)
                else: #Kalau next_node ada di shortest path
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight: #Cek Distance
                        shortest_paths[next_node] = (current_node, weight)

                jarak = weight

            next_destination = {
                node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destination:
                return print("Rute tidak dapat dilacak!")

            current_node = min(next_destination, key=lambda k: next_destination[k][1])

        #Simpulan Singkat
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node= shortest_paths[current_node][0]
            current_node = next_node
            
        path = path[::-1]

        print(f"Rutenya adalah {path} dengan jarak tempuh total {jarak}")


#Additional Method

def mainmenu():
    print("\n--- Graph ---")
    print("1. Masukkan Kota")
    print("2. Masukkan Lintasan")
    print("3. Cari Rute")
    print("0. Exit")
    print("--- ----- ---")


#Execute Class & Method
g = graph()
lanjut = True
while lanjut:
    mainmenu()
    try:
        ask = int(input("Pilih Menu: "))
        if ask == 1:
            temp_kota = str(input("Masukkan Kota: "))
            g.insertVertex(temp_kota)
        
        if ask == 2:
            dari, ke, jarak = [str(x) for x in input("Masukkan Lintasan (Dari, Ke, Jarak): ").split(", ")]
            jarak = int(jarak)
            g.insertEdge(dari, ke, jarak)

        if ask == 3:
            start, goal = [str(y) for y in input("Masukkan Rute (Destinasi Awal, Destinasi Akhir: ").split(", ")]
            g.checkRoute(start, goal)

        if ask == 0:
            quit()
    except ValueError:
        print("Masukkan input dengan Angka!")