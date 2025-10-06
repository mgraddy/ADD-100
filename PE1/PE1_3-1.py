'''Write a Python program that uses if-else statements and:
Asks the user for their age and converts the input to an integer.
Check to see if the user is old enough to drive.
Check to see if the user can vote.
Check to see if the user can legally buy alcohol.
Check to see if the user is eligible for a senior discount.
Prints all the results on the screen, ensuring the output is straightforward and user-friendly.'''

# Ask user for age and convert to int
age = int(input("Enter your age: "))

# Check if old enough to drive and print result
if age >= 16:
    print("User is old enough to drive.")
else:
    print("User is not old enough to drive.")

# Check if old enough to vote and print result
if age >= 18:
    print("User is old enough to vote.")
else:
    print("User is not old enough to vote.")

# Check if old enough to purchase alcohol and print result
if age >= 21:
    print("User is old enough to purchase alcohol.")
else:
    print("User is not old enough to purchase alcohol.")

# Check if eligible for senior discount and print result
if age >= 55:
    print("User is eligible for a senior discount.")
else:
    print("User is not eligible for a senior discount.")