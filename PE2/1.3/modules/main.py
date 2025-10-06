from math_operations import calculator
from math_operations import geometry
def main():
    result = calculator.add(5, 3)
    print("Addition result:", result)

    result = calculator.subtract(10, 4)
    print("Subtraction result:", result)

    result = geometry.area_circle(3)
    print("Area of a circle with radius 3:", result)

    result = geometry.area_triangle(4,10)
    print("Area of a triangle with base 4 and height 10:", result)
main()
