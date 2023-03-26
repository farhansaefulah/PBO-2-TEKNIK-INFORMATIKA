#Nama : Farhan Saefulah
#NIM : 210511059
#Kelas : R2


class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, color, wheels, speed):
        super().__init__(color, wheels)
        self.speed = speed

    def drive(self):
        print(f"The {self.color} car is driving at {self.speed} km/h.")

class ElectricCar(Car):
    def __init__(self, color, wheels, speed, battery_capacity):
        super().__init__(color, wheels, speed)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.color} electric car is charging its battery with {self.battery_capacity} kWh.")

my_electric_car = ElectricCar("blue", 4, 120, 60)
my_electric_car.drive()
my_electric_car.charge()
