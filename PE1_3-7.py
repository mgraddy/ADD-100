'''In this assignment, you will create a Python program to track your daily heart rate at different times and calculate the average.
Objective:
Create a Python script to track heart rate readings and calculate the average heart rate.
Requirements:
Define time_slots as a list with times of day (e.g., "Morning", "Midday", "Afternoon", "Evening").
Use a loop to prompt the user for heart rate (in BPM) at each time slot.
Create a multi-level list heart_rates to store the time slots and their corresponding heart rates.
Calculate the average heart rate and display it.'''
# Initialize lists
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
# Make multi-level list
for time in time_slots:
    heart_rates.append([time,int(input(f"Enter your heart rate (in BPM) in the {time}: "))])

# Calculate average
total_rates = 0
for i in range(len(heart_rates)):
    total_rates += heart_rates[i][1]
average_rate = total_rates / len(time_slots)

# Print results
for i in range(len(heart_rates)):
    print(f"{heart_rates[i][0]}: {heart_rates[i][1]}")
print(f"Average heart rate today: {average_rate}")
