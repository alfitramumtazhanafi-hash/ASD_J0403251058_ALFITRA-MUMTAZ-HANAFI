#membuka file dalam satu string
print("Membuka File dalam satu string")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
    print(isi_file)

print("Tipe Data:", type(isi_file))


#membuka file per baris
print("Membuka File per Baris")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan karakter newline
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)

#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
         baris = baris.strip() #menghilangkan karakter newline
         nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
         print("NIM:", nim, "| Nama:", nama, "| Nilai:", nilai)

data_list = []

#============================================================================
#PRAKTIKUM 1: Konsep ADT dan File Handling
#LATIHAN DASAR 3: Membaca data dan menyimpannya ke dalam struktur data list
#============================================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        data_list.append({"NIM": nim, "Nama": nama, "Nilai": nilai}) #menyimpan data
print("===Menampilakn List===")
print(data_list)
print("Contoh record ke-1", data_list[0])
print("Contoh record ke-2", data_list[1])

print("Jumlah record:", len(data_list))

#============================================================================
#PRAKTIKUM 1: Konsep ADT dan File Handling
#LATIHAN DASAR 4: Membaca data dan menyimpannya ke dalam struktur data dictionary
#============================================================================
data_dict = {}

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        #simpan data ke dictionary dengan NIM sebagai key
        data_dict[nim] = {
            "Nama": nama,
            "Nilai": nilai
            }
print("===Menampilkan Data Dictionary===") 
print(data_dict)