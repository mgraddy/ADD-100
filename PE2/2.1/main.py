'''At the end of this lesson, students will be able to:
Convert a character to its ASCII value using Python.
Convert an ASCII value back to a character.
Implement input validation using loops and error handling.'''
def main():
    
    # Part 1: Convert char to ASCII
    while True: # Loops until valid input
        user_char = input("Please enter a single character: ")
        if len(user_char) == 1: # Checks if user_char is 1 character
            ascii_value = ord(user_char)
            print(f"The ASCII value of {user_char} is {ascii_value}.")
            break
        else: # Loops back if invalid input
            print("Error: Please enter exactly one character.")

    # Part 2: Convert ASCII to char
    while True: # Loops until valid input
        user_ascii = input("Please enter an ASCII value: ")
        try: # 
            ascii_num = int(user_ascii) # Validate input. Potential failure
            if 32 <= ascii_num <= 127: # Validate range
                character = chr(ascii_num)
                print(f"The character for ASCII value {ascii_num} is {character}.")
                break
            else:
                print("Error. The number must be between 32 and 127.")
        except ValueError: # Runs if int(user_ascii) fails
            print("Error: Invalid input. Please enter a whole number.")
main()

        
    