class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10 #These are attributes. They belong to a class.
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 1
print(point2.x)
point1.move()
point1.draw()


# CONSTRUCTORS

class Point:
    def __init__(self, x, y):#sSo this is the constructor and it's a function that gets called at the time of creating an object
        self.x = x # This is literally the same as point1.x = 10 just that the constructor take in the parameter
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10, 20)
print(point1.x, point1.y)


# Practice
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name} ")

person1 = Person("Loni")
person1.talk()
