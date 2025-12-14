# Sistem Pathfinding Berdasarkan Rute Dengan Waktu Tercepat Untuk Layanan Pos Pemadam Kebakaran Daerah Balikpapan Menggunakan Algoritma A*
## Mata Kuliah : Pengantar Kecerdasan Artifisial (B)
- Muhamad Radyt Iksan Pratama - 11241048
- James Alvaro Gavriel Pulung - 11241036
- Muhammad Fauzan Akmal - 11241054		
- Yumna Azzahra - 11241090

## Abstract
Efisiensi waktu respon merupakan faktor krusial dalam penanganan situasi darurat, khususnya pada kasus kebakaran di mana keterlambatan dapat berakibat fatal. Proyek ini bertujuan untuk mengembangkan sistem pencarian rute terbaik (pathfinding) yang ditujukan untuk layanan pemadam kebakaran di wilayah Balikpapan. Sistem ini dibangun menggunakan bahasa pemrograman Python 3.13.9 dan memanfaatkan algoritma A* (A-Star) untuk menentukan jalur tercepat antara pos pemadam dan lokasi kejadian.

Metodologi yang digunakan melibatkan pengolahan data geospasial nyata dari OpenStreetMap (OSM) melalui pustaka osmnx untuk memodelkan jaringan jalan sebagai graf. Dalam proses pencarian rute, algoritma A* mengkombinasikan biaya tempuh aktual (G-Cost) dengan fungsi heuristik (H-Cost) berupa jalan yang memiliki waktu paling cepat untuk sampai ke titik tujuan. Hasil implementasi menunjukkan bahwa sistem mampu merekonstruksi jalur optimal secara efisien dari titik awal ke titik tujuan, yang diharapkan dapat menjadi alat bantu navigasi untuk meminimalkan waktu tempuh unit pemadam kebakaran di lapangan.

Kata Kunci: A-Star Algorithm, Pathfinding, OpenStreetMap, Haversine Formula, Layanan Kebakaran, Balikpapan.

## Methods
Dalam pengembangan sistem pathfinding ini, metode yang digunakan terdiri dari mendapatkan data spasial dari Kota Balikpapan, perancangan model matematis, implementasi algoritma pencarian, dan integrasi sistem navigasi. Berikut adalah penjelasan yang lebih terperinci mengenai metode-metode yang sudah disebutkan sebelumnya :

1. Representasi Graf Data Spasial Kota Balikpapan
Data peta Kota Balikpapan diambil dengan memanfaatkan library OSMnx yang bersumber dari OpenStreetMap (OSM). Peta direpresentasikan sebagai Multi-Directed Graph (MultiDiGraph), di mana :
    * Nodes (Simpul) : Merepresentasikan persimpangan jalan atau titik ujung jalan
    * edge (Sisi) : Merepresentasikan segmen-segmen jalan yang menghubungkan 2 node. Setiap edge memiliki attribute seperti, length (panjang jalan dalam meter), highway (jenis jalan), dan maxspeed(batas kecepatan jalan). 
