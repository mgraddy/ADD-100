'''Your mission is to create a Python program that uses a dictionary to translate letters into the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.

Steps to Follow:
Create the NATO Phonetic Alphabet Dictionary:
Construct a dictionary in Python named nato_alphabet, where each key is a letter, and its value is the corresponding NATO phonetic term.
Develop the Spelling Program:
Write a function to prompt the user for a word and iterate through each letter to find and print the NATO phonetic term.
Incorporate a Main Function:
Encapsulate your logic within a main() function for organization.
Test Your Program:
Test the program with various inputs, ensuring it works as expected.'''
nato_alphabet = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

def nato_spell(word):
    word_upper = word.upper()
    for letter in word_upper:
        for key in nato_alphabet:
            if letter == key:
                print(nato_alphabet[key])
            else:
                continue
def main():
    user_word = input("Enter a word: ")
    nato_spell(user_word)
main()


