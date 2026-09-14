Nama : Piedra Ridwan Azra Pulungan

NPM : 2506623055

Kelas : PBP D

test

### Tugas 1

1. Ya, saya menggunakan elemen semantik seperti `<section>` dan `<header>`. Elemen ini sangat membantu dalam menyusun *static web* agar kodenya lebih terstruktur, mudah dibaca, dan jelas hierarkinya.

2. Tantangan utamanya adalah menjaga tata letak agar tidak berantakan saat layar mengecil ke ukuran *mobile*. Evaluasinya dilakukan dengan memprioritaskan informasi penting agar tampil di atas, serta memanfaatkan *flexbox/grid* agar kartu konten otomatis menumpuk secara vertikal.

3. Batasan utamanya adalah ketiadaan fitur interaktif murni seperti form kontak dinamis atau sistem manajemen konten. Fungsionalitas dinamis yang ingin ditambahkan pada iterasi berikutnya adalah integrasi backend penuh untuk pengelolaan data portofolio secara otomatis.

### Tugas 2

1. Alur MVT dimulai ketika browser mengirimkan permintaan HTTP ke server, yang kemudian diarahkan oleh urls.py proyek ke urls.py aplikasi untuk mencocokkan pola path dengan fungsi view yang sesuai. Selanjutnya, view akan berinteraksi dengan Model untuk mengambil data dari database, lalu merendernya ke dalam Template HTML menggunakan objek context sebelum akhirnya dikirim kembali ke browser untuk ditampilkan kepada pengguna. 

2. Penyimpanan data pada model alih-alih langsung di dalam template sangat penting untuk menerapkan prinsip pemisahan tanggung jawab (separation of concerns), di mana model mengurus struktur data dan template hanya fokus pada tampilan antarmuka. Pendekatan ini membuat aplikasi jauh lebih mudah dipelihara dan dikembangkan karena perubahan data atau penambahan informasi dapat dikelola langsung lewat database atau panel admin tanpa harus membongkar baris kode HTML satu per satu.

3. Perbedaan utama terletak pada fungsinya, di mana makemigrations bertugas membuat berkas blueprint atau skrip migrasi berdasarkan perubahan pada models.py tanpa menyentuh database, sedangkan migrate berfungsi mengeksekusi skrip tersebut agar perubahan tabel atau kolom benar-benar diterapkan ke dalam database fisik. Contoh nyata yang mewajibkan kedua perintah ini dijalankan adalah ketika kita baru saja menambahkan model baru seperti Skill atau menambahkan atribut/kolom baru ke dalam model yang sudah ada.