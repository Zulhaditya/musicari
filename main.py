from fingerprint import extract_fingerprint
from db import save_fingerprint

file_path = "dataset/follow-you.wav"
title = "Follow You"

fingerprint = extract_fingerprint(file_path)
save_fingerprint(title, fingerprint)

print(f"Fingerprint untuk {title} berhasil disimpan!")
