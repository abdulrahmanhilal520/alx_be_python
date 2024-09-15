monthly_income = float(input("Enter your monthly income"))
monthly_expenses = float(input("Enter your monthly expenses"))

monthly_savings = monthly_income - monthly_expenses

print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Annual interest rate (assuming simple interest for simplicity)
annual_interest_rate = 0.05  # 5%

# Calculate projected annual savings with interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print projected annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