<br>
2. Algoritma Pathfinding
Pencarian rute terbaik pada program ini dilakukan dengan menggunakan algoritma A* (A-Star). Alasan mengapa algoritma ini dipilih dikarenakan kemampuannya untuk menemukan jalur paling optimal secara efisien dengan memanfaatkan fungsi heuristik agar algoritma tidak semata-mata hanya mencari ke segala arah.
fungsi evaluasi total f(n) untuk setiap node (n) dirumuskan sebagai berikut : 
$$f(n) = g(n) + h(n)$$
yang dimana : 
g(n) : merupakan biaya aktual untuk berpindah dari titik awal ke node n
h(n) : Estimasi biaya heuristik dari node n ke titik tujuan
<br>
3. Fungsi Biaya
Alih-alih mencari rute jalan terdekat yang dapat di ambil. Tujuan utama dari proyek ini adalah mencari rute jalan yang dapat ditempuh untuk mendapatkan waktu tempuh terdekat. Oleh karena itu, bobot (weight) antar node dihitung dalam satuan detik, bukan meter.
Persamaan yang digunakan untuk menghitung biaya (cost) pada setiap segmen jalan adalah : 
$$Cost_{time} = \frac{d}{v}$$
Dimana :
d : Merupakan panjang jalan (meter) yang didapat menggunakan atribute `length`
v : Kecepatan kendaraan (meter/detik)
OpenStreetMap memiliki data nilai jalan seperti `maxspeed` yaitu kecepatan maksimal yang dapat ditempuh dalam suatu jenis jalan. Namun data yang dimiliki OpenStreetMap sangat terbatas, sehingga tidak semua jenis kendaraan memiliki nilai `maxspeed` yang bisa langsung diambil. Untuk menangani hal tersebut kami mengambil data dari PERATURAN MENTERI PERHUBUNGAN REPUBLIK INDONESIA NOMOR PM 111 TAHUN 2015 sebagai referensi untuk mengisi nilai `maxspeed` yang tidak tersedia.
<br>
4. Fungsi Heuristik 
Agar Algoritma A* yang digunakan bersifat admissible (tidak pernah melebih-lebihkan biaya sisa) dan konsisten, fungsi heuristik juga harus dalam satuan waktu detik. Heuristik dihitung menggunakan Haversine Formula (jarak garis lurus pada permukaan bola bumi) dibagi dengan kecepatan maksimum global yang mungkin terjadi pada peta. 
$$h(n) = \frac{\text{Distance}_{Haversine}(n, goal)}{v_{max\_global}}$$
Dimana ${v_{max\_global}}$ ditetapkan sebesar 90 m/s untuk memastikan estimasi waktu tidak pernah lebih kecil dari waktu tempuh nyata yang dapat dilakukan secara teoritis, sehingga hal ini menjamin ditemukannya rute optimal
<br>
5. Penentuan Lokasi Pos Pemadam
Sebelum algoritma dijalankan, sistem menghitung jarak semua pos pemadam kebakaran yang ada di balikpapan terhadap lokasi kebakaran. Setelah pos pemadam kebakaran yang memiliki jarak terdekat dengan lokasi kebakaran ditemukan, pada pos tersebut akan menjadi node pertama (starting node).

### Tools yang Digunakan
| Kategori | Tools | Deskripsi |
| :--- | :--- | :--- |
| Bahasa Pemrograman | Python 3.13.9 | Bahasa utama untuk pengembangan logika. |
| Library Geospasial & Visualisasi | `osmnx`, `folium`, `contextily`, `matplotlib.pyplot` | Digunakan untuk memproses data peta (OpenStreetMap) dan visualisasi rute. |
| Library Komputasi & Data | `pandas`, `numpy` | Digunakan untuk manipulasi data struktur dan perhitungan matematis (trigonometri). |
| Library Utilitas | `random`, `typing` | Untuk pengacakan node dan type hinting. |
| Algoritma | A* (A-Star) | Algoritma pencarian jalur terpendek menggunakan heuristik. |
| Rumus Matematika | A* (A-Star) : $f(n) = g(n) + h(n)$. <br> Haversine formula : $d = R \cdot \arccos(\sin \phi_1 \sin \phi_2 + \cos \phi_1 \cos \phi_2 \cos(\Delta \lambda))$| Algoritma pencarian jalur terpendek menggunakan heuristik dan rumus mencari jarak garis lurus pada permukaan bola bumi |
| Tools Lain | Git, Github | Alat dan platform version control system

## Implementation

### Struktur Proyek
Pada proyek ini terdapat enam file utama yaitu : 
- helper.py
- creating_nodes.py
- fire_station.py
- aSTAR.py
- initialization.py
- main.py

Berikut adalah penjelasan mengenai mengenai file-file yang telah disebutkan di atas. 
1. `helper.py`
Berikut adalah penjelasan mengenai fungsi yang ada di dalam file helper.py

| Nama Fungsi | Fungsi/tujuan 
| :--- | :--- | 
| rad_to_degree & degree_to_rad | Mengkonversi satuan sudut antara radian dan derajat untuk keperluan perhitungan haversine |
| calculateHeuristic_length | Menghitung jarak garis lurus antara dua koordinat geografis menggunakan formula haversine | 
| calculateHeuristic_time | Mengkonversi estimasi jarak menjadi estimasi waktu dengan asumsi kecepatan maksimum global. Fungsi ini menjamin sifat admissible dari heuristik A*(A-star) | 
| get_speed_from_edges | Menentukan kecepatan perjalanan pada suatu segmen jalan|
| get_neighbor_cost_time | Mengambil semua node tetangga yang tersedia beserta informasi biaya waktu tempuh ke masing-masing tetangga | 
| reconstruct_path | Merekonstruksi jalur lengkap dari node awal ke node tujuan
| getting_taken_road_info| Mengekstrak informasi jalanan yang diambil seperti nama jalan 

<br>

2. creating_nodes.py
File ini bertanggung jawab untuk membuat dan memanipulasi struktur data node. Berikut adalah penjelasan mengenai fungsi yang ada di dalam file creating_nodes.py

