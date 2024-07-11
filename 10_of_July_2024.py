#For a given list, get the sum of each number in the list

import random as rand


def create_random_list(): #did this function to make a random list of 10 numbers between 0 and 100
    num_list = []
    for x in range(11):
        num = rand.randint(0,100)
        num_list.append(num)
    return num_list

def sum_list(nums):
    sum = 0
    for x in range(len(nums)):
        sum += nums[x]
    print(nums)
    return sum

print(sum_list(create_random_list()))

#-------------------------------------------------------------------------

#Find the largest element of a list.

#Easy way

import random as rand

num_list = []

for x in range(rand.randint(1,10)):
    num_list.append(x)

print(num_list)
print(max(num_list))


#Hard Way

#Find the largest element of a list.

import random as rand

def create_random_list(): #did this function to make a random list of 10 numbers between 0 and 100
    num_list = []
    for x in range(11):
        num = rand.randint(0,100)
        num_list.append(num)
    return num_list

def find_largest(nums):
    largest = nums[0]

    for x in range(len(nums)):
        if nums[x] > largest: #if nums[x] is larger than the largest then it becomes the new largest.
            largest = nums[x]
    print(nums)
    return largest

print(find_largest(create_random_list())) #the find_largest function needs a list of numbers, and the create_random_list returns a list of numbers.

#-------------------------------------------------------------------------

#Take a number as input. Then get the sum of the numbers. If the number is n. Then get 0^2+1^2+2^2+3^2+4^2+.............+n^2

def square_sum(num):
    sum = 0
    for x in range(0, num+1): #If you enter 2, then it will return 5, without the +1 it would return just 1, because the list starts at 0 and does not include the end of the range
        square = x**2
        sum += square
    return sum

number = int(input("Enter a number: "))
print(square_sum(number))

#-------------------------------------------------------------------------

#For a list, find the second largest number in the list.

import random as rand

def create_random_list(): #did this function to make a random list of 10 numbers between 0 and 100
    num_list = []
    for x in range(11):
        num = rand.randint(0,100)
        num_list.append(num)
    return num_list

def find_second_largest(nums):
    largest = nums[0]
    second = nums[0]

    for x in range(1, len(num_list)): #starts at 1 because if we start at cero then it would compare to itself on the first loop, and if its the largest then it wouldnt work.
        if nums[x] > largest:
            second = largest #the largest passes to be the second largest
            largest = nums[x] #we assign the largest a new value
        elif nums[x] > second: #if the number is greater than the second largest then we assign it to the variable second (second largest)
            second = nums[x]
    print(nums)
    return second

print(find_second_largest(create_random_list())) #the find_second_largest function needs a list of numbers, and the create_random_list returns a list of numbers.

#-------------------------------------------------------------------------

#For a list, find the second smallest element in the list

import random as rand

def create_random_list(): #did this function to make a random list of 10 numbers between 0 and 100
    num_list = []
    for x in range(11):
        num = rand.randint(0,100)
        num_list.append(num)
    return num_list

def find_second_smallest(nums):

    smallest = nums[0]
    second_smallest = nums[0]

    for x in range(1, len(nums)):
        if nums[x] < smallest: #if the value of nums[x] is smaller than smallest, then the smallest is the second smallest and the value of nums[x] is the new smallest
            second_smallest = smallest #smallest now becomes the second smallest
            smallest = nums[x] #nums[x] is now the new smallest
        elif nums[x] < second_smallest: #if the value of nums[x] is smaller than the second smallest then it becomes the new second smallest.
            second_smallest = nums[x]
    print(nums)
    return second_smallest

print(find_second_smallest(create_random_list())) #the find_second_smallest function needs a list of numbers, and the create_random_list returns a list of numbers.
