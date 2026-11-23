

import math

# 21-day PM2.5 Air Quality readings (ug/m^3) with two sudden spikes
readings = [
    12.4, 13.1, 11.8, 14.0, 12.9, 13.5, 12.2,
    13.8, 14.2, 34.6, 15.1, 13.0, 12.7, 13.4,
    14.1, 12.8, 13.6, 41.2, 16.5, 13.9, 12.5
]

def calc_stats(window):
    mean = sum(window) / len(window)
    variance = sum((x - mean) ** 2 for x in window) / len(window)
    std_dev = math.sqrt(variance)
    return mean, std_dev

def detect_anomalies(data, window_size=5, z_threshold=2.0):
    print("=== ROLLING Z-SCORE AIR QUALITY ANOMALY DETECTOR ===")
    print(f"Baseline Window: {window_size} days | Alert Threshold: Z >= {z_threshold}\n")
    print(f"{'Day':<6} {'PM2.5':>8} {'Baseline':>10} {'StdDev':>8} {'Z-Score':>9} {'Status':>14}")
    print("-" * 60)

    anomalies_found = 0

    for i in range(window_size, len(data)):
        # Look ONLY at the previous 'window_size' days so spikes don't pollute their own baseline
        window = data[i - window_size : i]
        mean, std_dev = calc_stats(window)

        current = data[i]
        z_score = (current - mean) / std_dev if std_dev > 0 else 0.0

        if abs(z_score) >= z_threshold:
            status = "SPIKE ALERT!"
            anomalies_found += 1
        else:
            status = "Normal"

        print(f"Day {i + 1:<2} {current:>7.1f} {mean:>9.2f} {std_dev:>7.2f} {z_score:>8.2f} {status:>14}")

    print("-" * 60)
    print(f"Scan complete: {anomalies_found} anomaly spike(s) detected out of {len(data) - window_size} evaluated days.")

detect_anomalies(readings)