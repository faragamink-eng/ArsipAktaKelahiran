import sqlite3
import os

DB_NAME = "database.db"

# Hapus database lama kalau rusak
if os.path.exists(DB_NAME):
    print("Database lama ditemukan.")
else:
    print("Membuat database baru...")

conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

# Buat tabel admin
c.execute("""
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Buat tabel akta kelahiran
c.execute("""
CREATE TABLE IF NOT EXISTS akta_kelahiran (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT,
    nik TEXT,
    tanggal_lahir TEXT,
    no_akta TEXT
)
""")

# Cek apakah admin sudah ada
c.execute("SELECT * FROM admin WHERE username='admin'")
if not c.fetchone():
    c.execute("INSERT INTO admin (username, password) VALUES (?, ?)", ('admin', 'admin'))
    print("User admin berhasil dibuat.")
else:
    print("User admin sudah ada.")

conn.commit()
conn.close()

print("Database siap digunakan!")
