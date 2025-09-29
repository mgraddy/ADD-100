'''Objective: Create a BMI calculator that takes a user's weight and height, calculates their BMI, and categorizes it as underweight, normal weight, overweight, or obese.

Requirements:
Global Variables:
Conversion constants for weight (1 lb = 0.453592 kg) and height (1 in = 0.0254 m).
Main Function:
Prompt the user for their weight in pounds and height in inches.
Convert the inputs to metric units using global conversion constants.
Calculate BMI using the formula bmi = weight / (height * height).
Determine the BMI category based on standard ranges.
Display the BMI value and category.
Commenting:
Include comments to explain key parts of the code.'''

# Global Variables
KG_PER_POUND = 0.453592
M_PER_IN = 0.0254

# Main Function
def main():

    # Prompt user for height and weight
    weight_lbs = int(input("Enter your weight in pounds: "))
    height_in = int(input("Enter your height in inches: "))

    # Perform conversions and bmi calculation
    weight_kg = weight_lbs * KG_PER_POUND # Convert weight to kg
    height_m = height_in * M_PER_IN # Convert height to m
    bmi = weight_kg / (height_m * height_m) # Calculate bmi
    
    # Determine bmi category
    if bmi < 18.5:
        weight_category = "underweight"
    elif bmi >= 18.5 and bmi < 25:
        weight_category = "normal"
    elif bmi >= 25 and bmi < 30:
        weight_category = "overweight"
    elif bmi >= 30:
        weight_category = "obese"
    else:
        print("Error.")
    
    # Print results
    print(f"Your BMI is: {bmi}")
    print(f"You are in the {weight_category} category.")

main()