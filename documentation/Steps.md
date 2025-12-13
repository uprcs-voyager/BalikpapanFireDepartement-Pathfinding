# Steps 
## 1 Mengimport library yang dibutuhkan 
Sebelum memulai project kita harus mengimport library-library yang dibutuhkan yaitu : 
- osmnx: Untuk mengambil dan memproses data peta jalan.
- matplotlib: Untuk plotting grafik statis.
- folium: Untuk visualisasi peta interaktif. (Optional)
- contextily: Untuk menambahkan basemap pada plot geospasial.

## 2 Mendownload / menyiapkan data yang dibutuhkan 
Data - data yang dibutuhkan adalah : 
1. map dari balikpapan (dalam bentuk graphml)
Pengambilan map balikpapan dilakukan dengan cara mendownload terlebih dahulu file graphml nya, agar saat program di jalankan tidak perlu mengambil lagi dari server OSM melainkan di load secara lokal (karena sudah di download).
###
2. Data jalanan yang akan dijadikan weight :
   1. Tipe jalan (Highway? Residential?)
   2. Tipe arah jalan (one way?, two way?)
   3. kecepatan maksimal (maxspeed)
   4. Lebar jalanan (width)
   5. Kepadatan jalanan (traffic density)

## 3. Menjalankan Program Utama
Setelah instalasi dan data siap, jalankan file main.py. Berikut adalah detail proses yang terjadi di balik layar
1. Generate Nodes
Kode akan memanggil fungsi createNo dua kali:
- Type 1 (Start Node): Memilih satu node secara acak (atau ditentukan) dari graf sebagai titik keberangkatan.
- Type 2 (Goal Node): Memilih satu node lain sebagai titik tujuan.
Output: ID Node dan Koordinat (Latitude, Longitude) ditampilkan di terminal.

2. Proses A* (A-Star Calculation)
Setelah Start dan Goal didapatkan, fungsi aSTAR.find_path dijalankan:
- Perhitungan Heuristik: Menggunakan Haversine Formula (dari helper.py) untuk memperkirakan jarak lurus dari node saat ini ke tujuan.
- Eksplorasi Neighbor: Program mengecek tetangga node yang bisa dilewati.
- Evaluasi Cost: Menghitung F = G + H (Jarak tempuh + Heuristik). Node dengan F terkecil akan dipilih untuk langkah selanjutnya.

3. Hasil Akhir
Jika rute berhasil direkonstruksi, terminal akan menampilkan pesan "path found".
