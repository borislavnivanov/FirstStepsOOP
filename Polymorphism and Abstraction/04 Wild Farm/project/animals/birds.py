from project import food
from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @property
    def weight_gain(self) -> float:
        return 0.25

    @property
    def food_options(self) -> list[food]:
        return [Meat]

    @staticmethod
    def make_sound() -> str:
        return 'Hoot Hoot'

class Hen(Bird):
    @property
    def weight_gain(self) -> float:
        return 0.35

    @property
    def food_options(self) -> list[food]:
        return [Vegetable, Fruit, Meat, Seed]

    @staticmethod
    def make_sound() -> str:
        return 'Cluck'