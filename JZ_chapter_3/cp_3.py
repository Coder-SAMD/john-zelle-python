#1. Write a program to calculate the volume and surface area of a sphere from its radius, given as input.
import math
rad_sph = float(input('Enter the radius of the sphere in cm: '))
vol_sph = (4/3) * math.pi * (rad_sph**3)
surArea_sph = 4 * math.pi *(rad_sph**2)
print(f'Volume of sphere is: {vol_sph} cm^3')
print(f'Surface area of sphere is: {surArea_sph} cm^2')
#
# #2. Write a program that calculates the cost per square inch of a circular pizza, given its diameter and price.
d = 10
price = 5
r = d/2
area = math.pi * (r**2)
cost = price * area
print(f'Cost of pizza per square inches is: {cost}.')

# 3. Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number
# of hydrogen, carbon, and oxygen atoms in the molecule. The program should prompt the user to enter the number of
# hydrogen atoms, the number of carbon atoms, and the number of oxygen atoms. The program then prints the total combined
# molecular weight of all the atoms based on these individual atom weights:
H = 1.00794
C = 12.0107
O = 15.9994

H1 = int(input('Enter the number of Hydrogen atoms: '))
C1 = int(input('Enter the number of Carbon atoms: '))
O1 = int(input('Enter the number of Oxygen atoms: '))

mol_wt = H1*1.00794 + C1*12.0107 + O1*15.9994

print('The molecular weight of carbohydrate is: ',mol_wt,' gram/mol.')

# 4. Write a program that determines the distance to a lightning strike based on the time elapsed between the flash and
# the sound of thunder. The speed of sound is approximately 1100 ft/ sec and 1 mile is 5280 ft.
t = float(input('Enter the time required for the sound of lightning to reach you in seconds: '))
feet_per_sec = 1100     #ft/sec
feet_per_mile = 5280
v = feet_per_mile / feet_per_sec  #mile/sec
distance = v * t
print(f'The distance to the lightning is: {distance} miles.')

# 5. The confectionary coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $0.86 per
# pound + $1.50 fixed cost for overhead. Write a program that calculates the cost of an order.
coffee_amt = float(input('How much coffee (in pounds) you wish to buy? The costing is given below:'+
                         'Coffee: $10.50 per pound '+
                         'Shipping: $0.86 per pound + $1.50 '))
shipping_price = 0.86
coffee_price = 10.50
overhead_charges = 1.50
total_price  = coffee_amt * coffee_price + coffee_amt * shipping_price + overhead_charges
print('Your total bill including shipping and overhead charges comes out to be', total_price)

# 6. Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a program that calculates the
# slope of a line through two (non-vertical) points entered by the user.
# 7. Write a program that accepts two points (see previous problem) and determines the distance between them.
x1 = int(input('Enter x co-ordinate of first point: '))
y1 = int(input('Enter y co-ordinate of first point: '))
x2 = int(input('Enter x co-ordinate of second point: '))
y2 = int(input('Enter y co-ordinate of second point: '))
slope = (y2 - y1) / (x2 - x1)
dist = int(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)))
print(f'The slope of line passing through the given two points is {slope}.')
print(f'The distance between the given two points is {dist} units.')

