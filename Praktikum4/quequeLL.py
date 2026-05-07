#=====================================================
#Nama   : Alfitra Mumtaz Hanafi
#NIM    : J0403251058
#Kelas  : TPL A/P2
#=====================================================

#=====================================================
#Implementasi Dasar : Queque
#=====================================================

class Node:
    #Konstruktor yang dijalankan scr otomatis ketika class node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjukan ke note berikutnya (awal=none)

class queque:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None
    
    #Membuat fungsi untuk menambahkan data baru
    def enqueque(self, data):
            nodeBaru = Node(data)
            
            if self.is_empty():
                 self.front = nodeBaru
                 self.rear =  nodeBaru
                 return
            

            self.rear.next = nodeBaru
            self.rear = nodeBaru
            
    def dequeue(self):
        #menghapus data dari depan
        data_terhapus = self.front.data

        #geser front ke node berikutnya
        self.front = self.front.next

        #jka setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi none
        if self.front is None:
             self.rear = None

        return data_terhapus
    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Rear")

q = queque()
q.enqueque("A")
q.enqueque("B")
q.enqueque("C")
q.tampilkan()
q.dequeue
q.tampilkan()