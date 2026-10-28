
nilai = []

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if not baris:
            continue

        try:
            nim, teks_nilai = baris.split(",")
            angka = float(teks_nilai)
            nilai.append(angka)
            print(f"{nim}: {angka}")
        except ValueError:
            print(f"Data tidak valid: {baris}")

if nilai:
    rata_rata = sum(nilai) / len(nilai)
    print(f"Rata-rata nilai valid = {rata_rata:.2f}")
else:
    print("Tidak ada nilai valid.")
