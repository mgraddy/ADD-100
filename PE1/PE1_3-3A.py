'''In this exercise, you will practice using logical operators (and, or, not) in Python. Your task is to create a program that prompts the user for two integer inputs and then demonstrate the use of these operators.
User Input: Start by asking the user to input two distinct integers. 
Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators: and or not
Display Results: Print the logical statement and its result for each comparison.
Guidelines for Logical Comparisons:
Ensure that your comparisons are meaningful and not too obvious (e.g., avoid comparisons like num1 == num1).
Try to use comparisons that could yield different results based on user input.'''

# Ask for two distinct integers
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

if a % 2 == 0 and b % 2 == 0:
    print("Both numbers are even.")
elif not a & 2 == 0 and b & 2 == 0:
    print("Both numbers are odd.")
else:
    print("One number is odd and one number is even.")
if not a == b:
    print("Number 1 is not equal to Number 2.")
else:
    print("Number 1 is equal to Number 2.")
if a > 100 or b > 100:
    print("At least one number is greater than 100.")
else:
    print("Neither number is greater than 100.")
if not a == 0 or b == 0:
    print("Neither number is 0.")
else:
    print("At least one number is 0.")
if a < 0 or b < 0:
    print("At least one number is negative.")
else:
    print("Neither number is negative.")