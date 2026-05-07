import os  # mengimpor module os untuk mengecek apakah file ada atau tidak

class TextEditor:
    def __init__(self, filename="dokumen.txt"):
        self.filename = filename
        self.lines = []
        self.history_stack = []
        # TAMBAHKAN BARIS INI: Tempat untuk menyimpan riwayat redo
        self.redo_stack = []  
        self.load_from_file()

    def load_from_file(self):  # method untuk membaca isi file
        if os.path.exists(self.filename):  # mengecek apakah file dengan nama tersebut ada
            with open(self.filename, 'r') as file:  # membuka file dalam mode read (baca)
                self.lines = [line.strip() for line in file.readlines()]  
                # membaca semua baris lalu menghapus spasi/newline di akhir setiap baris

    def save_to_file(self):  # method untuk menyimpan isi list ke file
        with open(self.filename, 'w') as file:  # membuka file dalam mode write (tulis)
            for line in self.lines:  # melakukan perulangan untuk setiap baris teks
                file.write(line + '\n')  # menulis tiap baris ke file dan menambahkan enter

    def simpan_state(self):  # method untuk menyimpan kondisi sebelum perubahan
        self.history_stack.append(self.lines.copy())  
        # menyimpan salinan list lines ke stack agar bisa undo
        self.redo_stack.clear()

    def tambah_teks(self, teks):  # method untuk menambah teks baru
        self.simpan_state()  # menyimpan kondisi sebelum ditambah
        self.lines.append(teks)  # menambahkan teks ke akhir list
        self.save_to_file()  # menyimpan perubahan ke file

    def ubah_teks(self, index, teks_baru):  # method untuk mengubah teks berdasarkan index
        if 0 <= index < len(self.lines):  # memastikan index valid
            self.simpan_state()  # simpan kondisi sebelum diubah
            self.lines[index] = teks_baru  # mengganti isi pada index tertentu
            self.save_to_file()  # simpan hasil perubahan ke file
            return True  # mengembalikan nilai True jika berhasil
        return False  # jika index tidak valid, return False

    def hapus_teks(self, index):  # method untuk menghapus teks berdasarkan index
        if 0 <= index < len(self.lines):  # cek apakah index valid
            self.simpan_state()  # simpan kondisi sebelum dihapus
            self.lines.pop(index)  # menghapus elemen pada index tertentu
            self.save_to_file()  # simpan perubahan ke file
            return True  # berhasil
        return False  # gagal jika index salah

    def undo(self):  # method untuk membatalkan perubahan terakhir
        if not self.history_stack:  # jika stack kosong
            return False  # tidak bisa undo
            
        # 1. SIMPAN DULU state saat ini ke redo_stack (Selamatkan Waktu 3)
        self.redo_stack.append(self.lines.copy())
        
        # 2. BARU ambil state masa lalu dari history (Panggil Waktu 2)
        self.lines = self.history_stack.pop()  
        
        self.save_to_file()  # simpan hasil undo ke file
        return True  # undo berhasil

    # [BARU] Method untuk mengembalikan perubahan yang di-undo (Redo)
    # Pastikan method redo ini ada di bagian paling bawah class TextEditor
    def undo(self):
        if not self.history_stack:
            return False
        
        self.redo_stack.append(self.lines.copy())
        self.lines = self.history_stack.pop()  
        self.save_to_file()
        return True

    def redo(self):
        if not self.redo_stack:  # jika stack redo kosong
            return False  # tidak ada aksi yang bisa di-redo
            
        # Simpan state saat ini ke history_stack (undo) agar kita bisa membatalkan redo ini jika perlu
        self.history_stack.append(self.lines.copy())
        
        # Ambil state dari masa depan (redo)
        self.lines = self.redo_stack.pop()
        self.save_to_file()  # simpan hasil redo ke file
        return True  # redo berhasil

        # [BARU] Method untuk mencari kata/keyword di dalam teks
    def cari_teks(self, keyword):
        hasil_pencarian = []  # List untuk menyimpan nomor baris dan teksnya
        total_kemunculan = 0  # Variabel untuk menghitung total kata yang ditemukan
        
        # Mengubah keyword menjadi huruf kecil agar pencarian tidak sensitif huruf besar/kecil (case-insensitive)
        keyword_lower = keyword.lower()
        
        # Melakukan Linear Search: mengecek dari baris pertama sampai akhir
        for i, baris in enumerate(self.lines):
            baris_lower = baris.lower() # Ubah baris ke huruf kecil juga
            
            # Jika keyword ada di dalam baris tersebut
            if keyword_lower in baris_lower:
                # Menghitung ada berapa banyak kata tersebut di baris ini
                jumlah_di_baris = baris_lower.count(keyword_lower)
                total_kemunculan += jumlah_di_baris
                
                # Menyimpan nomor baris (i+1) dan isi teks aslinya ke dalam list hasil
                hasil_pencarian.append((i + 1, baris))
                
        # Mengembalikan 2 nilai sekaligus: total kemunculan dan list detail barisnya
        return total_kemunculan, hasil_pencarian