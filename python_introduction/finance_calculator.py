# Prompt for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt for total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Print monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Annual interest rate (assuming simple interest for simplicity)
annual_interest_rate = 0.05  # 5%

# Calculate projected annual savings with interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
