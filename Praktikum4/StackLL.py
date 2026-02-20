#=====================================================
#Nama   : Alfitra Mumtaz Hanafi
#NIM    : J0403251058
#Kelas  : TPL A/P2
#=====================================================

#=====================================================
#Implementasi Dasar : Stack
#=====================================================

class Node:
    #Konstruktor yang dijalankan scr otomatis ketika class node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjukan ke note berikutnya (awal=none)


#stack ada operasi push(memasukkan head baru) dan pop (menghapus head)
#  B-> C->None

class stack:
    def __init__(self):
        self.top = None #Top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None
    def push(self, data):
        #1 membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pada class Node
        
        #2 Node baru menunjuk ke top yang lama
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

    def pop(self): #mengambil/menghapus node paling atas
        
        if self.is_empty():
            print("Stack Kosong, Tidak Bisa Pop")
            return None
        data_terhapus = self.top.data #soroti bagiantop dan simpan di variabel
        self.top = self.top.next
        return data_terhapus

    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():    
            return None
        return self.top.data
    def tampilkan(self):
        #Top -> A -> B 
        current = self.top
        print ("Top " , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top):", s.peek())