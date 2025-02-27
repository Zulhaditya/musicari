import os
from flask import Flask, request, jsonify
from db import get_all_fingerprints, save_fingerprint
from fingerprint import extract_fingerprint
from match import match_song

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# API untuk menambahkan lagu ke database
@app.route('/add_song', methods=['POST'])
def add_song():
    if 'audio' not in request.files or 'title' not in request.form:
        return jsonify({"status": "error", "message": "Audio file tidak ada"}), 400
    
    audio_file = request.files['audio']
    title = request.form['title']

    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    fingerprint_hash = extract_fingerprint(file_path)
    save_fingerprint(title, fingerprint_hash)

    return jsonify({"status": "success", "message": f"Fingerprint untuk lagu {title} dibuat!"})

# API untuk mencari lagu
@app.route('/find_song', methods=['POST'])
def find_song():
    file = request.files['audio']
    file_path = "temp/input.wav"
    file.save(file_path)

    fingeprint = extract_fingerprint(file_path)
    title = match_song(fingeprint)

    if title:
        return jsonify({"status": "success", "song": title})
    
    return jsonify({"status": "not found"})

# API untuk melihat lagu yang telah terdaftar di database
@app.route('/list_songs', methods=['GET'])
def list_songs():
    songs = get_all_fingerprints()
    song_list = [{"title": song[0]} for song in songs]
    return jsonify({"status": "success", "songs": song_list})

if __name__ == "__main__":
    app.run(debug=True)
