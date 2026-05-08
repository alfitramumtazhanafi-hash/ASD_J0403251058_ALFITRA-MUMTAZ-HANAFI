# Mendefinisikan matriks input sesuai dengan soal di modul
matrix_input = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

# Menyiapkan dictionary kosong untuk menyimpan hasil konversi adjacency list
adj_list = {}

# Melakukan perulangan sebanyak jumlah baris pada matriks (yaitu 4 kali)
for i in range(len(matrix_input)):
    # Menyiapkan list kosong untuk menampung tetangga dari node ke-i
    neighbors = []
    # Melakukan perulangan sebanyak jumlah elemen di dalam baris tersebut
    for j in range(len(matrix_input[i])):
        # Mengecek jika nilai pada baris i dan kolom j adalah 1 (ada edge)
        if matrix_input[i][j] == 1:
            # Menambahkan index kolom (j) ke dalam list tetangga karena mereka terhubung
            neighbors.append(j)
    # Menyimpan list tetangga yang sudah terkumpul ke dalam dictionary dengan kunci node ke-i
    adj_list[i] = neighbors

# Mencetak header ke layar
print("\nHasil Konversi (Praktikum 3):")
# Melakukan perulangan untuk menampilkan hasil akhir dari adjacency list
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")