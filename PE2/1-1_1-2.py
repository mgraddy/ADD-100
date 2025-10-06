'''In this assignment, you will create a Python program that generates a random number between 1 and 100. Your program should allow the user to guess the number, and provide feedback on how close their guess is to the actual number.

Assignment Objectives:
Use the random module to generate a random number.
Implement a while loop to allow continuous guessing until the correct number is guessed.
Use the abs() function to determine the difference between the guess and the actual number.
Provide feedback based on the proximity of the guess to the actual number:
If the difference is within 5, print "Very Hot".
If the difference is within 15, print "Hot".
If the difference is within 25, print "Cool".
If the difference is more than 25, print "Cold".
Make sure to call the main function!
After completing the program, upload it to your GitHub repository.
Submit the link to your GitHub repository in Canvas.'''

import random
def main():
    guess = -1
    random_int = random.randint(1,100)
    while guess != random_int:
        guess = int(input("Guess a number: "))
        if abs(random_int - guess) <= 5:
            print("Very Hot")
        elif abs(random_int - guess) <= 15:
            print("Hot")
        elif abs(random_int - guess) <= 25:
            print("Cool")
        else:
            print("Cold")
    print("Congratulations, you found the number!")
main()