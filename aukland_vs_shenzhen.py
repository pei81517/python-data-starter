import pandas as pd
import matplotlib.pyplot as plt

# Monthly average temperatures (°C) for Auckland vs. Shenzhen
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Auckland": [20.1, 20.4, 19.2, 16.9, 14.4, 12.1, 11.2, 11.7, 13.1, 14.7, 16.5, 18.5],
    "Shenzhen": [15.4, 16.3, 19.0, 22.7, 26.0, 28.0, 28.9, 28.7, 27.7, 25.3, 21.2, 17.0]
}

df = pd.DataFrame(data)
df["Difference"] = df["Shenzhen"] - df["Auckland"]

print(df)
print("\nAverage Annual Temp:")
print(df[["Auckland", "Shenzhen"]].mean().round(1))

# Plot a publication-style comparison chart
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Auckland"], marker="o", linewidth=2.5, label="Auckland, NZ", color="#1f77b4")
plt.plot(df["Month"], df["Shenzhen"], marker="s", linewidth=2.5, label="Shenzhen, China", color="#d62728")

plt.title("Monthly Average Temperature: Auckland vs. Shenzhen", fontsize=14, fontweight="bold")
plt.xlabel("Month", fontsize=11)
plt.ylabel("Temperature (°C)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

# Save as a high-resolution PNG and display it
plt.savefig("auckland_vs_shenzhen.png", dpi=300)
plt.show()