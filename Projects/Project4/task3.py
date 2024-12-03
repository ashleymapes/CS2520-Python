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