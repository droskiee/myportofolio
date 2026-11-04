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

### Tugas 3

1. Kita menggunakan ModelForm pada Django agar pembuatan form HTML bisa dilakukan secara otomatis dan langsung terikat dengan model database yang ada, sehingga kita tidak perlu menulis kode berulang secara manual serta bisa melakukan validasi data dengan lebih mudah. Selain itu, penambahan tag {% csrf_token %} diwajibkan sebagai bentuk pengamanan terhadap ancaman serangan Cross-Site Request Forgery (CSRF) guna memastikan bahwa setiap pengiriman data berasal dari pengguna yang sah.

2. Dalam pengembangan aplikasi web modern, format JSON jauh lebih disukai dibandingkan XML karena memiliki struktur sintaks yang lebih ringan, bersih, dan mudah dibaca. Ukuran data JSON yang lebih kecil membuat proses transfer jaringan menjadi jauh lebih cepat, serta format ini secara native sangat kompatibel dengan JavaScript di sisi klien.

3. Alur saat fungsi view mengembalikan data portofolio dalam bentuk JSON dimulai dari permintaan klien ke URL terkait, di mana Django kemudian mengambil data dari database menggunakan ORM, mengubahnya ke format JSON melalui serializer, lalu mengembalikannya lewat objek HttpResponse berjenis application/json. Proses serialization ini wajib dilakukan karena objek QuerySet atau model Django merupakan objek kompleks berbasis Python yang tidak dapat langsung dibaca atau ditransmisikan melalui protokol HTTP standar tanpa diubah terlebih dahulu menjadi format universal seperti string JSON.


### Tugas 5

1. Debouncing adalah sebuah teknik pemrograman yang digunakan untuk menunda eksekusi suatu fungsi (seperti pengiriman request pencarian) sampai pengguna berhenti mengetik atau melakukan aktivitas dalam jeda waktu tertentu (misalnya setelah 300-500 milidetik). Teknik ini sangat penting pada fitur pencarian AJAX agar aplikasi tidak mengirimkan request ke server secara berlebihan di setiap ketukan huruf (keypress), sehingga dapat menghemat bandwidth, mengurangi beban kerja server (server load), dan menjaga performa aplikasi tetap responsif serta mulus bagi pengguna.

2. Penggunaan await berfungsi untuk menunggu hingga proses Promise dari fungsi fetch() selesai sepenuhnya (baik berhasil mengembalikan data maupun gagal) sebelum melanjutkan ke baris eksekusi kode berikutnya. Jika kita tidak menggunakan await (dan tidak menggunakan .then() sebagai alternatifnya), JavaScript akan langsung melanjutkan eksekusi kode di bawahnya secara asinkron tanpa menunggu datanya kembali dari server. Akibatnya, variabel yang menampung hasil fetch akan berisi objek Promise yang masih berstatus pending (belum ada datanya) alih-alih data JSON yang kita harapkan, sehingga data gagal dirender atau menyebabkan error pada aplikasi.

3. XSS adalah jenis kerentanan keamanan di mana penyerang dapat menyisipkan skrip berbahaya (biasanya berupa kode JavaScript atau HTML) ke dalam halaman web yang nantinya akan dilihat oleh pengguna lain. Data yang dimuat melalui AJAX/JavaScript lebih rentan karena proses rendering dilakukan secara dinamis di sisi klien (client-side) dengan menyuntikkan string mentah ke dalam DOM (misalnya melalui innerHTML). Jika data masukan dari pengguna mengandung tag skrip berbahaya dan tidak disaring (sanitized atau di-escape dengan benar), browser akan langsung mengeksekusi skrip tersebut. Sebaliknya, sistem template bawaan Django secara default memiliki mekanisme perlindungan otomatis (auto-escaping) di sisi server untuk mendeteksi dan menetralisir karakter khusus HTML sebelum dikirim ke peramban.