class Car:
    def driver(self):
        return "Am a car"
    
class Bike:
    def driver(self):
        return "Am a bike"
    
class factory:
    @staticmethod
    def check(name):
        if name == "car":
            return Car()
        elif name == "bike":
            return Bike()
        else:
            return ValueError

# Correct way:
vehicle = factory.check("car")  # Directly calls static method and stores Car instance
print(vehicle.driver())  # Works because vehicle is a Car instance

# Alternative way using instance:
obj = factory()
vehicle = obj.check("bike") # Also works but unnecessary instance creation
print(vehicle.driver())
