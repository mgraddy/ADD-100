'''Create a List: Start by creating a list named days that includes all seven days of the week.
Initialize an Empty List: Create an empty list called steps to store the number of steps taken each day.
User Input: Using a loop, ask the user to enter the number of steps they took for each day.
Store Steps: Append the user's input to the steps list.
Display Daily Steps: Show the user the steps recorded for each day.
Total Steps: Calculate and display the total number of steps taken in the week.
Average Steps: Calculate and display the average steps.'''

# Initialize lists
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = []

# Ask user to enter number of steps for each day
for i in range(7):
    steps.append(int(input(f"Enter steps taken on {days[i]}: ")))
# Print daily results
for i in range(7):
    print(f"Steps taken on {days[i]}: {steps[i]}")
# Calculate total and average
total_steps = 0
for i in range(7):
    total_steps += steps[i]
average_steps = total_steps / 7
# Print calculated results
print(f"Total steps taken in the week: {total_steps}")
print(f"Average steps taken per day: {average_steps}")


