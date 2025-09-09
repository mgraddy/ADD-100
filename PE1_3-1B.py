'''Accept a numeric grade from the user and display a letter grade. The  grading scale is  90 - 100: A, 80-89: B, 70-79:C, 60-69:D, Below 60: F
Check to see if the number given is between 0 and 100.  '''

# Ask user for numeric grade and convert to int
grade_num = int(input("Enter the numeric grade: "))

# Determine letter grade
if grade_num < 60:
    grade_letter = 'F'
elif grade_num < 70:
    grade_letter = 'D'
elif grade_num < 80:
    grade_letter = 'C'
elif grade_num < 90:
    grade_letter = 'B'
else:
    grade_letter = 'A'

# Print Result
print("The letter grade is: " + grade_letter)
