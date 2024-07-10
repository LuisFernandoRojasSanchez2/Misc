#Create a random number between 0 to 10
import random

random_num = random.randint(0,10)

print(random_num)


#Find the floor division of two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = num1//num2
print(result)

#Swap two variables.

#To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable.

a = 1
b = 2

temp = a
a = b
b = temp

print(a,b)

#Find the max number of two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# if num1 < num2:
#     largest = num2
# else:
#     largest = num1

largest = max(num1,num2)

print("Largest number you entered is: ", largest)


#For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5.
def divisible3and5(num):
    result = []
    for i in range(num):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
    return result

print(divisible3and5(int(input("Number"))))

#Find the largest of the three numbers.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

#largest = max(num1, num2, num3)

print("Largest number you entered is: ", largest)

#Take numbers from a user and show the average of the numbers the user entered.
loops = int(input("How many numbers"))

total = 0
 
for i in range(0,loops):
   elem=int(input("Enter element: "))
   total += elem
 
avg = total/loops

print(avg)
