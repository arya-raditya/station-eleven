# Tugas Week 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

=> 
Pertama, dimulai dengan membuat direktori baru di lokal dengan nama e-commerce yang ingin saya buat, yaitu station-eleven. Kemudian, pada direktori tersebut, diinstall requirements yang telah dilist di requirements.txt. Lalu, project Django diinisiasi dengan “django-admin startproject (nama project)”. Selanjutnya, pada settings.py, ditambahkan localhost ke allowed host.

Kemudian, aplikasi dengan nama main dibuat dengan menjalankan command “python manage.py startapp main”. Setelah berhasil dijalankan, folder dengan nama main akan otomatis dibuat. Untuk melakukan routing pada proyek agar dapat menjalankan aplikasi main, ditambahkan “main” pada installed apps di settings.py.

Lalu, model pada aplikasi main diisi dengan atribut-atribut yang wajib diimplementasi, yaitu nama produk, harga, dan deskripsi. Saya juga menambahkan satu atribut tambahan berupa integer. Selanjutnya, saya membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikas, nama, dan kelas saya. Lalu, saya juga menambahkan contoh produk yang ingin saya tampilkan di e-commerce.

Kemudian, saya sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py dengan cara menambahkan fungsi yang dapat memanggil aplikasi “main”.

Terakhir, agar dapat dilihat melalui device lain, saya melakukan deployment ke PWS.


## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta rsponnya dan jelaskan pada bagan tersebut kaitan urls.py, views.py, models.py, dan berkas html.

![Bagan](./images/bagan_pbp.JPG)
HTTP Request yang dikirim oleh pengguna diterima oleh urls.py, yang bertugas mencocokkan URL dengan fungsi yang sesuai di views.py. Views.py memproses request tersebut dengan membaca atau menulis data melalui models.py, yang mewakili tabel di database menggunakan ORM. Setelah memproses data, views.py akan menggabungkannya dengan template HTML dan mengirimkan respons yang sesuai kepada pengguna.

## Jelaskan fungsi git dalam pengembangan perangkat lunak!

=> Git memiliki banyak sekali fungsi dalam pengembangan perangkat lunak. Menurut saya, salah satu fitur yang sangat krusial adalah Git memungkinkan banyak developer untuk bekerja pada proyek yang sama secara paralel, tanpa risiko menimpa pekerjaan satu sama lain. Hal ini dapat terjadi dikarenakan setiap orang dapat membuat cabang (branch) yang terpisah, dan kemudian menggabungkannya (merge) ke cabang utama. Selain itu, Git juga menyimpan setiap perubahan dan versi dari kode yang kita buat, sehingga memudahkan jika perlu melakukan penyelesaian konflik.

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

=> Django dapat dijadikan pilihan awal yang bagus untuk permulaan pembelajaran pengembangan perangkat lunak karena mudah dipahami dan punya dokumentasi lengkap. Framework ini menawarkan banyak fitur bawaan, seperti autentikasi pengguna, manajemen database, dan admin panel, sehingga pemula bisa langsung fokus pada pengembangan tanpa banyak konfigurasi. Dengan pola MVC, Django juga membantu pemula memahami struktur kode yang rapi dan terorganisir. Komunitasnya yang besar menyediakan banyak bantuan, dan Django punya fitur keamanan bawaan untuk melindungi aplikasi dari ancaman umum. Selain itu, Django digunakan oleh aplikasi besar, sehingga apa yang dipelajari bisa langsung diterapkan di proyek nyata.

## Mengapa model pada Django disebut sebagai ORM?

=> Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menggunakan teknik ORM untuk menghubungkan antara model Python dan database. ORM memungkinkan developer untuk bekerja dengan database menggunakan objek Python, tanpa harus menulis query SQL secara langsung. Dengan ORM, setiap tabel di database direpresentasikan sebagai sebuah class di Python (model), dan setiap baris di tabel tersebut menjadi instance dari class itu. Django ORM secara otomatis menerjemahkan operasi pada objek model ke dalam operasi SQL yang sesuai, sehingga memudahkan interaksi dengan database tanpa perlu pengetahuan mendalam tentang SQL.