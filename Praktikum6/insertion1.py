# Nama  : Alfitra Mumtaz Hanafi
# NIM   : 0403251058
# Kelas : A/P2
# Materi: Implementasi Algoritma Insertion Sort - Ascending

def insertionSort(data):
    for index in range(1, len(data)):
        currentvalue = data[index]
        position = index
        
        while position > 0 and data[position-1] > currentvalue:
            data[position] = data[position-1]
            position = position - 1
            
        data[position] = currentvalue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(data)
print("Ascending:", data)