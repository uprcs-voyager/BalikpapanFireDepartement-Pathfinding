# Steps 
## 1 Mengimport library yang dibutuhkan 
Sebelum memulai project kita harus mengimport library-library yang dibutuhkan yaitu : 
- osmnx
- matplotlib
- folium (optional)

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


