import sqlite3
import os

# Koneksi ke database
conn = sqlite3.connect("music_fingerprint.db", check_same_thread=False)
cursor = conn.cursor()

# Buat tabel fingerprints jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS fingerprints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    fingerprint BLOB
)
""")
conn.commit()

# Fungsi simpan fingerprint
def save_fingerprint(title, fingerprint_hash):
    cursor.execute("INSERT INTO fingerprints (title, fingerprint) VALUES (?, ?)", (title, fingerprint_hash))
    conn.commit()

# Fungsi mengambil semua fingerprint
def get_all_fingerprints():
    cursor.execute("SELECT title, fingerprint FROM fingerprints")
    return cursor.fetchall()

# Fungsi menghapus fingerprint dan lagu berdasarkan judul
def delete_fingerprint(title):
    # Ambil nama file dari database sebelum menghapus
    cursor.execute("SELECT title FROM fingerprints WHERE title = ?", (title,))
    song = cursor.fetchone()
    
    if song:
        # Hapus dari database
        cursor.execute("DELETE FROM fingerprints WHERE title = ?", (title,))
        conn.commit()
        
        # Hapus file dari folder uploads
        file_path = os.path.join("uploads", f"{title}.wav")
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return True
    return False

