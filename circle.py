import math

def calculate_area(radius):
    area = math.pi * radius * radius
    return area

r = float(input("Enter the radius: "))
print("Area of the circle is:", calculate_area(r))
