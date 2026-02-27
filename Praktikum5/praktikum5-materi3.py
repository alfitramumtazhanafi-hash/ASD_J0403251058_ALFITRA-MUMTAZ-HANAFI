# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Praktikum 5 - Materi 3 (Menjumlahkan Elemen List)
# ==========================================

# Rekursi digunakan untuk memproses data list secara bertahap dengan menggeser indeks.
def jumlah_list(data, index=0):
    # Base case: Berhenti jika nilai index sudah sama dengan panjang list (artinya semua elemen sudah dicek).
    if index == len(data):
        return 0
    
    # Recursive case: Menambahkan elemen saat ini dengan hasil penjumlahan elemen-elemen setelahnya.
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2, 4, 6, 8])) # Output: 20