from flask import Flask, request, jsonify
from fingerprint import extract_fingerprint
from match import match_song

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
