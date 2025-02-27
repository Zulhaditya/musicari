# Musicari

## API

### Tambahkan Lagu
- curl -X POST -F "audio=@dataset/follow-you.wav" -F "title=No Surprises" http://127.0.0.1:5000/add_song

### Cari Lagu
- curl -X POST -F "audio=@dataset/follow-you.wav" http://127.0.0.1:5000/find_song

### Hapus Lagu
- curl -X DELETE http://127.0.0.1:5000/delete_song \
     -H "Content-Type: application/json" \
     -d '{"title": "Follow You"}'
