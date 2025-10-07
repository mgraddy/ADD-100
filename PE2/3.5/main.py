'''Assignment Part 1: Defining Classes File 1: Write an Employee class with the following attributes: Employee name Employee number Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes: Shift number (integer: 1 for day, 2 for night) Hourly pay rate Implement accessor and mutator methods (getters and setters) for each class. Assignment Part 2: Implementing and Testing Part 2: Write a script to: Create an instance of ProductionWorker. Prompt the user for each attribute's data. Store and then display the data using the object's methods.'''

class Employee:

    # Employee constructor
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Getter methods
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number
    
    # Override __str__() method for user-friendly output
    def __str__(self):
        return f"Employee(Name: {self.__name}, Number: {self.__number})"
    
class ProductionWorker(Employee):

    # ProductionWorker constructor
    def __init__(self, name, number, shift_number: int, hourly_pay):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay = hourly_pay

    # Getter methods
    def get_shift_number(self):
        return self.__shift_number
    def get_hourly_pay(self):
        return self.__hourly_pay
    def get_shift_str(self):
        if self.__shift_number == 1:
            return "Day"
        else:
            return "Night"
    
    # Setter methods
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay
    
    # Override __str__() method for user-friendly output
    def __str__(self):
        return super().__str__() + f", ProductionWorker(Shift Number: {self.__shift_number}, Hourly Pay: {self.__hourly_pay})"

def main():

    # User inputs attributes
    print("Enter the following details of the Employee" + ("-" * 20))
    name = input("Name: ") # User enters name
    number = input("Phone Number: ") # User enters number
    while True: # Loop until user enters valid shift number
        try:
            shift_number = int(input("Shift Number (integer: 1 for day, 2 for night): "))
            if shift_number != 1 and shift_number != 2:
                print("Invalid shift number. Please enter 1 or 2.")
            else:
                break
        except ValueError:
            print("An input error has occurred.")  
    hourly_pay = input("Hourly Pay: ") # User enters hourly pay

    worker = ProductionWorker(name, number, shift_number, hourly_pay) # Create ProductionWorker object with user input attributes

    # Print details of Production Worker object
    print(("-" * 20) + "Details of Employee" + ("-" * 20))
    print("Name: " + worker.get_name())
    print("Employee Number: " + worker.get_number())
    print("Shift: " + worker.get_shift_str())
    print("Pay Rate: " + worker.get_hourly_pay())


if __name__ == "__main__":
    main()


    

    
    