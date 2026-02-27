# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Latihan 2 (Tracing Rekursi)
# ==========================================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)

countdown(3)

# HASIL DISKUSI:
# Mengapa output 'Keluar' muncul terbalik?
# Jawab: Karena fungsi rekursif menggunakan struktur data Call Stack (LIFO - Last In First Out). 
# Eksekusi fungsi `print("Keluar:", n)` tertunda selama fungsi memanggil dirinya sendiri (Stacking).
# Baris tersebut baru dieksekusi saat program mengurai fungsi dari tumpukan memori (Unwinding) setelah mencapai base case (n=0). Oleh karena itu, fungsi yang terakhir masuk ke stack (n=1) akan menjadi yang pertama keluar dan dieksekusi.