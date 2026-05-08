# Menentukan jumlah node (V = 4 yaitu node 0, 1, 2, 3)
V = 4

# Mendefinisikan list of edges berdasarkan gambar graph di PDF
edges = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3]] 

# Membuat matriks 4x4 yang diisi dengan angka 0 terlebih dahulu
mat = [[0 for _ in range(V)] for _ in range(V)]

# Melakukan perulangan untuk setiap pasang titik (u, v) di dalam edges
for u, v in edges:
    # Mengisi baris u kolom v dengan angka 1 (menandakan ada jalan/hubungan)
    mat[u][v] = 1
    # Mengisi baris v kolom u dengan angka 1 karena graph ini undirected (bolak-balik)
    mat[v][u] = 1

# Mencetak teks header ke layar
print("Adjacency Matrix Praktikum 1:")

# Melakukan perulangan untuk mencetak setiap baris matriks ke layar
for row in mat:
    print(row)