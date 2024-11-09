class Customer:
    id = 1
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()

    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1

    def __repr__(self) -> str:
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
