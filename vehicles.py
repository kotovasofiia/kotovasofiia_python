class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def start_engine(self):
        print("Starting the engine...")


class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        print("The car's engine is starting...")

    def drive(self):
        print("The car is now driving.")


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        print("The truck's engine is starting...")

    def haul(self):
        print("The truck is hauling cargo.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("The motorcycle's engine is starting...")

    def ride(self):
        print("The motorcycle is now riding.")


car1 = Car("Mercedes", "AMG GT", 2023, 1630, 2, 2)
truck1 = Truck("Ford", "F-150", 2021, 2500, 1000, 3500)
moto1 = Motorcycle("Honda", "CBR500R", 2023, 190, 2, False)

car1.start_engine()
car1.drive()

truck1.start_engine()
truck1.haul()

moto1.start_engine()
moto1.ride()

vehicle_list = [car1, truck1, moto1]
for v in vehicle_list:
    v.start_engine()
