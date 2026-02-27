# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Latihan 1 (Rekursi Pangkat)
# ==========================================

def pangkat(a, n):
    # Base case: Setiap bilangan yang dipangkatkan 0 hasilnya adalah 1.
    if n == 0:
        return 1
    
    # Recursive case: Mengalikan angka dasar (a) dengan hasil dari pangkat(a, n-1).
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # Output: 16

# HASIL DISKUSI ALUR PROGRAM:
# 1. Program memanggil pangkat(2, 4). Karena n bukan 0, program mengembalikan 2 * pangkat(2, 3).
# 2. Proses ini berulang (recursive call) hingga pangkat(2, 0).
# 3. Saat mencapai pangkat(2, 0), kondisi base case terpenuhi dan mengembalikan nilai 1.
# 4. Nilai 1 dikalikan mundur ke atas (unwinding): 1 * 2 * 2 * 2 * 2 sehingga menghasilkan 16.