# Nama  : Alfitra Mumtaz Hanafi
# NIM   : J0403251058
# Kelas : A/P2
# Materi: Latihan Soal Pengurutan - Seleksi Kandidat

def seleksiKandidat(skor_awal):
    # Menyimpan skor beserta nomor kandidat aslinya (index + 1)
    data_kandidat = []
    for i in range(len(skor_awal)):
        data_kandidat.append({"nomor": i + 1, "skor": skor_awal[i]})
        
    # Mengurutkan data secara descending (menggunakan Bubble Sort)
    for passnum in range(len(data_kandidat)-1, 0, -1):
        for i in range(passnum):
            if data_kandidat[i]["skor"] < data_kandidat[i+1]["skor"]:
                # Tukar posisi
                temp = data_kandidat[i]
                data_kandidat[i] = data_kandidat[i+1]
                data_kandidat[i+1] = temp
                
    return data_kandidat

# Data skor akademik awal
skor = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# Panggil fungsi
hasil_seleksi = seleksiKandidat(skor)

print("=== HASIL SELEKSI 5 KANDIDAT TERBAIK ===")
# Menampilkan 5 teratas
for i in range(5):
    print(f"Peringkat {i+1}: Kandidat ke-{hasil_seleksi[i]['nomor']} dengan skor {hasil_seleksi[i]['skor']}")