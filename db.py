import sqlite3

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

