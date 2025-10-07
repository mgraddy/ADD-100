'''Create the Pet Class: Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name. Implement get and set methods for each of these attributes. Add a method called print_details that prints the details of the pet. Create Instances: Create three objects of the Pet class with different kinds, breeds, and names. Call the print_details method for each object that you created Demonstrate a Special Method or Function: Choose three of the following and demonstrate its use with the Pet class instances: __name__: Display the name of the class. type(): Show the class used to instantiate a pet object. __module__: Return the module name in which the Pet class is defined. __bases__: Display the base classes of the Pet class (if any). isinstance(): Check if an instance is of the Pet class.'''

class Pet:
    
    # Initialize private variables
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter methods
    def get_kind(self):
        return self.__kind
    def get_breed(self):
        return self.__breed
    def get_name(self):
        return self.__name
    
    # Setter methods
    def set_kind(self, kind):
        self.__kind = kind
    def set_breed(self, breed):
        self.__breed = breed
    def set_name(self, name):
        self.__name = name
    
    def print_details(self): # Print details of pet
        print(f"Kind: {self.__kind}, Breed: {self.__breed}, Name: {self.__name}")
    


def main():

    # Create 3 Pet objects
    pet1 = Pet("Dog", "Dachshund", "Frankie")
    pet2 = Pet("Cat", "Orange Tabby", "Homer")
    pet3 = Pet("Bird", "Parakeet", "Willie")

    # Print info on all Pet objects
    print("Info on Pet 1:")
    pet1.print_details()
    print("Info on Pet 2: ")
    pet2.print_details()
    print("Info on Pet 3: ")
    pet3.print_details()

    # Demonstrating Special Methods or Functions
    print("Class name:", Pet.__name__) # Using __name__
    print("Class used to initialize Pet 1: ", type(pet1)) # Using type()
    print("Pet 2 is an instance of the Pet class: ", isinstance(pet2, Pet))

# Only run main function when file is executed directly
if __name__ == "__main__":
    main()

    