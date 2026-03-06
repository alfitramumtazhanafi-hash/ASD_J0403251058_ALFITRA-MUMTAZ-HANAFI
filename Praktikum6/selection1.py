# Nama  : Alfitra Mumtaz Hanafi
# NIM   : J0403251058
# Kelas : A/P2
# Materi: Implementasi Algoritma Selection Sort - Ascending

def selectionSort(data):
    for fillslot in range(len(data)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if data[location] > data[positionOfMax]:
                positionOfMax = location
        
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(data)
print("Ascending:", data)