#Declaration of variables
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
rate = 0.05

#Performing calculations
monthly_savings = monthly_income - monthly_expenses
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#Outputing results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")