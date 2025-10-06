'''Assignment Steps:
Create a list representing 20 seats, numbered 1 to 20.
Display the list of available seats to the customer.
Prompt the customer to select a seat by entering its number. Entering '0' ends the purchase process.
Remove the selected seat from the list of available seats and display the updated list.
If the customer selects an invalid or already sold seat, display a friendly error message and prompt them to try again.
Ensure the program gracefully handles all scenarios and is user-friendly.'''

# Initialize seat list and print list
seats = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Available seats by number: ", seats)

while True:
    selected_seat = int(input("Select a seat by number (or enter 0 to quit): "))
    # Check for exit condition
    if selected_seat == 0:
        print("Exiting purchase process.")
        break
    # Check if out of range
    elif selected_seat < 1 or selected_seat > 20:
        print("Invalid seat number. Please choose a number between 1 and 20.")
    # Check if seat is available, remove, and print updated list
    elif selected_seat in seats:
        seats.remove(selected_seat)
        print(f"Seat {selected_seat} has been sold.")
        print("Updated list of available seats:", seats)
    else:
        print("Seat already sold. Try again.")

