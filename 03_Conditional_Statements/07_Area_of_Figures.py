import math

figure_type = input("Enter figure type: ")

if figure_type == "square":
    side = float(input("Enter side length: "))
    area = side * side
elif figure_type == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
elif figure_type == "circle":
    radius = float(input("Enter radius: "))
    area = math.pi * radius * radius
elif figure_type == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = (base * height) / 2
else:
    area = None
    print("Unknown figure type.")

if area is not None:
    print(area)