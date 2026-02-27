# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Latihan 4 (Kombinasi Huruf)
# ==========================================

def kombinasi(n, hasil=""):
    # Base case
    if len(hasil) == n:
        print(hasil)
        return
    
    # Explore kombinasi
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)

# HASIL DISKUSI:
# Bagaimana jumlah kombinasi yang dihasilkan?
# Jawab: Jumlah kombinasi yang dihasilkan mengikuti rumus 2^n (dua pangkat n), di mana 2 adalah jumlah kemungkinan huruf (A dan B), dan n adalah panjang karakter.
# Untuk kombinasi(2), jumlah kombinasi yang dihasilkan adalah 2^2 = 4 kombinasi (AA, AB, BA, BB).