#Declaration of variables
monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
rate = 0.05

#Performing calculations
monthly_savings = int(monthly_income - total_monthly_expenses)
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#Outputing results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")