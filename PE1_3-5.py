'''Prompt the user to enter five names.
Store the names in a list.
Sort the list using the Bubble Sort algorithm.
Reverse the sorted list using a Python list method.
Print both the sorted and reversed lists.'''
# Initialize list
names = []
# Append list with user inputs
for i in range(5):
    names.append(input("Enter name: "))
# Make names lowercase for sorting
names = [name.lower() for name in names]

# Bubble Sort Implementation
swapped = True
while swapped:
    swapped = False
    for i in range(len(names)-1):
        if names[i] > names[i + 1]:
            names[i], names[i+1] = names[i+1], names[i]
            swapped = True # Mark that a swap occurred

print(names) # Print sorted names
names.reverse() # Reverse order
print(names) # Print reversed order