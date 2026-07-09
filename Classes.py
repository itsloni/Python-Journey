class Point: #Here is where we define the Point type using classes
    def move(self):  # These are methods which are actions that belong exclusively to the class.
        print("Moving Point")
    def draw(self): # These are defined methods that derive from the type Point
        print("Drawing Point")
point1 = Point() # This is an object that is an instance of the class Point the Point() is stored in a variable
point1.x = 10 # These are variables called attributes that are attached to a specific object.
point1.y = 20 # These are variables called attributes that are attached to a specific object.
print(point1.x)
point1.draw()

point2 = Point() # This is an object that is an instance of the class Point the Point() is stored in a variable
point2.x = 30 # These are variables called attributes that are attached to a specific object.
print(point2.x)

