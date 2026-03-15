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

# 5. The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $0.86 per
# pound + $1.50 fixed cost for overhead. Write a program that calculates the cost of an order.
# coffee_amt = float(input('How much coffee (in pounds) you wish to buy? The costing is given below:'+
#                          'Coffee: $10.50 per pound '+
#                          'Shipping: $0.86 per pound + $1.50 '))
# shipping_price = 0.86
# coffee_price = 10.50
overhead_charges = 1.50
# total_price  = coffee_amt * coffee_price + coffee_amt * shipping_price + overhead_charges
# print('Your total bill including shipping and overhead charges comes out to be ', total_price)

# 6. Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a program that calculates the
# slope of a line through two (non-vertical) points entered by the user.
# 7. Write a program that accepts two points (see previous problem) and determines the distance between them.


