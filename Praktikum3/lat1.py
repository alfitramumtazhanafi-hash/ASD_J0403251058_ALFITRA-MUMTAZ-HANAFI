
#Latihan	1:		Implementasikan	fungsi	untuk	menghapus	node	dengan	nilai	tertentu.	
#def	delete_node(self,	key):	
#temp	=	self.head	
#if	temp	and	temp.data	==	key:	
#self.head	=	temp.next	
#temp	=	None	
#return	
#prev	=	None	
#while	temp	and	temp.data	!=	key:	
#prev	=	temp	
#temp	=	temp.next	
#if	temp	is	None:	
#return	
#prev.next	=	temp.next	
#temp	=	None
###
def delete_node(self, key):
    temp = self.head
    # Jika node yang ingin dihapus adalah head
    if temp and temp.data == key:
        self.head = temp.next
        temp = None
        return
    # Mencari node yang ingin dihapus
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    # Jika key tidak ditemukan
    if temp is None:
        return
    # Menghapus node
    prev.next = temp.next
    temp = None
