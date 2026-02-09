# ==========================================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat Fungsi Load Data
#===========================================================================================

#variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        return data_dict

    parts = content.split(",")
    # If file is a single long comma-separated stream (no newlines)
    if len(parts) >= 3 and len(parts) % 3 == 0:
        for i in range(0, len(parts), 3):
            nim = parts[i].strip()
            nama = parts[i + 1].strip()
            try:
                nilai = int(parts[i + 2].strip())
            except ValueError:
                continue
            data_dict[nim] = {"nama": nama, "nilai": nilai}
        return data_dict

    # Otherwise try parsing line by line (handles names containing commas using maxsplit)
    for baris in content.splitlines():
        baris = baris.strip()
        if not baris:
            continue
        parts = baris.split(",", 2)
        if len(parts) < 3:
            continue
        nim = parts[0].strip()
        nama = parts[1].strip()
        try:
            nilai = int(parts[2].strip())
        except ValueError:
            continue
        data_dict[nim] = {"nama": nama, "nilai": nilai}

    return data_dict


buka_data = baca_data(nama_file)
print("jumlah data terbaca", len(buka_data))

# ==========================================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 2: Membuat Fungsi Menampilkan Data
#===========================================================================================

def tampilkan_data(data_dict):
    #Membuat header tabel 
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' : <10} | {'NAMA' : <12} | {'NILAI' : >5}")
    '''
    
    untuk tampilan yang rapi, atur lebar kolom
    {'NIM' : <10} artinya nim rata kiri dengan lebar kolom 10 karakter
    {'NAMA' : <12} artinya nama rata kiri dengan lebar kolom 12 karakter
    {'NILAI' : >5} artinya nilai rata kanan dengan lebar kolom 5 karakter
    '''
    print("-"*35) #MEMBUAT GARIS

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) : >5}")

tampilkan_data(buka_data) #memanggil fungsi tampilkan data


# ==========================================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3: Membuat Fungsi Mencari Data
#===========================================================================================

def cari_data(data_dict) :
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]


        print("==== Data Mahasiswa Ditemukan ====")
        print(f"NIM: {nim_cari}")
        print(f"NAMA: {nama}")
        print(f"NILAI: {nilai}")
    else :
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")

# ==========================================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4: Membuat Fungsi Update Data
#===========================================================================================

#MEMBUAT FUNGSI UPDATE DATA
def update_data(data_dict):

    #awali dulu dengan mencari data yang akan diubah
    NIM = input("Masukkan NIM mahasiswa yang akan diubah datanya: ").strip()

    if NIM not in data_dict :
        print("NIM tidak ditemmukan. Update dibatalkan")
        return 
    
    nilai_baru_str = input("masukkan nilai baru 0-100 : ").strip()
    try:
        nilai_baru = int(input("masukkan nilai baru 0-100 : ")).strip()
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. Update dibatalkan")
        return

    nilai_lama = data_dict[NIM]["nilai"]
    data_dict[NIM]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {NIM} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi update data
    update_data(buka_data)

# ==========================================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5: Membuat Fungsi Menyimpan Data ke File
#===========================================================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}")

#Memanggil fungsi simpan data
simpan_data(nama_file, buka_data)
print("\nData berhasil disimpan ke file", nama_file)

# ==========================================================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6: Membuat Fungsi Menu Interaktif
#===========================================================================================

def main():
    #mload data otomatis saat program dimulai
    data_mahasiswa = baca_data(nama_file) 

    while True:
        print("\n=== MENU UTAMA ===")    
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Simpan Data dan Keluar")
        print("0. Keluar")
        pilihan = input("Pilih menu (1-4): ").strip()
    
        if pilihan == "1":
            tampilkan_data(data_mahasiswa)
        elif pilihan == "2":
            cari_data(data_mahasiswa)
        elif pilihan == "3":
            update_data(data_mahasiswa)
        elif pilihan == "4":
            simpan_data(nama_file, data_mahasiswa)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")