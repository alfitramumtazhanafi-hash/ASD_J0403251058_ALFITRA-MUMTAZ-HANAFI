# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Praktikum 5 - Materi 1 (Faktorial)
# ==========================================

# Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri.
def faktorial(n):
    # Base case: Kondisi berhenti agar fungsi tidak berjalan terus-menerus.
    # Berhenti ketika n mencapai 0.
    if n == 0:
        return 1
    
    # Recursive case: Pemanggilan fungsi ke dirinya sendiri dengan ukuran masalah yang diperkecil (n-1).
    return n * faktorial(n - 1)

print(faktorial(5)) # Output: 120