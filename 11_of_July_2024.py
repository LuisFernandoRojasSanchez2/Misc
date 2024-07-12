#Take two inputs from the user. One will be an integer. The other will be a float number. Then multiply them to display the output.

a = int(input('First number:'))
b = float(input('Second number:'))

result = a * b

print('Your result is: ', result)

#-------------------------------------------------------------------------------

#Take two numbers from the users. Calculate the result of second number power of the first number.

base = int(input('Base number:'))
power = int(input('Power number:'))

result = base ** power
#result = pow(base, power)

print('Your result is: ', result)

#-------------------------------------------------------------------------------

#Find the floor division of two numbers.

a = int(input('First number:'))
b = int(input('Second number:'))

result = a//b

print(result)

#-------------------------------------------------------------------------------

#For a given list, get the sum of each number in the list

import random as rand

def create_random_list(): #did this function to make a random list of 10 numbers between 0 and 100
    num_list = []
    for x in range(11):
        num = rand.randint(0,100)
        num_list.append(num)
    return num_list

def get_sum(nums):
    sum = 0
    for x in nums:
        sum += x
    print(nums)
    return sum

print(get_sum(create_random_list()))

#-------------------------------------------------------------------------------

#For a given string, remove all duplicate characters from that string.


def remove_duplicate(phrase): #if the character is in result, then it means it's duplicated, if it's not then it means it's not duplicated
    result = ""
    for x in phrase:
        if x not in result:
            result += x
    return result

the_string = input("Enter your phrase")

print(the_string)
print(remove_duplicate(the_string))