| Nama Fungsi | Fungsi/tujuan 
| :--- | :--- | 
|  createNo  |Fungsi createNo menerima beberapa argumen, salah satunya adalah type. Jika argumen type=1 maka ini akan membuat starting node secara acak (fungsi ini banyak digunakan saat tahap testing) yang kedua adalah type=2, type=2 membuat node acak yang berfungsi sebagai node tujuan (tempat terjadinya kebakaran) |
| neighbour| Fungsi ini bertujuan untuk membuat struktur node tetangga yang akan dieksplorasi dalam algoritma A*|

<br>

3. fire_station.py
File ini bertanggung jawab untuk mengelola data pos kebakaran dan logika pemilihan pos pemadam kebakaran yang akan dijadikan starting node. Berikut adalah penjelasan mengenai fungsi yang ada di dalam file fire_station.py

| Nama Fungsi | Fungsi/tujuan   
| :--- | :--- | 
|  get_fire_stations_nodes  | Memetakkan koordinat GPS pos pemadam kebakaran dengan node terdekat yang ada pada data OSMnx |
| get_closest_fire_station_to_target| Menentukan pos kebakaran mana yang memiliki jarak garis lurus terdekat dengan lokasi kebakaran|

<br>

4. aSTAR.py
Disinilah pengimplementasian algoritma A* dengan memanfaatkan fungsi-fungsi yang sudah disebutkan dalam file-file sebelumnya .Berikut adalah penjelasan mengenai fungsi yang ada di dalam file aSTAR.py

| Nama Fungsi | Fungsi/tujuan   
| :--- | :--- | 
|  find_path  | Ini merupakan fungsi utama yang memanfaatkan semua fungsi-fungsi pada file-file Helper.py `, `creating_nodes.py dan - fire_station.py  

<br>

5. initialization.py
File ini menginisialisasikan sistem, menjalankan algoritma pathfinding, dan ekskusi utama algoritma tanpa dibungkus fungsi terpisah.
<br>

6. main.py
Ini merupakan file utama yang mengintegrasikan semua komponen dan menyajikan output secara informatif di terminal dan dalam bentuk visual. Disini juga tidak ada fungsi yang dibuat

### Alur program
Berikut adalah penjelasan tentang apa yang terjadi saat kode di dalam file `main.py` dijalankan : 
1. **Program memuat library eksternal** (`osmnx`, `folium`, dll) dan modul internal.

<br>

2. **Penentuan Titik Tujuan(Goal Node)**:
    - Memanggil fungsi `creating_nodes.createNo(type=2)`.
    - Program mengambil ID node dan koordinat posisi tujuan secara acak sebagai simulasi lokasi kebakaran.
  
<br>

3. **Pemilihan Pos Pemadam Terdekat**:
    - Memanggil fungsi `get_fire_stations_nodes` untuk memetakan 6 pos kebakaran yang ada di balikpapan
    - Memanggil fungsi `get_closest_fire_station_to_target` untuk menentukan pos pemadam kebakaran yang memiliki posisi terdekat dengan Goal Node (Lokasi kebakaran)
    - Pos terpilih akan menjadi Starting Node atau Node awal
  
<br>

4. **Pencarian Rute (Pathfinding)**:
    - Fungsi `aSTAR.find_path()` dipanggil dengan parameter: ID Awal, ID Tujuan, Koordinat Awal, dan Koordinat Tujuan.
    - Algoritma A* bekerja dengan memanfaatkan fungsi heuristik heuristic waktu dan pengecekan *neighbor* dari `helper.py`.
  
<br>

5. **Perhitungan Data Rute dan Nama-Nama Jalan Yang Dilalui**:
    - Program menghitung total jarak tempuh dan total waktu yang dihabiskan dengan memanfaatkan *fungsi get_speed_from_edges* dari `helper.py` dan method *get_edge_data* dari object graph NetworkX.
    - Setelah itu fungsi *getting_taken_road_info* dari `helper.py` untuk mendapatkan ekstrak nama-nama jalan yang telah dilalui.
  
<br>

6. **Visualisasi Hasil**:
    - Memvisualisasikan hasil dengan memanfaatkan library `matplotlib.pyplot`.

<br>

7. **Output Hasil**:
    - Jika jalur ditemukan (`if path:`), program akan mencetak instruksi navigasi ke console dan memvisualisasikan jalur yang telah dipilih dalam berbentuk map.
    - Jika gagal, program mencetak "error".

## Demo
## 1. Cara Menjalankan Program
1. Jalankan file main.py
2. Biarkan Program berjalan hingga menghasilkan Output pada Terminal
3. Program akan terus berjalan hingga membuat map atau peta rute Pos Pemadam Kebakaran menuju ke Lokasi Kejadian

