# The test thing
# Brayden Towner
# 11/06/2023

import os
os.system("cls")

def square_area(side_length, side_height=""):
    """Calculate the area of a square

    Args:
        side_length (float): The length of the square you're calculating the area for
        side_height (float, optional): The height of the rectangle if you aren't making a square
    Returns the area of the square
    """
    # Checks to see if side height is a valid variable. If not, make it side length
    if not (type(side_height) == float or type(side_height) == int):
        side_height=side_length
    # Returns the area
    return side_length*side_height


def circle_area(radius, pi = 3.14195265, diameter=""):
    """Calculates the area of a circle using radius or a diameter

    Args:
        radius (float): What the radius to calculate is
        pi (float, constant): Constant Pi variable. Defaults to 3.14195265. Do not use
        diameter (float, optional): If you can't divide by 2, you can use diameter instead. Overrides radius
    returns the area of a circle
    """
    # Checks to see if diameter exists if diameter is valid. If so, overwrite radius
    if (type(diameter) == float or type(diameter) == int):
        radius=diameter/2
    # Returns the area
    return pi*radius**2

def triangle_area(height, base):
    """Calculates the area of a triangle

    Args:
        height (float): The height of the triangle
        base (float): The width of the base of the triangle
    returns area of the triangle
    """
    pass


def add_all(*numbers):
    """Adds all the numbers the user gives
    Args:
        numbers (floats, multiple): The numbers needed to add
    returns all the numbers added
    """
    pass
