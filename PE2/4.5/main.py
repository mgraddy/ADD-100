'''In this assignment, you will create a program that asks the user for their birthday and then calculates their age in different units such as years, months, days, hours, and minutes. This exercise will help you practice using the datetime and timedelta modules in Python. Assignment Objectives: Ask the user to input their birthday. Calculate the user's age in years, months, days, hours, and minutes. Provide detailed comments to all of the code, explaining what each line that has to do with time calculation does. Display the results in a user-friendly format. Implement the solution inside a main() function. Instructions: Create a Python script that performs the following steps: Define a main() function where your program logic will reside. Use my start program from GitHub: startprogramLinks to an external site. You can view the classroom demonstration of how we got to the code at the top of the page. Comment explaining each line of the code Finish the code to get and display: months weeks days (done) years (done) Format and print the results in a clear, understandable manner. Tips: To calculate the age in years, you might need to consider leap years. A simple approach is to divide the total number of days by 365.25. For months, first calculate the years, then use the remaining days to estimate the months. For weeks, calculate by dividing days by 7 Use try-except blocks to handle any potential input errors.'''

# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime

def main():
   
    print("\n\n")
    try:
        today = datetime.today()
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day)
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 

        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
       
        print(f'You are {delta_years} years old')

        months = delta.days // 30.41
        print(f'You are {months} months old')

        weeks = delta.days // 7
        print(f'You are {weeks} weeks old')

        print(f'You are {delta.days} days old')

        hours = delta.days * 24
        print(f'You are {hours} hours old')

        minutes = hours * 60
        print(f'You are {minutes} minutes old')
 
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()
    