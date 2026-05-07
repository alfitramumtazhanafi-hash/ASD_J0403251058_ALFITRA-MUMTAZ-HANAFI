def quick_sort(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]

        kiri=[]
        tengah=[]
        kanan=[] 

        for angka in data:
            if angka < pivot:
                kiri.append(angka)
            elif angka > pivot:
                kanan.append(angka)
            else: 
                tengah.append(angka)

    return quick_sort(kiri) + tengah + quick_sort(kanan)

data=[20, 13, 14, 8, 6, 10, 11]
print("Data sebelum diurutkan:", data)
hasil = quick_sort(data)
print("Data setelah diurutkan:", hasil)