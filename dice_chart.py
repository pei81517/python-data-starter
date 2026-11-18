import random

rolls = 10000
# A dictionary to count every sum from 2 to 12
counts = {total: 0 for total in range(2, 13)}

for i in range(rolls):
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    counts[dice_total] += 1

print("--- 10,000 DICE ROLLS DISTRIBUTION ---")
for total, count in counts.items():
    bars = "█" * (count // 50)
    print(f"Sum {total:2}: {bars} ({count})")