<br>
## 2. Ilustrasi (Hasil Visualisasi)
https://drive.google.com/file/d/1gVc7n58QEqGlGuBPtxAgIEaUJjfIxKNG/view?usp=drive_link (GIF)


<br>
## 3. Hasil (Terminal)
importing..
dependencies..

starting

Node target (emergency) yang terpilih memiliki ID = || 7540555826 || dengan data  {'y': -1.2148061, 'x': 116.8564501, 'street_count': 3} || latitude = -1.2148061, longitude = 116.8564501
(None, {'id': 7540555826, 'position': (-1.2148061, 116.8564501)})

[SISTEM] Ditemukan 6 titik Pos Pemadam Kebakaran dalam database.
 - Pos pemadam kebakaran balikpapan tengah
 - Pos BPBD WIL UTARA Kota Balikpapan
 - pos pemadam kebakaran uptbd balikpapan selatan
 - Pos Pemadam Kebakaran, Uptpbd Wil Timur
 - pemadam kebakaran kebun sayur
 - Pos Pemadam UPT PBD Wil Kota

==================================================
       LAPORAN LOKASI DARURAT
==================================================
Lokasi Kejadian (Emergency) : (-1.2148061, 116.8564501)
Pos Pemadam Terpilih        : Pos BPBD WIL UTARA Kota Balikpapan
Jarak Lurus (Euclidean)     : 3.06 KM
Koordinat Pos Pemadam       : (-1.2369789, 116.8400918)
==================================================

[SISTEM] Sedang menghitung rute terbaik menggunakan A*...

============================================================
PANDUAN NAVIGASI DARI: POS BPBD WIL UTARA KOTA BALIKPAPAN
============================================================
1. Ikuti jalan Unnamed Road
2. Ikuti jalan Jalan Soekarno-Hatta
3. Ikuti jalan Unnamed Road
4. Ikuti jalan Jalan Soekarno-Hatta hingga tujuan
------------------------------------------------------------
RINGKASAN PERJALANAN
Estimasi Waktu Tempuh : 4.28 Menit
Total Jarak Tempuh    : 3.79 KM
============================================================
<br>

## Summary
Pengembangan sistem pathfinding untuk layanan pemadam kebakaran di Kota Balikpapan ini berhasil diimplementasikan dengan memanfaatkan algoritma A* (A-Star) dan pengolahan data geospasial OpenStreetMap (OSM). Berbeda dengan navigasi standar yang hanya berfokus pada jarak terpendek, sistem ini memprioritaskan waktu tempuh tercepat ($Cost_{time}$) dengan memperhitungkan variabel panjang jalan dan batas kecepatan kendaraan sesuai regulasi nyata.

Penerapan fungsi heuristik yang mengombinasikan Haversine Formula dengan kecepatan maksimum global (90 m/s) terbukti mampu menjaga sifat admissible dan konsisten pada algoritma, sehingga menjamin ditemukannya rute yang paling optimal tanpa melebih-lebihkan estimasi biaya. Selain itu, integrasi fitur cerdas dalam penentuan pos pemadam terdekat (get_closest_fire_station_to_target) memastikan bahwa titik awal pencarian rute selalu dimulai dari unit yang paling strategis terhadap lokasi kejadian.

Secara keseluruhan, simulasi menunjukkan bahwa sistem mampu merekonstruksi jalur evakuasi secara efisien dan menyajikan visualisasi rute yang jelas melalui peta interaktif. Hal ini mengindikasikan bahwa pendekatan algoritma A* pada data graf jalan nyata memiliki potensi besar untuk diaplikasikan sebagai alat bantu navigasi dalam meminimalkan waktu respon (response time) pada situasi darurat kebakaran di Balikpapan.

## References
* Kementerian Perhubungan Republik Indonesia. (2015). Peraturan Menteri Perhubungan Republik Indonesia Nomor PM 111 Tahun 2015 tentang Tata Cara Penetapan Batas Kecepatan. Database Peraturan BPK. https://peraturan.bpk.go.id/Details/103508/permenhub-no-111-tahun-2015 
* Kumar, R. (2024, November 7). The A* Algorithm: A Complete Guide*. DataCamp. https://www.datacamp.com/tutorial/a-star-algorithm
* Karr, D. (2022, 5 Desember). Calculate or query great circle distance between points of latitude and longitude using the Haversine formula (PHP, JavaScript, Java, Python, MySQL, MSSQL examples). Martech Zone. https://martech.zone/calculate-great-circle-distance

