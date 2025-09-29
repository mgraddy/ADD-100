'''Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
Write a program that uses a for loop to print each class in the tuple.
Use the len function to print how many courses are in the tuple.
Make sure to use a main function for this program.'''

programming_classes = ('Intro to Python','Advanced Python','Database Essentials','Web Development Basics','Data Structures in Python','Web Design Fundamentals')

def print_each(tuple): # Function to print each item in a tuple
    for item in tuple:
        print(item)

def main():
    print("Here's a list of programming classes: ")
    print_each(programming_classes)
    print("There are",len(programming_classes),"classes in the programming_classes tuple.")
main() # Call main function
