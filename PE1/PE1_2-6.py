'''Create a Python application that allows users to input their total budget and the amount spent in various categories. The program will then calculate and display the percentage of the total budget each category represents.'''

# Ask user for Total Budget (monthly income)
budget = float(input("Enter net monthly income: "))

# Ask user for spending categories
housing = float(input("Enter amount spent on housing: "))
utilities = float(input("Enter amount spent on utilities: "))
groceries = float(input("Enter amount spent on groceries: "))
transportation = float(input("Enter amount spent on transportation: "))
health_care = float(input("Enter amount spent on health care: "))
personal_care = float(input("Enter amount spent on personal care: "))
clothing = float(input("Enter amount spent on clothing: "))
debt = float(input("Enter amount spent on debt: "))

# Calculate percentage of total budget spent in each category
housing_pct = (housing / budget) * 100
utilities_pct = (utilities / budget) * 100
groceries_pct = (groceries / budget) * 100
transportation_pct = (transportation / budget) * 100
health_care_pct = (health_care / budget) * 100
personal_care_pct = (personal_care / budget) * 100
clothing_pct = (clothing / budget) * 100
debt_pct = (debt / budget) * 100

# Calculate total money spent and total money remaining
total_spending = housing + utilities + groceries + transportation + health_care + personal_care + clothing + debt
total_left = budget - total_spending

# Print results to the user
print(f"The total amount spent on expenses is ${total_spending:.2f}")
print(f"The amount remaining after expenses is ${total_left:.2f}")