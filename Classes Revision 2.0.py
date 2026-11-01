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
