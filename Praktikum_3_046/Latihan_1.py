import tkinter as tk

# Stack untuk menyimpan history teks
undo_stack = []

def on_key_press(event):
    # Simpan state sebelum perubahan
    undo_stack.append(text_editor.get("1.0", tk.END))

def undo():
    if undo_stack:
        last_state = undo_stack.pop()
        text_editor.delete("1.0", tk.END)
        text_editor.insert(tk.END, last_state)

# Membuat window
root = tk.Tk()
root.title("Editor Teks Sederhana dengan Undo")

# Membuat Text widget
text_editor = tk.Text(root, width=50, height=20)
text_editor.pack()

# Bind tombol untuk menyimpan state
text_editor.bind("<Key>", on_key_press)

# Tombol Undo
undo_button = tk.Button(root, text="Undo", command=undo)
undo_button.pack()

root.mainloop()
