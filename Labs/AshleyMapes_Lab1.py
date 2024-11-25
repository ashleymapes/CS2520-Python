'''
Ashley Mapes
Lab 1
Task 1 will display my dream job goal settings
Task 2 will calculate the average price of one item based on input
'''

# TASK 1

# get name, age, company name, and annual salary
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
compName = input("Enter the company you wish to work: ")
annSalary = float(input("Enter the annual salary you wish to earn in dollars: "))

# calculate monthly salary
monSalary = annSalary/12

# print results
print("\nHello!")
print(f"My name is {name}, my age is {age}")
print(f"I hope to work for {compName} and earn $%.2f a month" % monSalary)
print("\n")

'''
TEST 1:
Please enter your name: Alice Wonderland
Please enter your age: 20
Enter the company you wish to work: Google
Enter the annual salary you wish to earn in dollars: 98576 

Hello!
My name is Alice Wonderland, my age is 20
I hope to work for Google and earn $8214.67 a month 

TEST 2:
Please enter your name: Ashley Mapes
Please enter your age: 19
Enter the company you wish to work: Samsung
Enter the annual salary you wish to earn in dollars: 100000

Hello!
My name is Ashley Mapes, my age is 19
I hope to work for Samsung and earn $8333.33 a month
'''

# TASK 2

# get itemName, numUnits, totalPrice
itemName = input("Please enter item name: ")
numUnits = int(input("Please enter number of units purchased: "))
totalPrice = float(input("Please enter total price paid: "))

# calcualte average price per unit
avgPrice = totalPrice/numUnits

# f-string printout
print("\nf-string:")
print(f"I purchased {numUnits} {itemName}(s) that cost me ${totalPrice:.2f}. The average price for each {itemName} is ${avgPrice:.2f}.")

# python string format printout
print("\nformat string:")
formattedSentence = "Product: {}\nNumber of units purchased: {}\nTotal price ${:0.2f}\nAverage price: ${:0.2f}"
print(formattedSentence.format(itemName, numUnits, totalPrice, avgPrice))

'''
TEST 1 (using given example):
Please enter item name: apple
Please enter number of units purchased: 3
Please enter total price paid: 5

f-string:
I purchased 3 apple(s) that cost me $5.00. The average price for each apple is $1.67.

format string:
Product: apple
Number of units purchased: 3
Total price $5.00
Average price: $1.67

TEST 2:
Please enter item name: salmon
Please enter number of units purchased: 2
Please enter total price paid: 22.57

f-string:
I purchased 2 salmon(s) that cost me $22.57. The average price for each salmon is $11.29.

format string:
Product: salmon
Number of units purchased: 2
Total price $22.57
Average price: $11.29

TEST 3:
Please enter item name: pillow
Please enter number of units purchased: 4
Please enter total price paid: 157.23

f-string:
I purchased 4 pillow(s) that cost me $157.23. The average price for each pillow is $39.31.

format string:
Product: pillow
Number of units purchased: 4
Total price $157.23
Average price: $39.31
'''