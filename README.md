 📌 Sistem Arsip Data Akta Kelahiran Berbasis Web

**Dinas Kependudukan dan Pencatatan Sipil**


## 🗂️ Deskripsi Sistem

Sistem Arsip Data Akta Kelahiran Berbasis Web merupakan aplikasi yang dikembangkan untuk membantu proses pengelolaan, penyimpanan, pencarian, dan pemeliharaan data arsip akta kelahiran secara digital. Sistem ini bertujuan untuk meningkatkan efisiensi kerja, keamanan data, serta kemudahan akses informasi pada Dinas Kependudukan dan Pencatatan Sipil.

Aplikasi ini dibangun menggunakan **bahasa pemrograman Python** dengan framework **Flask** dan menggunakan **SQLite** sebagai basis data.

---

## ⚙️ Teknologi yang Digunakan

* Python 3.x
* Flask
* SQLite
* HTML & CSS
* Bootstrap 5

---

## 📁 Struktur Folder

```
arsip/
│
├── app.py
├── database.db
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── tambah.html
│   └── edit.html
│
├── static/
│   └── css/
│
└── README.md
```

---

## 🛠️ Instalasi Sistem

### 1️⃣ Persyaratan Sistem

Pastikan perangkat telah terpasang:

* Python versi 3.x
* PIP (Python Package Manager)

Cek instalasi Python:

```bash
python --version
```

---

### 2️⃣ Instalasi Library Flask

Jalankan perintah berikut pada terminal atau command prompt:

```bash
pip install flask
```

---

### 3️⃣ Menjalankan Aplikasi

Jalankan aplikasi dengan perintah:

```bash
python app.py
```

Jika berhasil, aplikasi akan berjalan pada alamat:

```
http://127.0.0.1:5000
```

---

## 🔐 Akun Login Default

Gunakan akun berikut untuk masuk ke sistem:

* **Username:** admin
* **Password:** admin

---

## 📌 Panduan Penggunaan Sistem

### 1. Login

Pengguna melakukan login menggunakan akun admin untuk dapat mengakses sistem.

---

### 2. Dashboard

Dashboard menampilkan daftar arsip akta kelahiran dalam bentuk **card**, yang berisi informasi:

* Nomor Akta
* Nama
* NIK
* Tanggal Lahir

---

### 3. Tambah Data Akta

Admin dapat menambahkan data akta kelahiran dengan mengisi:

* Nama
* NIK
* Tanggal Lahir
* Nomor Akta

---

### 4. Edit Data Akta

Admin dapat memperbarui data arsip akta kelahiran yang telah tersimpan di dalam sistem.

---

### 5. Hapus Data Akta

Admin dapat menghapus data arsip akta kelahiran yang tidak diperlukan.

---

### 6. Logout

Admin dapat keluar dari sistem dengan menekan tombol **Logout**.

## 🔒 Keamanan Sistem
* Sistem menggunakan **session login** untuk membatasi akses pengguna.
* Data disimpan secara lokal menggunakan **database SQLite**.
* Hanya pengguna yang telah login yang dapat mengakses dashboard dan fitur pengelolaan data.

