#James Klick
#Car Creator
#Version 1.0
#9/8/24

class Vehicle:
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

print("Currently available types of vehicles: Car, Truck, Plane, Boat, Broomstick")
car = Vehicle(input("What kind of vehicle are you creating?  "))
carYear = input("Enter car model year: ")
carMake = input("Enter car make: ")
carModel = input("Enter car model: ")
carDoors = input("Enter number of vehicle doors (2 or 4): ")
carRoof = input("Enter style of vehicle roof (solid or sun roof): ")

carComplex = Automobile(carYear, carMake, carModel, carDoors, carRoof)
print("Vehicle type: " + car.type)
print("Year: " + carComplex.year)
print("Make: " + carComplex.make)
print("Model: " + carComplex.model)
print("Number of Doors: " + carComplex.doors)
print("Type of roof: " + carComplex.roof)