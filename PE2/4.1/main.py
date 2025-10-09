'''Create a Python program that uses a generator function to produce all possible two-letter combinations from a given list of characters. For example, if the list is ['a', 'b', 'c'], the program should generate 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'. Instructions: Define a generator function two_letter_combinations that takes a list of characters as an argument. Use nested loops within the generator function to iterate over the list of characters. In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination. In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. Create an original  5-letter list. Include comments in your code to explain the logic behind the generator function and the use of the yield statement.'''

def two_letter_combinations(chars):
    for first_char in chars:
        for second_char in chars:
            yield first_char + second_char


def main():
    input_list = ['m','e','r','c','k'] # Define the original list
    combinations_generator = two_letter_combinations(input_list) # Create the generator object
    
    print("All two-letter combinations:")
    for combo in combinations_generator: # Ask the generator for values
        print(combo)

if __name__ == "__main__":
    main()


