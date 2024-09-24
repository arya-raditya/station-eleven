# Tugas Week 4

## Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect() dan redirect() di Django sama-sama digunakan untuk melakukan pengalihan (redirect) ke URL lain, namun perbedaannya terletak pada fleksibilitasnya. HttpResponseRedirect() membutuhkan URL lengkap atau relatif secara manual, sedangkan redirect() lebih fleksibel karena bisa menerima URL, nama URL pattern, atau objek model yang memiliki get_absolute_url(). Kelebihan redirect() adalah kemudahan dan fleksibilitas penggunaannya, sedangkan HttpResponseRedirect() lebih cocok jika URL sudah diketahui secara pasti.

## Jelaskan cara kerja penghubungan model Product dengan User!

Pada implementasi ini, digunakan ForeignKey untuk menghubungkan model Product dengan User. Penghubungan model Product dengan User menggunakan ForeignKey memungkinkan setiap Product terhubung ke satu User, sementara satu User bisa memiliki banyak Product. Implementasinya melibatkan menambahkan field user = models.ForeignKey(User, on_delete=models.CASCADE) di model Product, di mana on_delete=models.CASCADE memastikan produk terkait akan dihapus jika user dihapus. Ini mempermudah pengelolaan produk berdasarkan pengguna, misalnya dengan mengambil semua produk milik user tertentu menggunakan user.product_set.all(). Relasi ini cocok jika setiap produk hanya dimiliki oleh satu user.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses memverifikasi identitas pengguna, seperti saat login dengan username dan password untuk memastikan pengguna sah. Authorization adalah proses menentukan apa yang boleh diakses atau dilakukan oleh pengguna setelah berhasil login, seperti memberi akses ke halaman tertentu. Di Django, authentication dilakukan dengan fungsi seperti authenticate() dan login(), sementara authorization diatur melalui izin (permissions) dan dekorator seperti @login_required, memastikan hanya pengguna yang sudah terotentikasi bisa mengakses area tertentu sesuai dengan haknya.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login menggunakan cookies, khususnya session cookies, yang menyimpan session ID di browser setelah pengguna berhasil login. Setiap kali pengguna mengakses halaman, cookie ini dikirim kembali ke server, memungkinkan Django untuk memverifikasi identitas pengguna dan mempertahankan sesi mereka. Selain itu, cookies memiliki kegunaan lain seperti menyimpan preferensi pengguna, melacak aktivitas, dan personalisasi iklan. Namun, tidak semua cookies aman; risiko seperti cookies tidak terenkripsi, penyimpanan informasi sensitif, dan serangan XSS dapat mengancam keamanan. Namun, pada Django, Django membantu mengatasi risiko ini dengan menggunakan secure cookies dan HttpOnly cookies, tetapi pengembang perlu berhati-hati dalam pengelolaan dan perlindungan cookies.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Dalam tugas kali ini, fokus yang hendak dilakukan adalah mengimplementasikan authentication dan authorization pada app yang hendak dibuat. Untuk mengimplementasi authentication, perlu dilakukan pengimplementasian register, login, dan logout. Saya mengimport fungsi UserCreationForm dan AuthenticationForm untuk memudahkan pembuatan. UserCreationForm digunakan ketika mengimplementasikan fungsi register, sehingga sistem akan otomatis membuat user baru setiap dilakukan register, kemudian AuthenticationForm digunakan pada fungsi login, sehingga user yang telah dibuat tadi bisa digunakan seterusnya. Selain itu, pada models.py, ditambahkan user = models.ForeignKey(User, on_delete=models.CASCADE) untuk menghubungkan setiap data yang diinput pada user bersangkutan.

Setelah mengimplementasi authentication, selanjutnya dilakukan implementasi authorization. Hal ini dieksekusi dengan menambahkan decorator @login_required(login_url='/login') di fungsi show main. Fungsi ini  membuat setiap browser yang ingin mengakses show_main memerlukan user login terlebih dahulu, sehingga akan automatis ter-direct ke login page jika belum login. Hal ini merestriksi setiap browser yang hendak mencoba mengakses app, di mana apabila browser tersebut belum login menggunakan usernamenya, maka akses terhadap show_main akan dihalangi. Terdapat modifikasi pula pada product_list menjadi Product.objects.filter(user=request.user), sehingga user hanya bisa melihat produk yang mereka input sendiri.

Kemudian, setelah setiap fungsi selesai dibuat, saya menambahkan html untik regist page dan login page, serta mengubungkan setiap fungsi yang baru dibuat di views.py ke urls.py. Setelahnya, dilakukan migration dan pengecekan apakah sudah dapat berjalan dengan baik di localhost. Setelah berhasil, dilakukan push ke github dan pws.


# Tugas Week 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dalam sebuah platform adalah proses pengiriman dan penerimaan data antara pengguna dan server. Proses ini penting karena memastikan bahwa data yang dimasukkan oleh pengguna bisa dikirim ke server untuk diproses, dan hasilnya bisa dikirim kembali ke pengguna. Ini dapat menjadi dasar dari interaksi antara pengguna dan aplikasi.

Dalam Django, data delivery sering terjadi ketika pengguna mengisi form di web dan mengirimkannya. Form tersebut akan mengirimkan data ke server melalui request HTTP (biasanya POST atau GET). Django kemudian menerima data ini, memprosesnya, dan memberikan respons kembali kepada pengguna, dalam tugas ini, outputnya adalah menampilkan isian form dalam tabel.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON (JavaScript Object Notation) dan XML (eXtensible Markup Language) adalah dua format yang digunakan untuk menyimpan dan mentransfer data. Meskipun keduanya memiliki fungsionalitas yang mirip, saya sendiri lebih menyukasi melihat data berformat JSON. Beberapa alasan yang melatarbelakangi hal ini di antaranya adalah kesederhanaan format yang lebih mudah dibaca jika dibandingkan dengan XML. 

