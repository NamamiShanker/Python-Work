class Dog:

    def __init__(self, n, b, c):
        self.name = n
        self.breed = b
        self.color = c

    def bark(self):
        print("bhaw bhaw")

    def run(self):
        print("Your dog ran 100 mts")

    def fetch(self):
        print("Your dog brought back the stick")

    def eat(self):
        print("Your dog ate all the food in the refrigerator")


dog1 = Dog()

# class - It is the blueprint to create objects
# object - It is a data structured in the form of a scpecific class
# data members - The information about the object
# member functions/functions/methods - The functions of the object.
# Attributes - data members and member functions are called attributes collectively
# Constructor - A special functions that helps define the data members of that class.
