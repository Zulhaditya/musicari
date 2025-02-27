from db import get_all_fingerprints

def match_song(fingerprint_hash):
    # Cocokkan fingerprint sebuah lagu dengan database
    results = get_all_fingerprints()

    for title, stored_fingerprint in results:
        if fingerprint_hash == stored_fingerprint:
            return title
    
    return None
