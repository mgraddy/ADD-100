'''Your task is to design and implement a class in a programming language. This class will represent a person and hold personal data.

 

Assignment Steps:

Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.'''

class Person:
    # Initialize private variables
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    
    # Getter methods
    def get_info(self): # Get person info as an f string
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone_number(self):
        return self.__phone_number
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

# Program to create 3 Person objects and print their info
def main():
    person1 = Person("Merrick", "1234 Millstream Rd", 22, 8159013286)
    person2 = Person("Madison", "12 Pine Cir", 21, 1234567890)
    person3 = Person("Sansa", "1234 Pickwick Ln", 2, 9876543210)
    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())


main()