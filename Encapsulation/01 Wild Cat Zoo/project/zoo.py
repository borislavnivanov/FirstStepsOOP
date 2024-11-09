from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return 'Not enough budget'
        if self.__animal_capacity <= len(self.animals):
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity <= len(self.workers):
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self) -> str:
        total_pay = sum([x.salary for x in self.workers])
        if self.__budget >= total_pay:
            self.__budget -= total_pay
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_care = sum([x.money_for_care for x in self.animals])
        if self.__budget >= total_care:
            self.__budget -= total_care
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        return self.__stat_printer(self.animals, 'Lion', 'Tiger', 'Cheetah')
        # lions = [repr(x) for x in self.animals if x.__class__.__name__ == 'Lion']
        # tiger = [repr(x) for x in self.animals if x.__class__.__name__ == 'Tiger']
        # cheetah = [repr(x) for x in self.animals if x.__class__.__name__ == 'Cheetah']
        # result = [f'You have {len(self.animals)} animals']
        # result.append(f'----- {len(lions)} Lions:')
        # result.append(x for x in lions)
        # result.append(f'----- {len(tiger)} Tigers:')
        # result.append(x for x in tiger)
        # result.append(f'----- {len(cheetah)} Cheetahs:')
        # result.append(x for x in cheetah)
        # return '\n'.join(result)

    def workers_status(self) -> str:
        return self.__stat_printer(self.workers, 'Keeper', 'Caretaker', 'Vet')
        # keeper = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Keeper']
        # caretaker = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Caretaker']
        # vet = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Vet']
        # result = [f'You have {len(self.workers)} workers']
        # result.append(f'----- {len(keeper)} Keepers:')
        # result.extend(keeper)
        # result.append(f'----- {len(caretaker)} Caretakers:')
        # result.extend(caretaker)
        # result.append(f'----- {len(vet)} Vets:')
        # result.extend(vet)
        # return '\n'.join(result)

    @staticmethod
    def __stat_printer(object_list: list[Animal | Worker], *class_names: str) -> str:

        elements = {name: [] for name in class_names}
        for obj in object_list:
            elements[obj.__class__.__name__].append(repr(obj))

        result = [f'You have {len(object_list)} {str(object_list[0].__class__.__bases__[0].__name__).lower()}s']

        for key, value in elements.items():
            result.append(f'----- {len(value)} {key}s:')
            result.extend(value)

        return '\n'.join(result)
