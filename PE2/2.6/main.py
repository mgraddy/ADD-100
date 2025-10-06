def main(): # simple program to calculate grade percentage

    print("---Test Score Calculator---")
    
    try:
        score = int(input("Enter the student's score: "))
        total_possible = int(input("Enter the total possible points: "))
        percentage = (score / total_possible) * 100
        print(f"The student's percentage is: {percentage:.2f}%")

    except ValueError: # runs if user enters decimal numbers and int() fails
        print("Error: Please enter only whole numbers for the score and total.")
        
    except ZeroDivisionError: # runs if user enters zero for total_possible
        print("Error: The total possible points cannot be zero.")

main()