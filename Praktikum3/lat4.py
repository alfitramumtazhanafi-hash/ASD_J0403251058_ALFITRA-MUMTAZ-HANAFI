# Fungsi untuk menampilkan linked list
def tampilkan(linked_list):
    if not linked_list:
        return "kosong"
    hasil = ""
    for elemen in linked_list:
        hasil += str(elemen) + " -> "
    hasil += "null"
    return hasil


# Input Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan koma): ")

if data1.strip() != "":
    list1 = list(map(int, data1.replace(" ", "").split(",")))
else:
    list1 = []

# Input Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan koma): ")

if data2.strip() != "":
    list2 = list(map(int, data2.replace(" ", "").split(",")))
else:
    list2 = []

# Tampilkan Linked List 1
print("Linked List 1:", tampilkan(list1))

# Tampilkan Linked List 2
print("Linked List 2:", tampilkan(list2))

# Gabungkan kedua linked list
gabungan = list1 + list2

# Tampilkan hasil gabungan
print("Linked List setelah digabungkan:", tampilkan(gabungan))
