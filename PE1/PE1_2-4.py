"""Create a Python program that converts kilograms to pounds. Use at least four different samples to convert. A sample of the math is provided below; do not use the same example in your program."""
# Conversion factor
kg_to_lb = 2.20462
# Sample weights in kilograms
weights_kg_1 = 10
weights_kg_2 = 25.5
weights_kg_3 = 50
weights_kg_4 = 100
# Convert to pounds
weights_lb_1 = weights_kg_1 * kg_to_lb
weights_lb_2 = weights_kg_2 * kg_to_lb
weights_lb_3 = weights_kg_3 * kg_to_lb
weights_lb_4 = weights_kg_4 * kg_to_lb
# Print results
print(f"{weights_kg_1} kg is {weights_lb_1:.2f} lbs")
print(f"{weights_kg_2} kg is {weights_lb_2:.2f} lbs")
print(f"{weights_kg_3} kg is {weights_lb_3:.2f} lbs")
print(f"{weights_kg_4} kg is {weights_lb_4:.2f} lbs")