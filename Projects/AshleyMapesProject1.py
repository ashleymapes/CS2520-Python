'''
Ashley Mapes
Project 1

Task 1: program will calculate future value based on user
inputted present value, interest, and amount of years

Task 2: convert given program from java to python
- get numerical input from user then perform arithmetic on them

Task 3: program will get user's prefered method then 
calculate their bmi and give their classification
'''

# TASK 1
print("Welcome to an interest caluclator!")
print()

# collect values from user
presentVal = float(input("Please enter the present value as a float: "))
intRate = float(input("Please enter interest rate percentage as a float: "))
years = int(input("Please enter amount of years as a whole number: "))

# calculate final value
futureVal = presentVal * ((1 + intRate/100) ** years)

print(f"After {years} years and an interest rate of {intRate}%, your ${presentVal:.2f} has a value of ${futureVal:.2f}")
print()

'''
Test 1:
Welcome to an interest caluclator!

Please enter the present value as a float: 1000.00
Please enter interest rate percentage as a float: 5.0
Please enter amount of years as a whole number: 30
After 30 years and an interest rate of 5.0%, your $1000.00 has a value of $4321.94

Test 2:
Welcome to an interest caluclator!

Please enter the present value as a float: 1530.50
Please enter interest rate percentage as a float: 3.5
Please enter amount of years as a whole number: 15
After 15 years and an interest rate of 3.5%, your $1530.50 has a value of $2564.12

Test 3:
Welcome to an interest caluclator!

Please enter the present value as a float: 4123.25
Please enter interest rate percentage as a float: 2.5
Please enter amount of years as a whole number: 10
After 10 years and an interest rate of 2.5%, your $4123.25 has a value of $5278.11
'''

# TASK 2

# collect values from user
num1 = int(input("Enter the value of num1 (integer): "))
num2 = int(input("Enter the value of num2 (integer): "))

# swap two numbers
num1, num2 = num2, num1
print("The two numbers after swapping are: {} {}".format(num1,num2))

# calculate quotient and remainder
quotient = num1//num2
remainder = num1 % num2

# print results
print(f"Quotient when {num1}/{num2} is: {quotient}")
print(f"Remainder when {num1} is divided by {num2} is: {remainder}")
print()

'''
Test 1:
Enter the value of num1 (integer): 12
Enter the value of num2 (integer): 35
The two numbers after swapping are: 35 12
Quotient when 35/12 is: 2
Remainder when 35 is divided by 12 is: 11

Test 2:
Enter the value of num1 (integer): 35
Enter the value of num2 (integer): 13
The two numbers after swapping are: 13 35
Quotient when 13/35 is: 0
Remainder when 13 is divided by 35 is: 13


Test 3:
Enter the value of num1 (integer): 35
Enter the value of num2 (integer): 0
The two numbers after swapping are: 0 35
Quotient when 0/35 is: 0
Remainder when 0 is divided by 35 is: 0
'''

# TASK 3

print("Welcome to BMI calculator")
# ask the user if they would like us or metric and validate input
while True:
    bmiType = input("Please enter which system you would like to use ('USA' or 'Metric'): ").lower()
    if bmiType == "usa" or bmiType == "metric":
        break
    else:
        print("invalid input")

# ask user for weight and validate if over 0
weight = float(input(f"Please enter your weight in {'pounds (lb)' if bmiType == 'usa' else 'kilograms (kg)'}: "))
    
# ask user for height and validate if over 0
height = float(input(f"Please enter your height in {'inches (in)' if bmiType == 'usa' else 'meters (m)'}: "))

if weight > 0 and height > 0:
    # calculate bmi
    bmi = weight / (height ** 2) 

    # multiply by 703 is usa
    if bmiType == "usa":
        bmi *= 703

    classification = 0.0
    
    # classify bmi
    if bmi > 25:
        classification = "overweight"
    elif bmi >= 18:
        classification = "normal"
    elif bmi < 18:
        classification = "underweight"
    else:
        print("an error has occured in processing bmi...")

    print(f"Your bmi is {bmi:.1f}, which is classified as {classification}")
    
# error message if input is wrong
else:
    print("ERROR: bmi could not be calculated with the given measurements :(")

'''
Test 1:
USA system, normal BMI

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): usa
Please enter your weight in pounds (lb): 130
Please enter your height in inches (in): 65
Your bmi is 21.6, which is classified as normal

Test 2:
USA system, overweight

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): usa
Please enter your weight in pounds (lb): 200
Please enter your height in inches (in): 69
Your bmi is 29.5, which is classified as overweight

Test 3:
USA system, underweight

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): usa
Please enter your weight in pounds (lb): 95
Please enter your height in inches (in): 62
Your bmi is 17.4, which is classified as underweight

Test 4:
Metric system, normal BMI

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): metric
Please enter your weight in kilograms (kg): 53
Please enter your height in meters (m): 1.63
Your bmi is 19.9, which is classified as normal

Test 5:
Metric system, overweight

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): metric
Please enter your weight in kilograms (kg): 82
Please enter your height in meters (m): 1.73
Your bmi is 27.4, which is classified as overweight

Test 6:
Metric system, underweight

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): metric
Please enter your weight in kilograms (kg): 42
Please enter your height in meters (m): 1.63
Your bmi is 15.8, which is classified as underweight

Test 7:
height = 0

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): usa
Please enter your weight in pounds (lb): 112
Please enter your height in inches (in): 0
ERROR: bmi could not be calculated with the given measurements :(

Test 8: 
negative weight

Welcome to BMI calculator
Please enter which system you would like to use ('USA' or 'Metric'): metric
Please enter your weight in kilograms (kg): -50
Please enter your height in meters (m): 1.72
ERROR: bmi could not be calculated with the given measurements :(

'''