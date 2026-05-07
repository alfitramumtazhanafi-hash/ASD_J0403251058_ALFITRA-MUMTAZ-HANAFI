import re  # [BARU] Modul bawaan Python untuk memanipulasi teks (Regex)
import time  # [BARU] Untuk mengatur jeda waktu antar huruf
import sys   # [BARU] Untuk memunculkan huruf satu per satu
import os    # [BARU] Untuk membersihkan layar terminal
# Mengimpor kelas TextEditor dari modul (file) editor.py yang berada di folder yang sama
from editor import TextEditor

def intro_animation():
    # Membersihkan layar terminal (cls untuk Windows, clear untuk Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Teks yang mau ditampilkan
    teks_intro = "=== SELAMAT DATANG DI APLIKASI TEKS EDITOR ===\n      Memuat sistem memori dan riwayat...\n"
    
    # Looping untuk memunculkan teks huruf demi huruf (efek mesin tik)
    for huruf in teks_intro:
        sys.stdout.write(huruf)
        sys.stdout.flush() # Memaksa terminal segera menampilkan hurufnya
        time.sleep(0.04)   # Kecepatan ketikan (0.04 detik per huruf)
        
    print("\n") # Memberi jarak enter
    time.sleep(1) # Jeda 1 detik sebelum masuk ke menu utama agar tidak terlalu cepat hilang

