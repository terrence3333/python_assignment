# Base class
class Vehicle:
    def move(self):
        pass  # Generic method

# Child classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵️")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each class responds differently
