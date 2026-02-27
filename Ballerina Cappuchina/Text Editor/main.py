from editor import TextEditor

def main():
    editor = TextEditor()

    while True:
        print("\n=== APLIKASI EDITOR TEKS SEDERHANA ===")
        print("1. Lihat Teks")
        print("2. Tambah Teks")
        print("3. Ubah Teks")
        print("4. Hapus Teks")
        print("5. Undo Perubahan Terakhir")
        print("0. Keluar")
        
        pilihan = input("Pilih menu (0-5): ")

        if pilihan == '1':
            print("\n--- Isi Dokumen ---")
            if not editor.lines:
                print("(Dokumen kosong)")
            else:
                for i, baris in enumerate(editor.lines):
                    print(f"[{i+1}] {baris}")
            print("-------------------")

        elif pilihan == '2':
            teks = input("Masukkan teks baru: ")
            editor.tambah_teks(teks)
            print("[Sukses] Teks berhasil ditambahkan.")

        elif pilihan == '3':
            try:
                # User biasanya menghitung dari 1, sedangkan index Python dari 0
                idx = int(input("Masukkan nomor baris yang ingin diubah: ")) - 1
                teks_baru = input("Masukkan teks pengganti: ")
                if editor.ubah_teks(idx, teks_baru):
                    print("[Sukses] Teks berhasil diubah.")
                else:
                    print("[Error] Nomor baris tidak ditemukan!")
            except ValueError:
                print("[Error] Harap masukkan angka yang valid!") # Validasi input 

        elif pilihan == '4':
            try:
                idx = int(input("Masukkan nomor baris yang ingin dihapus: ")) - 1
                if editor.hapus_teks(idx):
                    print("[Sukses] Teks berhasil dihapus.")
                else:
                    print("[Error] Nomor baris tidak ditemukan!")
            except ValueError:
                print("[Error] Harap masukkan angka yang valid!") # Validasi input 

        elif pilihan == '5':
            if editor.undo():
                print("[Sukses] Undo berhasil. Mengembalikan state sebelumnya.")
            else:
                print("[Info] Tidak ada riwayat untuk di-undo.")

        elif pilihan == '0':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("[Error] Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()