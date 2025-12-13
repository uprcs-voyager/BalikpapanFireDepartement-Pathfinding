# Sistem Pathfinding Rute Terbaik Untuk Layanan Kebakaran Daerah Balikpapan Menggunakan Algoritma A*
## Mata Kuliah : Pengantar Kecerdasan Artifisial (B)

| Kategori | Tools | Deskripsi |
| :--- | :--- | :--- |
| Bahasa Pemrograman | Python 3.13.9 | Bahasa utama untuk pengembangan logika. |
| Library Geospasial & Visualisasi | `osmnx`, `folium`, `contextily`, `matplotlib.pyplot` | Digunakan untuk memproses data peta (OpenStreetMap) dan visualisasi rute. |
| Library Komputasi & Data | `pandas`, `numpy` | Digunakan untuk manipulasi data struktur dan perhitungan matematis (trigonometri). |
| Library Utilitas | `random`, `typing` | Untuk pengacakan node dan type hinting. |
| Algoritma | A* (A-Star) | Algoritma pencarian jalur terpendek menggunakan heuristik. |
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
1. Program memuat library eksternal (`osmnx`, `folium`, dll) dan modul internal dari folder `components`.
2. **Penentuan Titik Awal (Start Node)**:
    - Memanggil fungsi `creating_nodes.createNo(type=1)`.
    - Program mengambil ID node dan koordinat posisi awal.
3. **Penentuan Titik Tujuan (Goal Node)**:
    - Memanggil fungsi `creating_nodes.createNo(type=2)`.
    - Program mengambil ID node dan koordinat posisi tujuan.
4. **Pencarian Rute (Pathfinding)**:
    - Fungsi `aSTAR.find_path()` dipanggil dengan parameter: ID Awal, ID Tujuan, Koordinat Awal, dan Koordinat Tujuan.
    - Algoritma A* bekerja dengan memanfaatkan fungsi heuristik dan pengecekan *neighbor* dari `helper.py`.
5. **Output Hasil**:
    - Jika jalur ditemukan (`if path:`), program mencetak "path found".
    - Jika gagal, program mencetak "error".