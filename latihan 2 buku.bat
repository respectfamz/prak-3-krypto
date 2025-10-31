import itertools

print("=== LATIHAN 2: Pengaturan Buku di Rak ===")

n = int(input("Masukkan jumlah buku (n): "))
r = int(input("Masukkan jumlah bagian rak (r): "))

# Label buku
buku = [f"B{i+1}" for i in range(n)]

# Semua cara menempatkan buku di rak
kombinasi = list(itertools.product(range(1, r + 1), repeat=n))

print(f"\nTotal cara mengatur: {len(kombinasi)}\n")

for i, k in enumerate(kombinasi, start=1):
    print(f"Cara {i}:")
    for j in range(n):
        print(f"  {buku[j]} -> Rak {k[j]}")
    print()
