import calendar

class DVD:
    def __init__(self, name: str, id_: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id_
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented: bool = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> 'DVD':
        parse_date, parse_month, parse_year = date.split('.') # day.month.year
        return cls(name, id, int(parse_year), calendar.month_name[int(parse_month)], age_restriction)

    def __repr__(self) -> str:
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {"rented" if self.is_rented else "not rented"}'