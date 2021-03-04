from abc import ABC
# from abc import abstractmethod


class Vehicle(ABC):

    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        pass

    def wheels_num(self):
        pass

    def vehicle_type(self) -> str:
        pass

    def is_motorcycle(self) -> bool:
        pass

    def purchase_price(self) -> float:
        pass


# Don't change class implementation
class Car(Vehicle):
    wheels_num = 4


# Don't change class implementation
class Motorcycle(Vehicle):
    wheels_num = 2


# Don't change class implementation
class Truck(Vehicle):
    wheels_num = 10


# Don't change class implementation
class Bus(Vehicle):
    wheels_num = 6
