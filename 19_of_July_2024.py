#Ask the user to enter a number. Then find all the primes up to that number.

def prime_number(number):
    for x in range(2, number): #We check if the remainder is 0 for every division we make, if it's true then it means that the number isn't prime, if it's false for every case then it means it's a prime number, we start on 2 and end before the number to check if its divisible by any number other than 1 and the number itself
        if number % x == 0:
            return False
    return True

def all_prime(number):
    prime_list = []

    for x in range(2,number+1):
        if prime_number(x) is True: #If prime_number returns True, then add the number to the list, if not then continue with the for loop
            prime_list.append(x)
    return prime_list

print(all_prime(int(input("Enter a number:"))))

#----------------------------------------------------------------------------------

#Ask the user to enter a number. Then find all the primes factors for the number.

def prime_number(number):
    for x in range(2, number): #We check if the remainder is 0 for every division we make, if it's true then it means that the number isn't prime, if it's false for every case then it means it's a prime number, we start on 2 and end before the number to check if its divisible by any number other than 1 and the number itself
        if number % x == 0:
            return False
    return True

def prime_factors(number):
    factors_list = []

    for x in range(2,number+1):
        if number % x == 0:
            if prime_number(x) is True:
                factors_list.append(x)
    return factors_list

print(prime_factors(int(input("Enter a number:"))))


#----------------------------------------------------------------------------------

#Find the smallest prime factor for the given number.

#Ask the user to enter a number. Then find all the primes factors for the number.

def prime_number(number):
    for x in range(2, number): #We check if the remainder is 0 for every division we make, if it's true then it means that the number isn't prime, if it's false for every case then it means it's a prime number, we start on 2 and end before the number to check if its divisible by any number other than 1 and the number itself
        if number % x == 0:
            return False
    return True

def prime_factors(number):
    factors_list = []

    for x in range(2, number+1):
        if number % x == 0:
            if prime_number(x) is True:
                factors_list.append(x)
    return factors_list

prime_list = prime_factors(int(input("Enter a number:")))

print(prime_list)

print(min(prime_list))


#----------------------------------------------------------------------------------

#Reverse a string.

#If the input is: Hello World.

#The output should be: .dlroW olleH

def reverse_string(string):
    reverse = ""
    for x in string:
        reverse = x + reverse #When we put the x first, it puts the new character to the left of the string, basically it follows the order in which you put it, so for every loop it will put the character and the rest of the already existing string.
    return reverse

print(reverse_string(input("Enter the string:")))

#----------------------------------------------------------------------------------

#Reverse a string using a stack.

def reverse_stack(string):
    stack = []

    for char in string:
        stack.append(char)
    
    reverse = ""

    while (len(stack)) > 0:
        reverse = reverse + stack.pop() #We use the .pop() method to get the last element on the list, for me this way is easier to understand the process of how the string gets reversed.
    
    return reverse

print(reverse_stack(input("Enter the string:")))
