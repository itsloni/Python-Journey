class Mammal:
    def walk(self):
        print("Why Not walk your pet?")

class Dog(Mammal):
    def bark(self):
        print("My pet Dog barks")

class Cat(Mammal):
    def meow(self):
        print("My pet Cat is violent")

action = Dog()
action.walk()
action.bark()