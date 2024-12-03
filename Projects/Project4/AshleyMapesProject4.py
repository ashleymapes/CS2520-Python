'''
Ashley Mapes
CS2520 Python
Project 4
12-2-2024
Task 1: read file and create stock objects
Task 2: create pair object and preform operations
Task 3: translate java code to python about bicycles
'''


# TASK1: Read file and create stock objects

# create Stock class
class Stock:
    # define constructor
    def __init__(self, symbol, high, low, closing):
        self.symbol = symbol
        self.high = float(high)
        self.low = float(low)
        self.closing = float(closing)

    # define string return
    def __str__(self):
        return f"Stock: {self.symbol}, High price: {self.high}, Low price: {self.low}, Closing price: {self.closing}"

    # calculate the absolute value of difference between high and low
    def priceDifference(self):
        return abs(self.high - self.low)

    # function to see if closing price is less than low (good deal)
    def isDeal(self):
        return self.closing < self.low
    
    # function to see if closing price is more than high (expensive)
    def isExpensive(self):
        return self.closing > self.high
    
    # for testing, get difference between closing and high
    def closingToHigh(self):
        return abs(self.high - self.closing)


# function to read file and return list of stocks
def read_file():
    # set number of attempts
    attempts = 0
    while attempts < 3:
        # open file
        try:
            filename = input("Please enter the filepath: ")
            with open(filename, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            # allow user to try again
            attempts += 1
            print(f"Attempt {attempts}: File not found. Try again.")
    print("Maximum attempts reached. Exiting program.")
    return None

# function to read lines and create stock objects
def process_stocks(lines):
    # create empty list to hold stocks
    stocks = []
    for line in lines[1:]:
        try:
            # split line into values
            data = line.strip().split()
            if len(data) == 4:
                symbol, high, low, closing = data
            elif len(data) == 5:
                symbol, high, low, closing = data[0], data[1], data[2], data[4]
            else:
                continue
            # append to stocks
            stocks.append(Stock(symbol, high, low, closing))
        # if line is not in correct format, skip it and print error
        except ValueError:
            print(f"Invalid data discarded: {line}")
            continue
        except Exception:
            print(f"File error: {line}")
            continue
    return stocks


def task1():
    # lines of file
    lines = read_file()
    
    # if file not read successfully
    if not lines:
        return

    # create list of stocks from file
    stocks = process_stocks(lines)

    # if stocks is not empty
    if stocks:
        # print out all stocks
        print("\nAll Stocks:")
        for stock in stocks:
            print(stock)

        # calculate and print largest difference between high and low prices
        largestDifference = max(stocks, key=lambda s: s.priceDifference())
        print("\nStock with Largest High-Low Difference:")
        print(largestDifference)

        # calculate and print smallest difference between closing and high prices
        smallestClosingToHigh = min(stocks, key=lambda s: s.closingToHigh())
        print("\nStock with Closing Price Closest to High Price:")
        print(smallestClosingToHigh)
        
        # test other methods
        testStock = stocks[0]
        print(f"\nTest Stock: {testStock}")
        print(f"High-Low Difference: {testStock.priceDifference()}")
        print(f"Closing-High Difference: {testStock.closingToHigh()}")
        print(f"Testing isDeal(): {testStock.isDeal()}")
        print(f"Testing isExpensive(): {testStock.isExpensive()}")
        
    
'''

TESTING TASK1
===============
TEST 1:
Please enter the filepath: symbols.txt
Invalid data discarded: META 531.50, 518.15 528.54


All Stocks:
Stock: AAPL, High price: 221.89, Low price: 219.01, Closing price: 221.27
Stock: AMD, High price: 141.19, Low price: 137.52, Closing price: 141.13
Stock: AMZN, High price: 171.04, Low price: 167.1, Closing price: 170.23
Stock: GME, High price: 22.38, Low price: 21.86, Closing price: 22.27
Stock: GOOG, High price: 165.93, Low price: 166.54, Closing price: 164.77
Stock: INTC, High price: 20.47, Low price: 20.48, Closing price: 19.47
Stock: LOGI, High price: 88.2, Low price: 86.63, Closing price: 87.76
Stock: MSFT, High price: 414.95, Low price: 409.57, Closing price: 414.01
Stock: NVDA, High price: 116.23, Low price: 111.58, Closing price: 116.14
Stock with Closing Price Closest to High Price:
Stock: AMD, High price: 141.19, Low price: 137.52, Closing price: 141.13

Test Stock: Stock: AAPL, High price: 221.89, Low price: 219.01, Closing price: 221.27
High-Low Difference: 2.8799999999999955
Closing-High Difference: 0.6199999999999761
Testing isDeal(): False
Testing isExpensive(): False

TEST 2:
Please enter the filepath: testing
Attempt 1: File not found. Try again.
Please enter the filepath: testing
Attempt 2: File not found. Try again.
Please enter the filepath: testing
Attempt 3: File not found. Try again.
Maximum attempts reached. Exiting program.

TEST 3: 
Please enter the filepath: test.txt

All Stocks:
Stock: APPLE, High price: 12.5, Low price: 10.5, Closing price: 9.99
Stock: BANANA, High price: 14.98, Low price: 4.32, Closing price: 9.65
Stock: PEAR, High price: 3.45, Low price: 2.45, Closing price: 2.95
Stock: SHOPKINS, High price: 90.8, Low price: 80.8, Closing price: 38.5
Stock: COOKIE, High price: 5.99, Low price: 4.99, Closing price: 3.2
Stock: LALA, High price: 3.87, Low price: 1.34, Closing price: 2.54
Stock: MOOMOO, High price: 10000.0, Low price: 1.0, Closing price: 32.4
Stock: TROLLS, High price: 0.99, Low price: 0.0, Closing price: 0.44

Stock with Largest High-Low Difference:
Stock: MOOMOO, High price: 10000.0, Low price: 1.0, Closing price: 32.4

Stock with Closing Price Closest to High Price:
Stock: PEAR, High price: 3.45, Low price: 2.45, Closing price: 2.95

Test Stock: Stock: APPLE, High price: 12.5, Low price: 10.5, Closing price: 9.99
High-Low Difference: 2.0
Closing-High Difference: 2.51
Testing isDeal(): True
Testing isExpensive(): False
'''

#TASK 2: Create pair object and class and preform operations

# define pair class
class Pair:
    # define constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # define string method to print pair
    def __str__(self):
        return f"<{self.x}, {self.y}>"

    # define add method to add two pairs
    def __add__(self, other):
        return Pair(self.x + other.x, self.y + other.y)

    # define subtract method to subtract two pairs
    def __mul__(self, other):
        return Pair(self.x * other.x, self.y * other.y)

    # define division method to divide two pairs
    def __truediv__(self, other):
        return Pair(self.x * self.y - other.x * other.y, self.x * other.x - self.y * other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

# function to run task 2
def task2():
    p1 = Pair(3, 2)
    p2 = Pair(1, 5)
    p3 = Pair(4, 3)

    print("\nGiven test case:")
    print(f"p1: {p1}, p2: {p2}, p3: {p3}")
    print(f"p1 + p2 = {p1} + {p2} = {p1 + p2}")
    print(f"p1 * p2 = {p1} * {p2} = {p1 * p2}")
    print(f"p1 / p2 = {p1} / {p2} = {p1 / p2}")
    print(f"p1 + p2 * p3 = {p1} + {p2} * {p3} = {p1 + p2 * p3}")
    print(f"p1 * p2 / p3 + p1 = {p1} * {p2} / {p3} + {p1} = {p1 * p2 / p3 + p1}")

    print("\nMy test cases:")
    p4 = Pair(1, 5)
    p5 = Pair(8, 6)
    p6 = Pair(1, 5)
    
    print(f"p4: {p4}, p5: {p5}, p6: {p6}")
    print(f"p4 + p5 = {p4} + {p5} = {p4 + p5}")
    print(f"p4 * p5 = {p4} * {p5} = {p4 * p5}")
    print(f"p4 / p5 = {p4} / {p5} = {p4 / p5}")
    
    print("\nTesting equals:")
    print(f"p4 == p6: {p4 == p6}")
    print(f"p4 == p5: {p4 == p5}")

'''
Given test case:
p1: <3, 2>, p2: <1, 5>, p3: <4, 3>
p1 + p2 = <3, 2> + <1, 5> = <4, 7>
p1 * p2 = <3, 2> * <1, 5> = <3, 10>
p1 / p2 = <3, 2> / <1, 5> = <1, -7>
p1 + p2 * p3 = <3, 2> + <1, 5> * <4, 3> = <7, 17>
p1 * p2 / p3 + p1 = <3, 2> * <1, 5> / <4, 3> + <3, 2> = <21, -16>

My test cases:
p4: <1, 5>, p5: <8, 6>, p6: <1, 5>
p4 + p5 = <1, 5> + <8, 6> = <9, 11>
p4 * p5 = <1, 5> * <8, 6> = <8, 30>
p4 / p5 = <1, 5> / <8, 6> = <-43, -22>

Testing equals:
p4 == p6: True
p4 == p5: False
'''


# TASK 3: Translate java code to python about bicycles

# define Bicycle class
class Bicycle:
    # define constructor
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    # define applyBreak
    def applyBrake(self, decrement):
        self.speed -= decrement

    # define speedUp
    def speedUp(self, increment):
        self.speed += increment
        
    # define upGear
    def upGear(self):
        self.gear += 1
    
    # define downGear
    def downGear(self):
        self.gear -= 1

    # define string method
    def __str__(self):
        return f"\tNo of gears: {self.gear}\n\tSpeed of bicyle: {self.speed}"

# define MountainBike class that inherits from Bicycle
class MountainBike(Bicycle):
    # define constructor
    def __init__(self, gear, speed, seatHeight):
        super().__init__(gear, speed)
        self.seatHeight = seatHeight

    # define setHeight
    def setHeight(self, newValue):
        self.seatHeight = newValue

    # new methods overriding methods from parent class
    def upGear(self):
        self.gear += 2
    def downGear(self):
        self.gear -= 2
        
    # new methods not overriding any method from parent class
    def lowerSeatHeight(self, decrement):
        self.seatHeight -= decrement
        
    def raiseSeatHeight(self, increment):
        self.seatHeight += increment
    
    # define string method that overrides super
    def __str__(self):
        return super().__str__() + f"\n\tSeat height: {self.seatHeight}"
    

        


def task3():
    # test Bicycle class
    bike = Bicycle(5, 20)
    print("\nTESTING BICYLE:")
    print(bike)
    
    bike.speedUp(10)
    print(f"After speeding up:\n{bike}")
    
    bike.applyBrake(5)
    print(f"After applying break:\n{bike}")
    
    bike.downGear()
    print(f"After down gear:\n{bike}")
    
    bike.upGear()
    print(f"After up gear:\n{bike}")

    # test MountainBike class
    mtb = MountainBike(7, 15, 30)
    print("\nTESTING MOUNTAINBIKE:")
    print(mtb)
    
    mtb.setHeight(35)
    print(f"After changing seat height:\n{mtb}")
    
    mtb.speedUp(10)
    print(f"After speeding up:\n{mtb}")
    
    mtb.applyBrake(5)
    print(f"After applying brake:\n{mtb}")
    
    mtb.lowerSeatHeight(5)
    print(f"After lowering seat height:\n{mtb}")
    
    mtb.raiseSeatHeight(5)
    print(f"After raising seat height:\n{mtb}")
    
    mtb.upGear()
    print(f"After up gear:\n{mtb}")
    
    mtb.downGear()
    print(f"After down gear:\n{mtb}")

'''
TESTING BICYLE:
        No of gears: 5
        Speed of bicyle: 20
After speeding up:
        No of gears: 5
        Speed of bicyle: 30
After applying break:
        No of gears: 5
        Speed of bicyle: 25
After down gear:
        No of gears: 4
        Speed of bicyle: 25
After up gear:
        No of gears: 5
        Speed of bicyle: 25

TESTING MOUNTAINBIKE:
        No of gears: 7
        Speed of bicyle: 15
        Seat height: 30
After changing seat height:
        No of gears: 7
        Speed of bicyle: 15
        Seat height: 35
After speeding up:
        No of gears: 7
        Speed of bicyle: 25
        Seat height: 35
After applying brake:
        No of gears: 7
        Speed of bicyle: 20
        Seat height: 35
After lowering seat height:
        No of gears: 7
        Speed of bicyle: 20
        Seat height: 30
After raising seat height:
        No of gears: 7
        Speed of bicyle: 20
        Seat height: 35
After up gear:
        No of gears: 9
        Speed of bicyle: 20
        Seat height: 35
After down gear:
        No of gears: 7
        Speed of bicyle: 20
        Seat height: 35
'''

def main():
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()
    