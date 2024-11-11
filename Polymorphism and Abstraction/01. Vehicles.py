from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass


class Car(Vehicle):
    AIR_CONDITIONING_FUEL_USE = 0.9

    def drive(self, distance: int):
        fuel_needed_for_journey = distance * (self.fuel_consumption + self.AIR_CONDITIONING_FUEL_USE)

        if self.fuel_quantity >= fuel_needed_for_journey:
            self.fuel_quantity -= fuel_needed_for_journey

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    AIR_CONDITIONING_FUEL_USE = 1.6
    REFUELING_LIMIT = 0.95

    def drive(self, distance: int):
        fuel_needed_for_journey = distance * (self.fuel_consumption + self.AIR_CONDITIONING_FUEL_USE)

        if self.fuel_quantity >= fuel_needed_for_journey:
            self.fuel_quantity -= fuel_needed_for_journey

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * self.REFUELING_LIMIT

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

