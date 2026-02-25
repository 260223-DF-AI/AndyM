# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro

"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()


# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")


# Get monthly income (as a float)
# Remember to convert the input to a float!

#
# function accepts a string (expense type) and gets input for it, verifies if its valid
# and returns it converted as a float if valid
def get_expense(expense_type, is_expense = True):
    ans = input(f"Enter your {expense_type}: ")
    if is_expense:
        return max(0,float(ans)) # if their answer is negative for an expense, set it to 0
    else:
        return float(ans)

# Get expenses for at least 4 categories:
# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)

# get name, monthly income, and 4 types of expenses using get_expese function
name = input("Enter your name: ")
if name == "":
    name = "Anonymous"

monthly_income = get_expense("Monthly Income", False)
if monthly_income < 0:
    print("error, monthly income is negative")
    exit(-1)

rent = get_expense("Rent costs")
utilities = get_expense("utilities costs")
food = get_expense("Food costs")
transportation = get_expense("Transportation costs")



# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses
total_expenses = rent + utilities + transportation + food

# Calculate remaining balance (income - expenses)
remaining_balance = monthly_income - total_expenses

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100
savings_rate = (remaining_balance / monthly_income) * 100

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
financial_status = None
if remaining_balance > 0:
    financial_status = "in the green"
elif remaining_balance < 0:
    financial_status = "in the red"
else:
    financial_status = "breaking even"
# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...
print("="*44)
print("         Monthly Budget Report")
print("="*44)
print(f"Name: {name}")
print(f"Monthly Income: {monthly_income}")
print(f"\nExpenses:\n")
print(f"    - Rent:            ${rent:.2f}")
print(f"    - Food:            ${food:.2f}")
print(f"    - Transportation:  ${transportation:.2f}")
print(f"    - Utilities:       ${utilities:.2f}")
print("-" * 44)
print(f"Total Expenses:        ${total_expenses:.2f}")
print(f"Remaining Balance:     ${remaining_balance:.2f}")
print(f"Savings Rate:          {savings_rate:.2f}%")
print(f"\nSTATUS: {financial_status}")
print("="*44)



# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
