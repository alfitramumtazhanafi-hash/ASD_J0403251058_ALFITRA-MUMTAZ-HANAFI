# Nama  : Alfitra Mumtaz Hanafi
# NIM   : J0403251058
# Kelas : A/P2
# Materi: Implementasi Algoritma Shell Sort - Ascending

def shellSort(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):
        currentvalue = data[i]
        position = i
        while position >= gap and data[position-gap] > currentvalue:
            data[position] = data[position-gap]
            position = position - gap
        data[position] = currentvalue

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(data)
print("Ascending:", data)