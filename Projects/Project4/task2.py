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