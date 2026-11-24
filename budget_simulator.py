import random

def run_monte_carlo_savings(
    starting_balance=1200,
    monthly_income=950,
    avg_expense=620,
    expense_volatility=110,
    months=12,
    goal=5000,
    simulations=5000
):
    final_balances = []
    goals_met = 0

    for _ in range(simulations):
        balance = starting_balance
        for _ in range(months):
            # Sample realistic monthly spending using a Gaussian (bell curve) distribution
            monthly_spend = max(250, random.gauss(avg_expense, expense_volatility))
            balance += (monthly_income - monthly_spend)

        final_balances.append(balance)
        if balance >= goal:
            goals_met += 1

    final_balances.sort()
    p10 = final_balances[int(0.10 * simulations)]
    p50 = final_balances[int(0.50 * simulations)]
    p90 = final_balances[int(0.90 * simulations)]
    success_rate = (goals_met / simulations) * 100

    print("=== MONTE CARLO SAVINGS & RISK SIMULATOR ===")
    print(f"Starting Balance: ${starting_balance:,.2f} | Target Goal: ${goal:,.2f} ({months} months)")
    print(f"Monthly Income:   ${monthly_income:,.2f} | Avg Expense: ${avg_expense:,.2f} (±${expense_volatility})")
    print(f"Simulations Run:  {simulations:,}\n")
    print(f"10th Percentile (Worst-Case):  ${p10:,.2f}")
    print(f"50th Percentile (Median):      ${p50:,.2f}")
    print(f"90th Percentile (Best-Case):   ${p90:,.2f}")
    print("-" * 52)
    print(f"Probability of Reaching ${goal:,.2f} Goal: {success_rate:.1f}%")

run_monte_carlo_savings()