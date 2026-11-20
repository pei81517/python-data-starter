# DJ Track Compatibility & BPM Analyzer
# Evaluates whether two tracks can be smoothly beatmatched and harmonically mixed

# Standard musical keys mapped to Camelot Wheel codes for harmonic mixing
CAMELOT_WHEEL = {
    "Abm": "1A", "B": "1B",
    "Ebm": "2A", "Gb": "2B", "F#": "2B",
    "Bbm": "3A", "Db": "3B", "C#": "3B",
    "Fm": "4A",  "Ab": "4B",
    "Cm": "5A",  "Eb": "5B",
    "Gm": "6A",  "Bb": "6B",
    "Dm": "7A",  "F": "7B",
    "Am": "8A",  "C": "8B",
    "Em": "9A",  "G": "9B",
    "Bm": "10A", "D": "10B",
    "Gbm": "11A", "F#m": "11A", "A": "11B",
    "Dbm": "12A", "C#m": "12A", "E": "12B"
}

def check_bpm_compatibility(bpm1, bpm2):
    """Checks direct BPM difference as well as half-time / double-time ratios."""
    ratios = [1.0, 2.0, 0.5]
    best_diff = min(abs(bpm1 - (bpm2 * r)) for r in ratios)
    percent_shift = (best_diff / bpm1) * 100
    
    if percent_shift <= 5.0:
        return True, f"Great match ({percent_shift:.1f}% tempo shift needed)"
    elif percent_shift <= 8.0:
        return True, f"Workable with SYNC ({percent_shift:.1f}% tempo shift)"
    else:
        return False, f"Too far apart ({percent_shift:.1f}% tempo shift)"

def check_key_compatibility(key1, key2):
    """Uses Camelot Wheel rules: same code, +/- 1 number, or A/B relative switch."""
    c1 = CAMELOT_WHEEL.get(key1)
    c2 = CAMELOT_WHEEL.get(key2)
    
    if not c1 or not c2:
        return False, "Unknown key"
    if c1 == c2:
        return True, f"Perfect harmonic match ({c1} -> {c2})"
    
    num1, mode1 = int(c1[:-1]), c1[-1]
    num2, mode2 = int(c2[:-1]), c2[-1]
    
    if num1 == num2 and mode1 != mode2:
        return True, f"Relative major/minor switch ({c1} -> {c2})"
    if mode1 == mode2 and (abs(num1 - num2) == 1 or {num1, num2} == {1, 12}):
        return True, f"Smooth energy boost/drop ({c1} -> {c2})"
    
    return False, f"Key clash risk ({c1} vs {c2})"

def evaluate_transition(track_a, track_b):
    bpm_ok, bpm_msg = check_bpm_compatibility(track_a["bpm"], track_b["bpm"])
    key_ok, key_msg = check_key_compatibility(track_a["key"], track_b["key"])
    
    print(f"\nMixing: '{track_a['title']}' ({track_a['bpm']} BPM, {track_a['key']})")
    print(f"   -->  '{track_b['title']}' ({track_b['bpm']} BPM, {track_b['key']})")
    print(f"  * Tempo: {bpm_msg}")
    print(f"  * Key:   {key_msg}")
    
    if bpm_ok and key_ok:
        print("  => VERDICT: Seamless Club Transition!")
    elif bpm_ok:
        print("  => VERDICT: Beatmatch works—use drum/outro loop to avoid vocal clash.")
    else:
        print("  => VERDICT: Hard cut or echo-out recommended.")

if __name__ == "__main__":
    playlist = [
        {"title": "Get Up (Ciara)", "bpm": 129, "key": "Eb"},
        {"title": "Whine Up (Kat DeLuna)", "bpm": 125, "key": "E"},
        {"title": "Don't Stop The Music (Rihanna)", "bpm": 123, "key": "A"},
        {"title": "Move Ya Body (Nina Sky)", "bpm": 121, "key": "Gb"},
        {"title": "Strangers (Half-Time)", "bpm": 65, "key": "F"}
    ]
    
    evaluate_transition(playlist[0], playlist[1])
    evaluate_transition(playlist[2], playlist[3])
    evaluate_transition(playlist[0], playlist[4])