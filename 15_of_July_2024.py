#Take the temperature in degrees Celsius and convert it to Fahrenheit.

#(0 °C × 9/5) + 32 = 32 °F (From Google)

def Celsius_To_Fahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit

print("Temp in F is: " + str(Celsius_To_Fahrenheit(int(input("Temperature in Fahrenheit: ")))))

#-----------------------------------------------------------------------------------

#Convert miles to kilometers.

# 1 mile = 1.609344 km

def miles_to_km(miles):
    kms = miles * 1.609344
    return kms

print("Distance in kilometers is: " + str(miles_to_km(int(input("Miles: ")))))

#-----------------------------------------------------------------------------------

#Convert a decimal number to binary number.

#if remainder is 0 then add 0, if remainder is 1 then add 1, at the end reverse the values to get the binary number

def decimal_to_binary(number):
    binary = [] #list to store the numbers

    result = number #variable to divide it

    while (result != 0): #while result is different than 0 it will keep going until result is 0
        if result % 2 == 0:
            binary.append(0)
            result = result // 2
        elif result % 2 == 1:
            binary.append(1)
            result = result // 2
    
    binary.reverse() #reverse the list to get the actual binary number, the first remainder is the least significant bit, the last remainder is the most significant bit, hence why we have to reverse it

    binary_str = '' #variable to store the binary number

    for bin in binary: #loop to put the list into a string
        binary_str += str(bin)

    return binary_str

num = int(input("Number to convert: "))

print(num)
print(decimal_to_binary(num))

#-----------------------------------------------------------------------------------

#Convert a decimal number to binary number using a recursive function.

def decimal_to_binary_recursive(number):
    if number > 1: #if number is greater than 1
        decimal_to_binary_recursive(number//2) #call the function again
    print(number % 2, end = '') #when the number is less then 1 than it prints from the most recent function call to the very first call
    # without the end string, then it would print it in a new line for each stacked function call

num = int(input("Your decimal number: "))
decimal_to_binary_recursive(num)

#-----------------------------------------------------------------------------------

#You borrowed $5000 for 2 years with 2% interest per year. Calculate the simple interest to know how much you have to pay?

#Input the information
money = int(input("Money you borrowed: "))
time = int(input("Overall Duration: "))
interest = int(input("Interest Rate: "))

#Make the calculation to get the simple interest
print("Simple interest is: ", money * time * (interest/100))


