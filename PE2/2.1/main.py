'''At the end of this lesson, students will be able to:
Convert a character to its ASCII value using Python.
Convert an ASCII value back to a character.
Implement input validation using loops and error handling.'''
def main():
    while True:
        user_char = input("Please enter a single character: ")
        if len(user_char) == 1:
            ascii_value = ord(user_char)
            print(f"The ASCII value of {user_char} is {ascii_value}.")
            break
        else:
            print("Error: Please enter exactly one character.")
    while True:
        user_ascii = input("Please enter an ASCII value: ")
        try:
            ascii_num = int(user_ascii)
            if 32 <= ascii_num <= 127:
                character = chr(ascii_num)
                print(f"The character for ASCII value {ascii_num} is {character}.")
                break
            else:
                print("Error. The number must be between 32 and 127.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")
main()

        
    