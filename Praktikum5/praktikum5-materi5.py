# ==========================================
# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2 - Teknologi Rekayasa Perangkat Lunak
# Topik : Praktikum 5 - Materi 5 (Batas '1' - Pruning)
# ==========================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: Menghentikan eksplorasi cabang yang pasti tidak memenuhi syarat agar lebih efisien.
    # Jika jumlah angka 1 sudah melebihi batas, langsung hentikan proses (return).
    if jumlah_1 > batas:
        return
    
    # Base case: Jika panjang string sudah mencapai n.
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih '0': Jumlah angka '1' tidak bertambah.
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Pilih '1': Jumlah angka '1' bertambah.
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)