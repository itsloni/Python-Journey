class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Moving Point")

    def draw(self):
        print("Drawing Point")

point = Point(10, 20)
point.x = 11
print(point.x)