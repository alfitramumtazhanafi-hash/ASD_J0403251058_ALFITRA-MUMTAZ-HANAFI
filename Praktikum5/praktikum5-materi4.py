# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Praktikum 5 - Materi 4 (Kombinasi Biner)
# ==========================================

# Backtracking adalah teknik pencarian solusi dengan mencoba berbagai kemungkinan (Choose, Explore, Unchoose).
def biner(n, hasil=""):
    # Base case: Jika panjang string hasil sudah mencapai n, maka cetak hasil dan berhenti.
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore: Mencoba menambahkan angka '0' ke dalam hasil.
    biner(n, hasil + "0")
    
    # Choose + Explore: Mencoba menambahkan angka '1' ke dalam hasil.
    biner(n, hasil + "1")

biner(3)