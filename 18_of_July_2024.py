#Take money borrowed, interest and duration as input. Then, compute the compound interest rate.

#Formula= A = P (1 + R/100) ^ t
#A is the final amount. P is the principal amount. r is the annual interest rate (decimal) t is the number of times interest is compounded per year (12 for monthly)

def compound_interest(principle, rate, time):
    interest = principle * ((1+ rate / 100) ** time)
    return interest

P = int(input("Principal amount"))
r = float(input("Annual Interest (Decimal): "))
t = float(input("Overall duration"))

A = compound_interest(P, r, t)

print("Interest amount is: ", A)

#I don't really understand what a compound interest is so I just did the formula that I found on Google.

#--------------------------------------------------------------------------------------------

#Calculate grade of five subjects.

print("Enter your grades:")
grade1 = int(input("Grade 1: "))
grade2 = int(input("Grade 2: "))
grade3 = int(input("Grade 3: "))
grade4 = int(input("Grade 4: "))
grade5 = int(input("Grade 5: "))

avg = (grade1 + grade2 + grade3 + grade4 + grade5)/5

if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#--------------------------------------------------------------------------------------------

import scipy #I used scipy to get the gravitational constant

# Compute gravitational force between two objects.

# F = (G * m1 * m2) / d^2. Where G is the gravitational constant, m1 and m2 are the masses of the bodies, and d is the distance between them.

m1 = float(input("Mass 1:")) #mass is in kilograms
m2 = float(input("Mass 2:")) 
d = float(input("Distance:")) #distance is in meters

F = (scipy.constants.G * m1 * m2) / d ** 2

print("Gravitacional force: ", F)

#--------------------------------------------------------------------------------------------

#Take three sides of a triangle. And then calculate the area of the triangle.

import math

side1 = int(input("Side 1:"))
side2 = int(input("Side 2:"))
side3 = int(input("Side 3:"))

#We need to use Heron's formula, but first, we need to find the semi perimeter, the perimeter is found by adding all sides, the semi perimeter is found by dividing the perimeter by 2

s = (side1 + side2 + side3)/2

#Heron's formula is Area = √[s(s-a)(s-b)(s-c)]

area = math.sqrt((s*(s-side1)*(s-side2)*(s-side3)))

print("The area of the triangle is: ", area)


#--------------------------------------------------------------------------------------------

#For a given number, check whether the number is a prime number or not.

def prime_number(number):
    for x in range(2, number): #We check if the remainder is 0 for every division we make, if it's true then it means that the number isn't prime, if it's false for every case then it means it's a prime number, we start on 2 and end before the number to check if its divisible by any number other than 1 and the number itself
        if number % x == 0:
            return False
    return True
    
check_prime = prime_number(int(input("Enter a number: ")))

if check_prime:
    print("Your number is a Prime")
else:
    print("Your number is not a Prime")
