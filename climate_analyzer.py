import csv

print("--- AUCKLAND VS. SHENZHEN CLIMATE ANALYZER ---")

auckland_temps = []
shenzhen_temps = []
biggest_gap = 0
biggest_gap_month = ""

with open("climate_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row["Month"]
        akl = float(row["Auckland_C"])
        sz = float(row["Shenzhen_C"])

        auckland_temps.append(akl)
        shenzhen_temps.append(sz)

        diff = round(abs(sz - akl), 1)
        print(f"{month}: Auckland {akl:4.1f}°C | Shenzhen {sz:4.1f}°C | Gap: {diff:4.1f}°C")

        if diff > biggest_gap:
            biggest_gap = diff
            biggest_gap_month = month

akl_avg = round(sum(auckland_temps) / len(auckland_temps), 1)
sz_avg = round(sum(shenzhen_temps) / len(shenzhen_temps), 1)

akl_swing = round(max(auckland_temps) - min(auckland_temps), 1)
sz_swing = round(max(shenzhen_temps) - min(shenzhen_temps), 1)

print("\n--- SUMMARY STATS ---")
print(f"Auckland Annual Avg: {akl_avg}°C (Seasonal Swing: {akl_swing}°C)")
print(f"Shenzhen Annual Avg: {sz_avg}°C (Seasonal Swing: {sz_swing}°C)")
print(f"Largest Monthly Gap: {biggest_gap_month} ({biggest_gap}°C difference)")