#=======================================================
# Nama   : ALFITRA MUMTAZ HANAFI
# Nim    : J0403251058
# Kelas  : A/P2
#=======================================================

#=======================================================
# Bubble Sort untuk mengurutkan skor kandidat secara descending
#=======================================================

nilai = [32, 12, 45, 32, 23, 42, 444]
def bubblesort(nilai):
    n = len(nilai)
    for i in range(n-1):
        for j in range(n-i-1): #membandingkan dua elemen yang bersebelahan dalam list
            if nilai[j] > nilai[j+1]:
                nilai[j], nilai[j+1] = nilai[j+1], nilai[j] #menukar posisi elemen jika maka elemen yang pertama lebih besar dari elemen yang kedua
bubblesort(nilai)
print("nilai yang sudah diurutkan dengan bubble sort:", nilai)