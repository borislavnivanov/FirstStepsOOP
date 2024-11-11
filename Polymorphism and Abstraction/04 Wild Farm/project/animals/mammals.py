from project import food
from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    @property
    def weight_gain(self) -> float:
        return 0.10

    @property
    def food_options(self) -> list[food]:
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound() -> str:
        return 'Squeak'

class Dog(Mammal):
    @property
    def weight_gain(self) -> float:
        return 0.40

    @property
    def food_options(self) -> list[food]:
        return [Meat]

    @staticmethod
    def make_sound() -> str:
        return 'Woof'

class Cat(Mammal):
    @property
    def weight_gain(self) -> float:
        return 0.30

    @property
    def food_options(self) -> list[food]:
        return [Vegetable, Meat]

    @staticmethod
    def make_sound() -> str:
        return 'Meow'

class Tiger(Mammal):
    @property
    def weight_gain(self) -> float:
        return 1.00

    @property
    def food_options(self) -> list[food]:
        return [Meat]

    @staticmethod
    def make_sound() -> str:
        return 'ROAR!!!'