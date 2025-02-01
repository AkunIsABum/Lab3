import math
#-------------------------------------------------------------------------------TASK ONE-------------------------------------------------------------------------------------------------
class String1:
    def __init__(self):
        self.value = ""

    def getString(self):
        self.value = input("Enter a string: ")

    def printString(self):
        print(self.value.upper())


#-------------------------------------------------------------------------------TASK TWO-------------------------------------------------------------------------------------------------
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

#-------------------------------------------------------------------------------TASK THREE-------------------------------------------------------------------------------------------------
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
      
#-------------------------------------------------------------------------------TASK FOUR-------------------------------------------------------------------------------------------------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Point moved to: ({self.x}, {self.y})")

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


#-------------------------------------------------------------------------------TASK FIVE-------------------------------------------------------------------------------------------------
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal denied. No Moners. :( ")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"
      
#-------------------------------------------------------------------------------MAIN-------------------------------------------------------------------------------------------------
str = String1()
str.getString()
str.printString()

shape = Shape()
print("Area of Shape:", shape.area())

square = Square(5)
print("Area of Square:", square.area())

rectangle = Rectangle(4, 6)
print("Area of Rectangle:", rectangle.area())

point1 = Point(1, 2)
point2 = Point(4, 6)

point1.show()
point2.show()

point1.move(3, 5)
point1.show()

distance = point1.dist(point2)
print(f"Distance between points: {distance:.2f}")


acc = Account("John", 100)

print(acc)

acc.deposit(50)
acc.deposit(200)

acc.withdraw(75)
acc.withdraw(300)
acc.withdraw(200)

print(acc)
