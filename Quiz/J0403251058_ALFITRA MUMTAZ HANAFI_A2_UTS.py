# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : ALFITRA MUMTAZ HANAFI
# NIM     : J0403251058
# Kelas   : A2
# ==============================================================================

import os

# ==========================================
# 1. FILE HANDLING & ADT (DICTIONARY)
# ==========================================
def baca_data_buku(nama_file):
    katalog_buku = {} 
    
    # Memaksa pencarian file di folder yang persis sama  dengan lokasi file python
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.join(base_dir, nama_file)
    
    try:
        with open(path_file, 'r') as file:
            for baris in file:
                data = baris.strip().split(',')
                if len(data) >= 3: 
                    kode = data[0].strip()   
                    judul = data[1].strip()  
                    harga = int(data[2].strip()) 
                    
                    katalog_buku[kode] = {'judul': judul, 'harga': harga}
        print(f"[Sukses] Data berhasil dimuat dari {path_file}")
    except FileNotFoundError:
        print(f"[Error] File {nama_file} TIDAK DITEMUKAN di lokasi: {path_file}")
    
    return katalog_buku

# ==========================================
# 2. SINGLE LINKED LIST - MANAJEMEN STOK PROMO
# ==========================================
# Class untuk membuat struktur Node penyusun Linked List
class Node:
    def __init__(self, judul):
        self.judul = judul # Menyimpan data judul buku ke dalam node
        self.next = None   # Pointer yang menunjuk ke node selanjutnya (awalnya kosong)

# Class untuk mengelola operasi Linked List
class LinkedListPromo:
    def __init__(self):
        self.head = None # Head adalah titik awal dari linked list (awalnya list kosong)

    def tambah_promo(self, judul):
        """Fungsi untuk menambahkan buku promo baru ke posisi paling akhir (tail) Linked List."""
        node_baru = Node(judul) # Membuat node baru dari judul yang diinput
        
        # Kondisi 1: Jika list masih kosong, node baru langsung menjadi head (kepala)
        if self.head is None:
            self.head = node_baru 
        # Kondisi 2: Jika sudah ada isinya, cari node paling ujung
        else:
            current = self.head
            # Berjalan menelusuri node sampai menemukan node yang pointer 'next'-nya kosong
            while current.next is not None:
                current = current.next
            # Sambungkan node terakhir tersebut dengan node baru
            current.next = node_baru 
        print(f"[Sukses] Buku '{judul}' ditambahkan ke daftar promo.")

    def tampilkan_promo(self):
        """Fungsi untuk menampilkan seluruh isi Linked List dari head sampai tail."""
        print("\n--- Daftar Buku Promo ---")
        if self.head is None:
            print("Daftar promo saat ini kosong.")
        else:
            current = self.head
            nomor = 1
            # Looping berjalan selama current node memiliki isi
            while current is not None:
                print(f"{nomor}. {current.judul}")
                current = current.next # Memindahkan kursor ke node selanjutnya
                nomor += 1

# ==========================================
# 3. QUEUE - ANTREAN PELANGGAN (FIFO)
# ==========================================
class QueueKasir:
    def __init__(self):
        self.antrean = [] # Menggunakan list bawaan Python sebagai representasi antrean

    def tambah_antrean(self, nama):
        """Fungsi untuk menambahkan pelanggan ke dalam antrean (Enqueue)."""
        # Append akan otomatis menaruh data di indeks paling belakang
        self.antrean.append(nama) 
        print(f"[Queue] Pelanggan '{nama}' masuk ke barisan antrean.")

    def layani_pelanggan(self):
        """Fungsi untuk melayani dan menghapus pelanggan dari baris terdepan (Dequeue)."""
        if len(self.antrean) == 0:
            print("[Queue] Antrean kosong, kasir sedang menganggur.")
        else:
            # Pop(0) akan mengambil dan menghapus elemen di indeks ke-0 (paling depan / FIFO)
            pelanggan_dilayani = self.antrean.pop(0) 
            print(f"[Queue] Melayani pelanggan: '{pelanggan_dilayani}'. Sisa antrean: {len(self.antrean)}")

