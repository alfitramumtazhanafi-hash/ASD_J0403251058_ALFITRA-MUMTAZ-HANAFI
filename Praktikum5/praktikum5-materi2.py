# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Praktikum 5 - Materi 2 (Tracing Masuk/Keluar)
# ==========================================

def hitung(n):
    # Base case: Kondisi untuk menghentikan rekursi
    if n == 0:
        print("Selesai")
        return
    
    # Fase Stacking (Masuk): Saat fungsi memanggil dirinya sendiri, call stack bertambah.
    print("Masuk:", n)
    
    # Pemanggilan rekursif memperkecil nilai n.
    hitung(n - 1)
    
    # Fase Unwinding (Keluar): Setelah base case tercapai, fungsi kembali satu per satu dan mengeksekusi sisa baris.
    print("Keluar:", n)

hitung(3)