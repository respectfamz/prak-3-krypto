import itertools

def faktorial(x):
    if x == 0 or x == 1:
        return 1

    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil


def kombinasi(n, r):
    if r > n:
        return 0

    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)

    return faktorial_n // (faktorial_r * faktorial_n_r)


# Input dari user
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))

# Buat daftar huruf: A, B, C, ...
huruf = [chr(ord('A') + i) for i in range(n)]

# Hitung jumlah kombinasi
hasil = kombinasi(n, r)
print(f"\nJumlah kombinasi C({n}, {r}) = {hasil}\n")

# Tampilkan semua kombinasi
print("Daftar kombinasi:")
for c in itertools.combinations(huruf, r):
    print(c)