# ==========================================
# 4. SORTING - LAPORAN PENJUALAN
# ==========================================
def insertion_sort_manual(arr):
    """
    Fungsi untuk mengurutkan List secara manual menggunakan algoritma Insertion Sort.
    Data diurutkan dari yang terkecil ke terbesar (Ascending).
    """
    # Melakukan perulangan mulai dari elemen kedua (indeks 1) sampai akhir list
    for i in range(1, len(arr)):
        key = arr[i] # Elemen yang saat ini sedang dicari posisi benarnya
        j = i - 1
        
        # Geser elemen-elemen di sebelah kiri 'key' yang lebih besar dari 'key'
        # ke kanan sebanyak 1 posisi
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Tempatkan 'key' di posisi kosong yang sudah tepat
        arr[j + 1] = key
        
    return arr

# ==========================================
# PROGRAM UTAMA (MAIN MENU)
# ==========================================
def main():
    # menjalankan struktur data yang sudah dibuat
    file_db = "buku.txt" # Nama file yang akan dibaca
    katalog = baca_data_buku(file_db) # Memanggil fungsi baca file
    promo_list = LinkedListPromo()    # Membuat objek Linked List
    kasir_queue = QueueKasir()        # Membuat objek Queue
    
    #data transaksi dari ketentuan yang ada di pdf
    data_transaksi = [150000, 50000, 200000, 75000, 120000]

    # Looping menu utama agar program terus berjalan sampai user memilih Keluar
    while True:
        print("\n======================================")
        print(" SISTEM MANAJEMEN TOKO BUKU ")
        print("======================================")
        print("1. Tampilkan Katalog Buku (Dictionary)")
        print("2. Manajemen Buku Promo (Linked List)")
        print("3. Manajemen Antrean Kasir (Queue)")
        print("4. Urutkan Laporan Penjualan (Sorting)")
        print("5. Keluar")
        print("======================================")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\n--- Katalog Buku ---")
            if not katalog:
                print("Katalog kosong atau file gagal dibaca.")
            else:
                # Mengeluarkan data dari dalam Dictionary
                for kode, info in katalog.items():
                    print(f"Kode: {kode} | Judul: {info['judul']} | Harga: Rp{info['harga']}")
                    
        elif pilihan == '2':
            print("\n1. Tambah Buku Promo")
            print("2. Tampilkan Daftar Promo")
            sub_pilih = input("Pilih aksi: ")
            if sub_pilih == '1':
                judul_baru = input("Masukkan judul buku promo: ")
                promo_list.tambah_promo(judul_baru) # Memanggil fungsi Enqueue promo
            elif sub_pilih == '2':
                promo_list.tampilkan_promo() # Menampilkan isi Linked list
            else:
                print("Pilihan tidak valid.")
                
        elif pilihan == '3':
            print("\n1. Tambah Pelanggan ke Antrean")
            print("2. Layani Pelanggan")
            sub_pilih = input("Pilih aksi: ")
            if sub_pilih == '1':
                nama = input("Masukkan nama pelanggan: ")
                kasir_queue.tambah_antrean(nama) # Memasukkan ke antrean
            elif sub_pilih == '2':
                kasir_queue.layani_pelanggan() # Melayani/menghapus dari antrean
            else:
                print("Pilihan tidak valid.")

        elif pilihan == '4':
            print("\n--- Laporan Penjualan ---")
            print(f"Data Transaksi Awal  : {data_transaksi}")
            
            # Melakukan .copy() agar data list original tidak tertimpa/hilang
            data_diurutkan = data_transaksi.copy() 
            hasil_sort = insertion_sort_manual(data_diurutkan) # Memanggil fungsi sorting manual
            
            print(f"Data Setelah Diurutkan: {hasil_sort}")

        elif pilihan == '5':
            print("Keluar dari program. Terima kasih!")
            break # Menghentikan looping while, program selesai
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# memastikan program utama dieksekusi pertama kali
if __name__ == "__main__":
    main()