# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Sep. 21, 2022
# This program calculates the area and perimeter of a circle with radius 15mm


import math


def main():
    # initializes radius
    radius = 15

    # prints area and perimeter of a circle
    print("The area and perimeter of a circle with a radius of 15mm are:")
    print("")
    print("area: pi*15^2 = {}mm²".format(math.pi * (radius**2)))
    print("")
    print("perimeter: 15*2*pi = {}mm".format(radius * 2 * math.pi))


if __name__ == "__main__":
    main()
