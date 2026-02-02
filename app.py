from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'arsipakta123'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

# =========================
# KONEKSI DATABASE
# =========================
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# =========================
# LOGIN
# =========================
@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('login'):
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return "Username dan password wajib diisi!"

        db = get_db()
        user = db.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (username, password)
        ).fetchone()
        db.close()

        if user:
            session['login'] = True
            session['username'] = user['username']
            return redirect(url_for('dashboard'))

        return "Login gagal! Username atau password salah."

    return render_template('login.html')

# =========================
# DASHBOARD
# =========================
@app.route('/dashboard')
def dashboard():
    if not session.get('login'):
        return redirect(url_for('login'))

    db = get_db()
    data = db.execute(
        "SELECT * FROM akta_kelahiran ORDER BY id DESC"
    ).fetchall()
    db.close()

    return render_template('dashboard.html', data=data)

# =========================
# TAMBAH DATA
# =========================
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if not session.get('login'):
        return redirect(url_for('login'))

    if request.method == 'POST':
        nama = request.form.get('nama')
        nik = request.form.get('nik')
        tanggal = request.form.get('tanggal')
        no_akta = request.form.get('no_akta')

        if not all([nama, nik, tanggal, no_akta]):
            return "Semua field wajib diisi!"

        db = get_db()
        db.execute("""
            INSERT INTO akta_kelahiran (nama, nik, tanggal_lahir, no_akta)
            VALUES (?, ?, ?, ?)
        """, (nama, nik, tanggal, no_akta))
        db.commit()
        db.close()

        return redirect(url_for('dashboard'))

    return render_template('tambah.html')

# =========================
# EDIT DATA
# =========================
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if not session.get('login'):
        return redirect(url_for('login'))

    db = get_db()

    if request.method == 'POST':
        nama = request.form.get('nama')
        nik = request.form.get('nik')
        tanggal = request.form.get('tanggal')
        no_akta = request.form.get('no_akta')

        if not all([nama, nik, tanggal, no_akta]):
            return "Semua field wajib diisi!"

        db.execute("""
            UPDATE akta_kelahiran
            SET nama=?, nik=?, tanggal_lahir=?, no_akta=?
            WHERE id=?
        """, (nama, nik, tanggal, no_akta, id))
        db.commit()
        db.close()

        return redirect(url_for('dashboard'))

    data = db.execute(
        "SELECT * FROM akta_kelahiran WHERE id=?",
        (id,)
    ).fetchone()
    db.close()

    if not data:
        return "Data tidak ditemukan!"

    return render_template('edit.html', data=data)

# =========================
# HAPUS DATA
# =========================
@app.route('/hapus/<int:id>')
def hapus(id):
    if not session.get('login'):
        return redirect(url_for('login'))

    db = get_db()
    db.execute("DELETE FROM akta_kelahiran WHERE id=?", (id,))
    db.commit()
    db.close()

    return redirect(url_for('dashboard'))

# =========================
# LOGOUT
# =========================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# =========================
# RUN
# =========================
if __name__ == '__main__':
    app.run(debug=True)
