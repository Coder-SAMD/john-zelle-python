#1. Write a program to calculate the volume and surface area of a sphere from its radius, given as input.
# import math
# rad_sph = float(input('Enter the radius of the sphere in cm: '))
# vol_sph = (4/3) * math.pi * (rad_sph**3)
# surArea_sph = 4 * math.pi *(rad_sph**2)
# print(f'Volume of sphere is: {vol_sph} cm^3')
# print(f'Surface area of sphere is: {surArea_sph} cm^2')
#
# #2. Write a program that calculates the cost per square inch of a circular pizza, given its diameter and price.
# d = 10
# price = 5
# r = d/2
# area = math.pi * (r**2)
# cost = price * area
# print(f'Cost of pizza per square inches is: {cost}.')

# 3. Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number
# of hydrogen, carbon, and oxygen atoms in the molecule. The program should prompt the user to enter the number of
# hydrogen atoms, the number of carbon atoms, and the number of oxygen atoms. The program then prints the total combined
# molecular weight of all the atoms based on these individual atom weights:
# H = 1.00794
# C = 12.0107
# O = 15.9994
#
# H1 = int(input('Enter the number of Hydrogen atoms: '))
# C1 = int(input('Enter the number of Carbon atoms: '))
# O1 = int(input('Enter the number of Oxygen atoms: '))
#
# mol_wt = H1*1.00794 + C1*12.0107 + O1*15.9994
#
# print('The molecular weight of carbohydrate is: ',mol_wt,' gram/mol.')

# 4. Write a program that determines the distance to a lightning strike based on the time elapsed between the flash and
# the sound of thunder. The speed of sound is approximately 1100 ft/ sec and 1 mile is 5280 ft.
# t = float(input('Enter the time required for the sound of lightning to reach you in seconds: '))
# feet_per_sec = 1100     #ft/sec
# feet_per_mile = 5280
# v = feet_per_mile / feet_per_sec  #mile/sec
# distance = v * t
# print(f'The distance to the lightning is: {distance} miles.')

# 5. The confectionary coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $0.86 per
# pound + $1.50 fixed cost for overhead. Write a program that calculates the cost of an order.
# coffee_amt = float(input('How much coffee (in pounds) you wish to buy? The costing is given below:'+
#                          'Coffee: $10.50 per pound '+
#                          'Shipping: $0.86 per pound + $1.50 '))
# shipping_price = 0.86
# coffee_price = 10.50
# overhead_charges = 1.50
# total_price  = coffee_amt * coffee_price + coffee_amt * shipping_price + overhead_charges
# print('Your total bill including shipping and overhead charges comes out to be', total_price)

# 6. Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a program that calculates the
# slope of a line through two (non-vertical) points entered by the user.
# 7. Write a program that accepts two points (see previous problem) and determines the distance between them.
# x1 = int(input('Enter x co-ordinate of first point: '))
# y1 = int(input('Enter y co-ordinate of first point: '))
# x2 = int(input('Enter x co-ordinate of second point: '))
# y2 = int(input('Enter y co-ordinate of second point: '))
# slope = (y2 - y1) / (x2 - x1)
# dist = int(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))
# print(f'The slope of line passing through the given two points is {slope}.')
# print(f'The distance between the given two points is {dist} units.')

# 8. The Gregorian epact is the number of days between January 1st and the previous new moon. This value is used to
# figure out the date of Easter. Write a program that prompts the user for a 4-digit year and then outputs
# the value of the epact.
# year = int(input('Enter the year in YYYY format: '))
# golden_num = year % 19
# C = year // 100
# solar_corr = (3 * C // 4) - 12
# lunar_corr = (8 * C + 5) // 25 - 5
# epact = (11 * golden_num + 8 - solar_corr + lunar_corr) % 30
# print(f'The Epact of the year {year} is {epact}.')

# 9. Write a program to calculate the area of a triangle given the length of its three sides-a, b, and c
# print('This program calculates area of a triangle.')
# a = float(input('Enter length of first side: '))
# b = float(input('Enter length of second side: '))
# c = float(input('Enter length of third side: '))
#
# s = (a + b+ c) / 2
# area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#
# print(f'The area of given triangle is: {area} square units.')

# 10.Write a program to determine the length of a ladder required to reach a given height when leaned against a house.
# The height and angle of the ladder are given as inputs.
# height = float(input('Enter the height of the top of the ladder from the ground: '))
# angle_degree = float(input('Enter the angle made by the ladder with the ground in degrees: '))
# angle_rad = math.radians(angle_degree)
# length_of_ladder = height / math.sin(angle_rad)
# print(f'The required length of ladder to reach the given height is: {length_of_ladder} units.')

