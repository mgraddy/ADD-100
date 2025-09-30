'''Objective: Enhance a basic Python program by implementing try and except statements to handle errors in user input, focusing on data type errors.
Instructions
Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
Identify Potential Errors: Consider errors that might occur with non-numeric input.
Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message.
Test Your Code: Ensure the exception handling works correctly with various inputs.
GitHub Upload: Upload your py file to GitHub and hand in the link'''

# Simple Python program to calculate the square of a number

def square_number():
    number_input = input("Enter a number to square: ")
    try: # try turning input into an integer
        number_int = int(number_input)
    except ValueError: # Runs if input is not a number
        print(f"Error: '{number_input}' is not a valid number. Please enter a numeric value.")
    else: # Runs if input is a number
        squared_number = number_int ** 2
        print(f"The square of {number_input} is {squared_number}.")

square_number()

