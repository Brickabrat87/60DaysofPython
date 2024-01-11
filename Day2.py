# Create a program to calculate the area of a circle given its radius.
import math


def area_of_circle():
    radius = int(input("Please provide radius: "))
    area_circ = round(math.pi * radius ** 2, 2)
    print("Calculated area of circle is ", area_circ)


area_of_circle()