# 8. The Gregorian epact is the number of days between January 1st and the previous new moon. This value is used to
# figure out the date of Easter. Write a program that prompts the user for a 4-digit year and then outputs
# the value of the epact.
year = int(input('Enter the year in YYYY format: '))
golden_num = year % 19
c1 = year // 100
solar_corr = (3 * c1 // 4) - 12
lunar_corr = (8 * c1 + 5) // 25 - 5
epact = (11 * golden_num + 8 - solar_corr + lunar_corr) % 30
print(f'The Epact of the year {year} is {epact}.')

# 9. Write a program to calculate the area of a triangle given the length of its three sides-a, b, and c
# print('This program calculates area of a triangle.')
a = float(input('Enter length of first side: '))
b = float(input('Enter length of second side: '))
c = float(input('Enter length of third side: '))

s = (a + b+ c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f'The area of given triangle is: {area} square units.')

# 10.Write a program to determine the length of a ladder required to reach a given height when leaned against a house.
# The height and angle of the ladder are given as inputs.
height = float(input('Enter the height of the top of the ladder from the ground: '))
angle_degree = float(input('Enter the angle made by the ladder with the ground in degrees: '))
angle_rad = math.radians(angle_degree)
length_of_ladder = height / math.sin(angle_rad)
print(f'The required length of ladder to reach the given height is: {length_of_ladder} units.')

# 11. Write a program to find the sum of the first n natural numbers, where the value of n is provided by the user.
# 12. Write a program to find the sum of the cubes of the first n natural numbers where the value of n is provided by
# the user.
# answer 11 -
n = int(input('Enter a finite natural number: '))
addition = 0
for i in range(1,n+1):
    addition += i
print(f'The sum of first {n} natural numbers is {addition}.')
# answer 12 -
cube_sum = 0
for i in range(1,n+1):
    cube_sum = cube_sum + (i**3)
print(f'The sum of cubes of first {n} natural numbers is {cube_sum}')

# #13. Write a program to sum a series of numbers entered by the user. The
# program should first prompt the user for how many numbers are to be
# summed. The program should then prompt the user for each of the numbers in turn and print out a total sum after all
# the numbers have been entered.
# 14. Write a program that finds the average of a series of numbers entered by the user. As in the previous problem, the
# program will first ask the user how many numbers there are. Note: The average should always be a float,
# even if the user inputs are all ints.
#answer 13
n2 = int(input('How many numbers are to be added? '))
add = 0
for i in range(n2):
    a = int(input(f'Enter number {i+1}: '))
    add = add + a
print(f'The final sum of the numbers entered is: {add}')

#answer 14
avg = add / n2
print('Average of all entered numbers is ',avg)

# 15. Write a program that approximates the value of pi by summing the terms of this series:
# (4/1-4/3 + 4/5-4/7 + 4/9-4/11 + . . .)
# The program should prompt the user for n, the number of terms to sum, and then output the sum of the first n terms of
# this series. Have your program subtract the approximation from the value of math. pi to see how accurate it is.

n3 = int(input('Enter the number of terms to sum: '))
divisor = 1
pi_sum = 0
sign = 1
for i in range(n3):
    pi_sum = pi_sum + sign * (4/divisor)
    divisor += 2
    sign = sign * -1
print('Calculated value of pie is: ',pi_sum)
accu = abs(math.pi - pi_sum)
print(f'The difference between the actual value of pi({math.pi}) and calculated value of pi({pi_sum}) is: {accu}')

# 16. A Fibonacci sequence is a sequence of numbers where each successive number is the sum of the previous two.
# The classic Fibonacci sequence begins: 1, 1, 2, 3, 5, 8, 13, . . . . Write a program that computes the nth
# Fibonacci number where n is a value input by the user. For example, if n = 6, then the result is 8.

n4 = int(input("Enter the value of n: "))
a = 0
b = 1

for i in range(n4 - 1):
    a, b = b, a + b

print(f"The {n4}th Fibonacci number is: {b}")

# 17. Write a program to approximate the square root of a number using Newton’s method. Start with guess = x/2, iterate
# the formula (g+x/g)/2 for a user-specified number of times, and compare the result with math.sqrt(x) to show the
# difference.

x = float(input("Enter the number to find the square root of: "))
n = int(input("How many times should the guess be improved? "))

guess = x / 2
for i in range(n):
    guess = (guess + (x / guess)) / 2

print(f"\nFinal approximation after {n} iterations: {guess}")

actual_sqrt = math.sqrt(x)
error = abs(actual_sqrt - guess)

print(f"Actual value from math.sqrt: {actual_sqrt}")
print(f"The difference (error) is: {error}")