'''Objective: Create a Python program that functions as a personal diary. Users should be able to add entries with the date and time they provide, which are then saved to a file. Detailed Directions Set Up Your Python Environment: Create a diary folder for this assignment, you will upload the whole file to GitHub when you are done. Create a New Python File: Name this file personal_diary.py. Writing the Code: Create this in a main function Prompt the user to enter the current date and time, then a diary entry. Open or create a file named diary.txt in append mode using open(). ( use append not write) Write the user-provided date, time, and diary entry into the file. Ensure each entry is separated from the others by writing a blank line after entering the date/time line and the entry line. Close the file using the close() method. Comments and Documentation: Add comments to your code explaining its functionality. Testing the Program: Run personal_diary.py three times, each time entering a different diary entry along with the date and time. Check diary.txt to ensure entries are recorded correctly. Submission: Submit both your personal_diary.py file and the diary.txt file containing your entries. '''

def main():
    date_time = input("Enter the current date and time: ") # Prompt user for date and time
    entry = input("Enter a diary entry: ") # Prompt user for diary entry

    diary = open('PE2/4.2/diary.txt', 'a') # Open diary file in append mode

    diary.write(date_time + "\n" + entry + "\n\n") # Write date/time and entry with newlines for formatting
    diary.close() # Close file

if __name__ == "__main__":
    main()
