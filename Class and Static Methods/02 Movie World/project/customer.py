from project import dvd


class Customer:
    def __init__(self, name: str, age: int, id_: int):
        self.name = name
        self.age = age
        self.id = id_
        self.rented_dvds: list[dvd] = []

    def __repr__(self) -> str:
        titles = ', '.join([d.name for d in self.rented_dvds])
        return f'{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD\'s ({titles})'