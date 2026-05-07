#=====================================================
#Nama   : Alfitra Mumtaz Hanafi
#NIM    : J0403251058
#Kelas  : TPL A/P2
#=====================================================

#=====================================================
#Implementasi Dasar : Node pada linked list
#=====================================================

class Node:
    #Konstruktor yang dijalankan scr otomatis ketika class node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data = data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjukan ke note berikutnya (awal=none)

#1)Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Menghubungkan Node : A-> B-> C-> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya