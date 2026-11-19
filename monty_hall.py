import random
import matplotlib.pyplot as plt

trials = 10000
stay_wins = 0
switch_wins = 0

for _ in range(trials):
    # 3 doors: 1 car (prize), 2 goats
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)

    # Player picks a random door (0, 1, or 2)
    player_choice = random.randint(0, 2)

    # Host opens a remaining door that has a goat
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] == "goat"]
    host_opens = random.choice(remaining_doors)

    # The other unopened door if the player switches
    switch_choice = [i for i in range(3) if i != player_choice and i != host_opens][0]

    if doors[player_choice] == "car":
        stay_wins += 1
    if doors[switch_choice] == "car":
        switch_wins += 1

stay_pct = (stay_wins / trials) * 100
switch_pct = (switch_wins / trials) * 100

print(f"After {trials:,} simulations:")
print(f"Stay strategy win rate:   {stay_pct:.1f}%")
print(f"Switch strategy win rate: {switch_pct:.1f}%")

# Plot the comparison
strategies = ["Stay with First Door", "Switch Doors"]
win_rates = [stay_pct, switch_pct]

plt.figure(figsize=(7, 5))
bars = plt.bar(strategies, win_rates, color=["#e74c3c", "#2ecc71"], width=0.5)
plt.title("Monty Hall Problem: 10,000 Simulated Games", fontsize=13, fontweight="bold")
plt.ylabel("Win Percentage (%)")
plt.ylim(0, 80)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{height:.1f}%", ha="center", fontweight="bold")

plt.tight_layout()
plt.savefig("monty_hall_results.png")
plt.show()