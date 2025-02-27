import librosa
import numpy as np
import hashlib

def extract_fingerprint(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    
    # Gunakan metode hashing agar hasil fingerprint lebih unik dan optimal
    fingerprint = np.mean(mfccs, axis=1)
    fingerprint_hash = hashlib.sha256(fingerprint.tobytes()).hexdigest()

    return fingerprint_hash
