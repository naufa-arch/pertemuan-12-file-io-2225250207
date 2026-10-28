# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Hashifah Naufa Setiawan  
**NIM:** 2225250207 
**Kelas:** 3E

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data dari file menggunakan Python serta menangani kesalahan yang mungkin terjadi saat program dijalankan.

## Format File Input
Data disimpan dalam file `data/nilai.txt` dengan format `NIM,nilai`.

Contoh isi file:
```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

## Cara Menjalankan
Jalankan perintah berikut melalui terminal VS Code dari folder proyek:

```bash
python3 tugas/rekap_nilai_file.py
```

Pada Windows, jika perintah `python3` tidak berfungsi, gunakan:

```bash
python tugas/rekap_nilai_file.py
```

## Error yang Ditangani
- **FileNotFoundError:** Terjadi ketika file input tidak ditemukan. Program menampilkan pesan bahwa file tidak ditemukan.
- **ValueError:** Terjadi ketika nilai tidak dapat dikonversi menjadi angka, misalnya `abc`. Program menandai baris tersebut sebagai data tidak valid dan melanjutkan pemrosesan data lainnya.

## Test Case

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| File berisi nilai valid | Data terbaca dan rata-rata dihitung dengan benar | Data terbaca dan rata-rata dihitung | Berhasil |
| File tidak ditemukan | Program menampilkan pesan file tidak ditemukan | Pesan kesalahan ditampilkan | Berhasil |
| Nilai berisi teks `abc` | Data tidak valid ditampilkan dan dilewati | Data tidak valid ditampilkan dan dilewati | Berhasil |
| File berisi baris kosong | Baris kosong dilewati | Baris kosong dilewati | Berhasil |

## Refleksi
Salah satu error yang ditemukan adalah `ValueError`, yaitu ketika nilai berupa teks seperti `abc` tidak dapat dikonversi menjadi angka. Untuk mengatasinya, program menggunakan `try-except` agar kesalahan dapat ditangani dengan menampilkan pesan data tidak valid. Program kemudian melanjutkan pemrosesan baris lainnya sehingga data yang valid tetap dapat digunakan untuk menghitung rata-rata. Saya belajar bahwa validasi input dan penanganan error penting agar program lebih aman dan tidak langsung berhenti ketika menemukan data yang salah.