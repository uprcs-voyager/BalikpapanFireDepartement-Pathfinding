# Sistem Pathfinding Rute Terbaik Untuk Layanan Kebakaran Daerah Balikpapan Menggunakan Algoritma A*
## Mata Kuliah : Pengantar Kecerdasan Artifisial (B)

## 1. Metodologi
### 1.1 Tools yang digunakan 
| Kategori | Tools |
| :--- | :--- |
| Bahasa pemrograman | Python 3.13.9 |
| Library Eksternal | osmnx, matplotlib.pyplot, pandas, random, numpy, typing |
| Rumus Yang Digunakan | Haversine Formula |
| Algoritma yang Digunakan | A* (A-Star) |
| Tools Lain | Git, Github |

## 2. Implementaasi
### 2.1 Struktur Proyek
Pada proyek ini terdapat lima folder yaitu : 
- cache
- components
- data_checking
- documentation
- testing

Berikut adalah penjelasan mengenai folder - folder yang telah disebutkan di ataa. 
1. cache 
Folder cache berfungsi sebagai tempat penyimpanan untuk hal-hal yang kemungkinan sudah tidak lagi digunakan atau tidak memiliki dampak yang signifikan terhadap kinerja proyek secara keseluruhan. File-file tersebut di simpan dalam folder cache dan tidak dihapus dikarenakan untuk berjaga-jaga jika suatu saat file tersebut dibutuhkan kembali.
#####
2. components
Folder Components berisi file-file komponen yang dibuat agar implementasi algoritma A* pada peta balikpapan dapat berhasil. File-file yang ada di dalam folder ini terdiri atas : 
   - `aSTAR.py` : file ini berperan sebagai algoritma A* utama yang digunakan untuk mencari rute-rute yang tersedia lalu menentukan rute terbaik berdasarkan rute yang memiliki F Cost terkecil
   - `creating_nodes.py` : File ini berisi kode untuk menentukan nodes-nodes yang akan digunakan saat program berjalan. 
   - `helper.py` : Pada file ini berisi kode helper yang bertujuan untuk melengkapi hal-hal yang dibutuhkan dalam penerapan alrogitma A* pada peta dunia nyata seperti Fungsi untuk menghitung nilai Heuristic, fungsi untuk mencari node tetangga, dan fungsi untuk merekonstruksi path yang sudah ditemukan 
#####
3. data_checking : 
   Isi dari folder ini adalah file bernama `geodataframes.py` di dalam file ini terdapat kode yang berfungsi untuk mengecek data yang ada pada edges dan node di file `Balikpapan_map_graph.graphml` seperti kategori yang tersedia contohnya, panjang edges, nama jalan, dan lain-lain.
####
4. documentation
   File-file yang ada di dalam folder ini berfungsi sebagai dokumentasi tentang pengerjaan proyek ini `Docs_tracking.md` berisi pencatatan tentang perubahan dan penambahan apa saja yang telah dilakukan pada proyek ini dan `Steps.md` berisi langkah - langkah bagaimana program ini nantinya akan berjalan 
#####
5. Testing 
   Folder ini hanya berfungsi untuk mengetes file-file yang berisi kode seperti A*, pencari neighbor, data checking, dan lain-lain. Dalam tahap akhir folder ini akan dihapus/di masukan ke dalam `.gitignore`


### 2.2 Alur program
Berikut adalah penjelasan tentang apa yang terjadi saat kode di dalam file `main.py` dijalankan : 
1. kode akan memanggil fungsi create node type 1 untuk membuat node awal (posisi awal)
2. Selanjutnya data-data node 1 (posisi awal) akan di ambil, termasuk koordinat dan ID nya untuk ditampilkan pada terminal 
3. Berikutnya kode akan menjalankan fungsi create_node lagi namun kali ini dengan type 2 yang artinya node yang akan dibuat akan menjadi node tujuan.
4. Data-data node 2 (node tujuan) juga akan di ambil termasuk koordinat dan ID node nya yang lalu akan ditampilkan di terminal
5. Setelah terdapat node awal (node 1) dan node tujuan (node 2). Kode akan memanggil fungsi pada file aSTAR untuk memulai pencarian rute terbaik yang dapat digunakan
6. Proses utama program terjadi pada file aSTAR. function find_path mengambil parameter-parameter seperti ` start_id: Tuple[float], goal_id: Tuple[float], start_coordinate: Tuple[float, float],  goal_coordinate: Tuple[float, float]`. fungsi ini lalu memanfaatkan fungsi-fungsi yang terdapat di dalam file `helper.py` dan `creating_nodes.py` untuk mendapatkan data heuristic, neighbor yang ada, dan juga membuat node baru berdasarkan neighbor yang tersedia. 
7. Selanjutnya, jika path yang optimal sudah ditemukan, kode akan memanggil fungsi yang berada di `helper.py`, fungsi tersebut bernama `reconstruct_path`.