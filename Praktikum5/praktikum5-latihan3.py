# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Latihan 3 (Mencari Nilai Maksimum)
# ==========================================

def cari_maks(data, index=0):
    # Base case: Jika index berada di posisi elemen terakhir, kembalikan elemen tersebut.
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case: Mencari nilai maksimum pada sisa list setelah index saat ini.
    maks_sisa = cari_maks(data, index + 1)
    
    # Membandingkan nilai elemen saat ini dengan nilai maksimum dari sisa list.
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

# HASIL DISKUSI ALUR PROGRAM:
# 1. Program memecah list dengan mengecek indeks satu per satu hingga mencapai elemen terakhir (base case).
# 2. Setelah mencapai elemen terakhir (angka 5), program akan melakukan perbandingan berpasangan (unwinding).
# 3. Membandingkan 9 dan 5 -> max 9. Lalu membandingkan 2 dan 9 -> max 9. Membandingkan 7 dan 9 -> max 9. Membandingkan 3 dan 9 -> max 9.
# 4. Hasil akhirnya, nilai terbesar yang dikembalikan ke pemanggil pertama adalah 9.