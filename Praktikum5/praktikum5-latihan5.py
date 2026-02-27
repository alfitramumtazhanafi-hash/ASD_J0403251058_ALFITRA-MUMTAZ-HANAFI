# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Latihan 5 (Studi Kasus: Generator PIN)
# ==========================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        # MENCEGAH ANGKA BERULANG (Penyelesaian diskusi)
        # Kita menambahkan pengecekan (Pruning sederhana).
        # Hanya tambahkan angka jika angka tersebut belum ada di dalam string 'hasil'.
        if angka not in hasil:
            buat_pin(panjang, hasil + angka)

buat_pin(3)

# HASIL DISKUSI:
# Bagaimana cara mencegah angka yang sama muncul berulang?
# Jawab: Kita dapat menambahkan kondisi `if angka not in hasil:` sebelum melakukan pemanggilan rekursif.
# Dengan pengecekan ini, jika suatu angka sudah terpilih di iterasi sebelumnya, cabang tersebut tidak akan dilanjutkan, sehingga setiap digit dalam PIN dipastikan unik.