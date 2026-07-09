# Create a new type called Person, the Person object should have name attribute as well as a talk() method

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

person1 = Person("Kolawole")
person1.talk()

person2 = Person("Loni")
person2.talk()
