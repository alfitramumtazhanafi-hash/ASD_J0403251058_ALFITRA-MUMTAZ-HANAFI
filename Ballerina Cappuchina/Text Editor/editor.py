import os

class TextEditor:
    def __init__(self, filename="dokumen.txt"):
        self.filename = filename
        self.lines = [] 
        self.history_stack = [] 
        self.load_from_file() 

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.lines = [line.strip() for line in file.readlines()]

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            for line in self.lines:
                file.write(line + '\n')

    def simpan_state(self):
        self.history_stack.append(self.lines.copy())

    def tambah_teks(self, teks):
        self.simpan_state()
        self.lines.append(teks)
        self.save_to_file()

    def ubah_teks(self, index, teks_baru):
        if 0 <= index < len(self.lines):
            self.simpan_state()
            self.lines[index] = teks_baru
            self.save_to_file()
            return True
        return False

    def hapus_teks(self, index):
        if 0 <= index < len(self.lines):
            self.simpan_state()
            self.lines.pop(index)
            self.save_to_file()
            return True
        return False

    def undo(self):
        if not self.history_stack:
            return False
        self.lines = self.history_stack.pop()
        self.save_to_file()
        return True