# Mendefinisikan fungsi utama untuk menjalankan jalannya aplikasi
def main():
    intro_animation()
    # Membuat objek (instance) dari kelas TextEditor dan menyimpannya ke dalam variabel 'editor'
    editor = TextEditor()

    # Memulai perulangan tak terbatas agar menu terus berulang sampai user memilih untuk keluar
    while True:
        # Mencetak judul aplikasi ke layar
        print("\n=== APLIKASI EDITOR TEKS SEDERHANA ===")
        # Menampilkan daftar opsi menu yang bisa dipilih oleh pengguna
        print("1. Lihat Teks")
        print("2. Tambah Teks")
        print("3. Ubah Teks")
        print("4. Hapus Teks")
        print("5. Undo Perubahan Terakhir")
        print("6. Redo Perubahan Terakhir")
        print("7. Cari Teks")
        print("0. Keluar")
        
        # Meminta input dari pengguna berupa teks/angka dan menyimpannya di variabel 'pilihan'
        pilihan = input("Pilih menu (0-7): ")

        # --- BLOK MENU 1: LIHAT TEKS ---
        # Mengecek apakah input yang dimasukkan pengguna adalah string '1'
        if pilihan == '1':
            # Mencetak batas atas untuk tampilan isi dokumen
            print("\n--- Isi Dokumen ---")
            # Mengecek apakah variabel list 'lines' di dalam objek editor dalam keadaan kosong
            if not editor.lines:
                # Jika kosong, tampilkan informasi bahwa dokumen tidak memiliki isi
                print("(Dokumen kosong)")
            # Jika dokumen memiliki isi teks
            else:
                # Melakukan iterasi (perulangan) pada isi teks, mengambil indeks (i) dan teksnya (baris)
                for i, baris in enumerate(editor.lines):
                    # Menampilkan nomor baris (indeks i ditambah 1 karena user melihat dari angka 1) beserta isi teksnya
                    print(f"[{i+1}] {baris}")
            # Mencetak batas bawah untuk tampilan isi dokumen
            print("-------------------")

        # --- BLOK MENU 2: TAMBAH TEKS ---
        # Mengecek apakah input yang dimasukkan pengguna adalah string '2'
        elif pilihan == '2':
            # Meminta pengguna untuk memasukkan teks baru
            teks = input("Masukkan teks baru: ")
            # Memanggil metode 'tambah_teks' dari objek editor untuk memasukkan teks tersebut ke dalam memori
            editor.tambah_teks(teks)
            # Menampilkan pesan bahwa proses penambahan teks berhasil
            print("[Sukses] Teks berhasil ditambahkan.")

        # --- BLOK MENU 3: UBAH TEKS ---
        # Mengecek apakah input yang dimasukkan pengguna adalah string '3'
        elif pilihan == '3':
            # Menggunakan blok try-except untuk menangani potensi error (misal: user memasukkan huruf, bukan angka)
            try:
                # Meminta input nomor baris, mengonversinya ke integer (bilangan bulat), dan dikurangi 1 (karena indeks list Python dimulai dari 0)
                idx = int(input("Masukkan nomor baris yang ingin diubah: ")) - 1
                # Meminta pengguna untuk memasukkan teks baru sebagai penggantinya
                teks_baru = input("Masukkan teks pengganti: ")
                # Memanggil metode 'ubah_teks'. Jika mengembalikan nilai True (berhasil diubah), maka jalankan blok ini
                if editor.ubah_teks(idx, teks_baru):
                    # Menampilkan pesan bahwa pengubahan teks berhasil
                    print("[Sukses] Teks berhasil diubah.")
                # Jika metode 'ubah_teks' mengembalikan False (misal karena indeks yang dimasukkan di luar batas)
                else:
                    # Menampilkan pesan error
                    print("[Error] Nomor baris tidak ditemukan!")
            # Menangkap error jika pengguna memasukkan karakter yang tidak bisa diubah menjadi angka (integer)
            except ValueError:
                # Menampilkan pesan teguran agar pengguna memasukkan angka yang valid
                print("[Error] Harap masukkan angka yang valid!") 

        # --- BLOK MENU 4: HAPUS TEKS ---
        # Mengecek apakah input yang dimasukkan pengguna adalah string '4'
        elif pilihan == '4':
            # Menggunakan blok try-except untuk validasi input angka seperti pada menu 3
            try:
                # Meminta input nomor baris yang akan dihapus, lalu dikonversi ke integer dan dikurangi 1
                idx = int(input("Masukkan nomor baris yang ingin dihapus: ")) - 1
                # Memanggil metode 'hapus_teks'. Jika baris berhasil dihapus (return True):
                if editor.hapus_teks(idx):
                    # Tampilkan pesan sukses
                    print("[Sukses] Teks berhasil dihapus.")
                # Jika baris gagal dihapus (return False / indeks tidak ditemukan):
                else:
                    # Tampilkan pesan error
                    print("[Error] Nomor baris tidak ditemukan!")
            # Menangkap error tipe data jika input bukan angka
            except ValueError:
                # Tampilkan pesan teguran
                print("[Error] Harap masukkan angka yang valid!") 

        # --- BLOK MENU 5: UNDO ---
        # Mengecek apakah input yang dimasukkan pengguna adalah string '5'
        elif pilihan == '5':
            # Memanggil metode 'undo'. Jika ada riwayat yang berhasil dikembalikan (return True):
            if editor.undo():
                # Tampilkan pesan sukses bahwa state/kondisi aplikasi telah kembali ke sebelumnya
                print("[Sukses] Undo berhasil. Mengembalikan state sebelumnya.")
            # Jika tidak ada riwayat yang tersimpan (return False):
            else:
                # Tampilkan pesan informasi bahwa undo tidak bisa dilakukan
                print("[Info] Tidak ada riwayat untuk di-undo.")

        elif pilihan == '6':
            # Memanggil metode 'redo'. Jika ada riwayat yang berhasil dikembalikan (return True):
            if editor.redo():
                # Tampilkan pesan sukses bahwa state/kondisi aplikasi telah kembali ke sebelumnya
                print("[Sukses] Redo berhasil. Mengembalikan state ke depan.")
            # Jika tidak ada riwayat yang tersimpan (return False):
            else:
                # Tampilkan pesan informasi bahwa redo tidak bisa dilakukan
                print("[Info] Tidak ada riwayat untuk di-redo.")

        # ... (kode elif pilihan == '6' yang sebelumnya) ...

        # --- BLOK MENU 7: CARI TEKS ---
        elif pilihan == '7':
            # Meminta user memasukkan kata kunci
            keyword = input("Masukkan kata kunci yang ingin dicari: ")
            
            # Jika user tidak memasukkan apa-apa
            if not keyword.strip():
                print("[Error] Kata kunci tidak boleh kosong.")
                continue

            # Memanggil fungsi cari_teks dari backend
            total, hasil = editor.cari_teks(keyword)
            
            print("\n--- Hasil Pencarian ---")
            if total > 0:
                print(f"[Info] Kata '{keyword}' ditemukan sebanyak {total} kali.")
                print("Terdapat pada baris:")
                
                # Looping untuk menampilkan detail nomor baris dan isinya
                for nomor, teks in hasil:
                    # [BARU] Logika Highlight Warna
                    # \033[43m : Background Kuning
                    # \033[30m : Teks Hitam (supaya kontras)
                    # \033[0m  : Reset warna kembali ke normal
                    # re.sub akan mencari kata dan mengapitnya dengan kode warna tersebut
                    teks_berwarna = re.sub(
                        f"(?i)({re.escape(keyword)})", 
                        r"\033[43m\033[30m\1\033[0m", 
                        teks
                    )
                    
                    # Tampilkan teks yang sudah di-highlight
                    print(f"[{nomor}] {teks_berwarna}")
            else:
                print(f"[Info] Kata '{keyword}' tidak ditemukan di dalam dokumen.")
            print("-----------------------")

        # --- BLOK MENU 0: KELUAR ---
        # Mengecek apakah input yang dimasukkan pengguna adalah string '0'
        elif pilihan == '0':
            # Mencetak pesan perpisahan
            print("Terima kasih telah menggunakan aplikasi ini!")
            # Perintah 'break' akan secara paksa menghentikan perulangan 'while True', sehingga aplikasi selesai/tutup
            break
            
        # --- BLOK VALIDASI ---
        # Jika input yang dimasukkan user bukan '0', '1', '2', '3', '4', atau '5'
        else:
            # Menampilkan pesan bahwa input tidak dikenali
            print("[Error] Pilihan tidak valid. Silakan coba lagi.")

# Blok pengecekan ini memastikan bahwa fungsi main() hanya dijalankan jika file ini dieksekusi secara langsung (bukan diimpor oleh file Python lain)
if __name__ == "__main__":
    # Memanggil fungsi main() untuk pertama kali agar program berjalan
    main()