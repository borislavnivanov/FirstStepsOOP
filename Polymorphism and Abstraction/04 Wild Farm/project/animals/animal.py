from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def food_options(self) -> list[Food]:
        pass

    @property
    @abstractmethod
    def  weight_gain(self) -> float:
        pass

    def feed(self, food: Food):
        if type(food) not in self.food_options:
            return f'{self.__class__.__name__ } does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * self.weight_gain
        self.food_eaten += food.quantity

class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size: float = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'