JSON bisa jadi lebih populer dari XML karena alasan yang sama, yaitu lebih sederhana, ringkas, dan mudah dibaca baik oleh manusia maupun mesin. Selain itu, JSON menghasilkan ukuran file yang lebih kecil, lebih cepat diparsing, dan lebih mudah diintegrasikan dengan bahasa pemrograman modern, terutama di lingkungan web. Selain itu, JSON lebih sesuai untuk kebutuhan data sederhana yang sering ditemui di API dan aplikasi web, sementara XML menawarkan kompleksitas yang biasanya tidak diperlukan dalam banyak kasus. Popularitas JSON juga didukung oleh penggunaannya yang luas dalam API REST dan teknologi web modern.

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django digunakan untuk memvalidasi data yang dikirim oleh pengguna melalui form. Ketika pengguna mengisi form dan mengirimkannya, Django perlu memastikan bahwa data yang diterima sesuai dengan aturan atau kriteria yang telah ditetapkan. Dengan ini, data yang akan diproses oleh Django hanya data yang sudah dipastikan valid saja.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang mencoba mengeksploitasi sesi autentikasi pengguna yang sudah login di sebuah situs web untuk melakukan aksi yang tidak diinginkan tanpa sepengetahuan pengguna.

Jika form Django tidak menyertakan csrf_token, aplikasi akan menjadi rentan terhadap serangan CSRF. Penyerang dapat memanfaatkan sesi pengguna yang sedang login untuk mengirimkan permintaan berbahaya ke server tanpa sepengetahuan pengguna. Contohnya, penyerang bisa membuat form di situs mereka sendiri yang mengirimkan data ke server aplikasi yang kita buat, sehingga melakukan aksi seperti mengubah pengaturan akun, melakukan transfer dana, atau menghapus data penting. Tanpa perlindungan csrf_token, seorang penyerang dapat mengelabui pengguna yang sedang login dan melakukan tindakan illegal.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

=> Ada dua task utama yang perlu dikerjakan di minggu ketiga ini, yaitu menambahkan fungsionalitas forms dan menambahkan pengembalian data dalam XML dan JSON. 

Pertama, untuk menambahkan forms, saya memulainya dari membenahi model. Setiap entri perlu memiliki primary key, sehingga saya membuat suatu atribut baru sebagai primary key pada model yang telah saya buat, yaitu UUID. Atribut ini dipastikan unik dan digenerate secara otomatis setiap ditambahkan entri baru. 

Setelah itu, saya membuat sebuah file baru dengan nama "forms.py". Di dalam file ini saya mendefinisikan suatu class ProductForm yang dapat menerima entri produk baru. forms dan model yang telah dibuat ini diimport ke views.py. Dan di file ini pula, saya membuat suatu metode baru untuk meminta input produk dari user, yaitu create_product_list, dan dihubungkan dengan suatu template html create_product_list.html.

Kemudian, saya memodifikasi sedikit fungsi show_main agar dapat menampilkan isian form, dengan menambahkan 'product_list': product_list ke dalam komponen dictionary. HTML utama (main.html) juga saya modifikasi dengan menambahkan suatu iterasi yang dapat mencetak isian dari form. Terakhir, saya memperbaiki routing di urls.py, dengan menambahkan path baru 'create_product_list' yang akan mendirect ke fungsi create_product_list.

Tugas kedua adalah mengintegrasikan cara melihat data xml dan json. Untuk melakukan hal ini, di views.py saya mengimport HttpResponse dan serializers. Kemudian, saya membuat fungsi-fungsi untuk menunjukkan xml, json, xml by id, dan json by id. Setelahnya, dilakukan routing pada urls.py dengan mengimport fungsi-fungsi yang telah didefinisikan tadi, lalu menambah path yang bersesuaian.

Berikut adalah hasil postmannya:

Melihat data XML:
![xml](./images/tugas3_xml.png)

Melihat data JSON:
![json](./images/tugas3_json.png)

Melihat data XML by id:
![xmlbyid](./images/tugas3_xmlbyid.png)

Melihat data JSON by id:
![jsonbyid](./images/tugas3_jsonbyid.png)


# Tugas Week 2

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

=> 
Pertama, dimulai dengan membuat direktori baru di lokal dengan nama e-commerce yang ingin saya buat, yaitu station-eleven. Kemudian, pada direktori tersebut, diinstall requirements yang telah dilist di requirements.txt. Lalu, project Django diinisiasi dengan “django-admin startproject (nama project)”. Selanjutnya, pada settings.py, ditambahkan localhost ke allowed host.
Pertama, dimulai dengan membuat direktori baru di lokal dengan nama e-commerce yang ingin saya buat, yaitu station-eleven. Kemudian, pada direktori tersebut, diinstall requirements yang telah dilist di requirements.txt. Lalu, project Django diinisiasi dengan “django-admin startproject (nama project)”. Selanjutnya, pada settings.py, ditambahkan localhost ke allowed host.

Kemudian, aplikasi dengan nama main dibuat dengan menjalankan command “python manage.py startapp main”. Setelah berhasil dijalankan, folder dengan nama main akan otomatis dibuat. Untuk melakukan routing pada proyek agar dapat menjalankan aplikasi main, ditambahkan “main” pada installed apps di settings.py.

Lalu, model pada aplikasi main diisi dengan atribut-atribut yang wajib diimplementasi, yaitu nama produk, harga, dan deskripsi. Saya juga menambahkan satu atribut tambahan berupa integer. Selanjutnya, saya membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikas, nama, dan kelas saya. Lalu, saya juga menambahkan contoh produk yang ingin saya tampilkan di e-commerce.
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
