'''Assignment Details Define a Pet Class: Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type. Set a default value for pet_type as "Dog". Implement getter and setter methods for all properties. Include a class variable vet_name set to the name of your veterinary office. Add a method display_pet_info to print all details of the pet and owner. Create Pet Objects: Instantiate at least three pet objects with different details. Show the use of setter methods for at least one pet object. Implement Property Existence Check: Write a function check_property that uses hasattr() to verify if a property exists in a pet object. Display Information: Use display_pet_info to print details for each pet. Show three examples of check_property being used on various properties and pets. show two examples of display_pet_info on different instances of pet that you create'''

class Pet:

    # Initialization of private variables
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = "Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
    
    # Getter methods
    def get_owner_first_name(self):
        return self.__owner_first_name
    def get_owner_last_name(self):
        return self.__owner_last_name
    def get_pet_id(self):
        return self.__pet_id
    def get_pet_name(self):
        return self.__pet_name
    def get_pet_type(self):
        return self.__pet_type
    
    # Setter methods
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name
    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name
    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # Print all details of pet and owner
    def display_pet_info(self):
        print(f"Owner's Name: {self.__owner_first_name} {self.__owner_last_name}, Pet ID: {self.__pet_id}, Pet Name: {self.__pet_name}, Pet Type: {self.__pet_type}")
    
    # Verifies if a property exists in a Pet object
    def check_property(self, attr):
        return hasattr(self, f"_Pet__{attr}")

pet1 = Pet("Merrick", "Graddy", 1, "Lyla") # Uses default pet_type of "Dog"
pet2 = Pet("Malena", "Graddy", 2, "Sansa", "Cat")
pet3 = Pet("Jerri", "Partlo", "3", "Willie", "Parakeet")

def main():
    # Display info of pets
    print("Info on Pet 1: ")
    pet1.display_pet_info()
    print("Info on Pet 2: ")
    pet2.display_pet_info()
    print("Info on Pet 3: ")
    pet3.display_pet_info()

    # Use setter methods to change pet details
    print("Changing pet details...")
    pet3.set_pet_name("Homer")
    pet3.set_pet_type("Cat")
    pet1.set_owner_first_name("Karin")
    pet1.set_pet_type("Creature")

    # Display updated info of pets
    print("Info on Pet 1: ")
    pet1.display_pet_info()
    print("Info on Pet 2: ")
    pet2.display_pet_info()
    print("Info on Pet 3: ")
    pet3.display_pet_info()

    # Check for properties using check_property()
    print("Checking for 'pet_name' attribute in Pet 1... ", pet1.check_property("pet_name"))
    print("Checking for 'pet_type' attribute in Pet 2... ", pet2.check_property("pet_type"))
    print("Checking for 'pet_breed' attribute in Pet 3... ", pet3.check_property("pet_breed"))


main()
