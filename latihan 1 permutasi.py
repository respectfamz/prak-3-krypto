import itertools

def permutasi_berkelompok(grup): 
    hasil = [[]] 
    for kelompok in grup: 
        hasil_baru = [] 
        for hsl in hasil: 
            for perm in itertools.permutations(kelompok): 
                hasil_baru.append(hsl + list(perm)) 
        hasil = hasil_baru 
    return hasil 

# === Program utama ===
print("=== LATIHAN 1: Permutasi Berkelompok ===")

n = int(input("Masukkan jumlah kelompok: "))
grup = []

for i in range(n):
    data = input(f"Masukkan elemen-elemen kelompok ke-{i+1} (pisahkan dengan spasi): ").split()
    grup.append(data)

hasil = permutasi_berkelompok(grup)

print("\nHasil semua permutasi berkelompok:")
for p in hasil:
    print(p)
