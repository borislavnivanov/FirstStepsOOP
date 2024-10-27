from project.user import User


class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str , list[str]] = {}
        self.rented_books: dict[str , dict[str, str]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):


