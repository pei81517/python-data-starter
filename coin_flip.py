import random
flip = 10000
heads = 0
current_streak = 0
longest_streak = 0
for _ in range(flip):
    result = random.choice(["heads", "tails"])
    if result == "heads":
        heads += 1
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
percentage = (heads / flip) * 100
print(f"Heads: {heads}/{flip} ({percentage:.1f}%)")
print(f"Longest streak of heads: {longest_streak}")