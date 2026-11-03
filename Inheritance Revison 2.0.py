
class Mammal:# This is the parent class, ypu see its done so that walk iss not repeated in cat and dog, cause the plan was to create the
    # method walk in both walk and cat.
    def walk(self):
        print("Walk") # So when you use the dog class, ypu can make use of the walk method because the dog class inherited it.
class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")

dog1 = Dog()
dog1.walk()
