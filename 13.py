class LibraryError(Exception):
    """Базовий клас для помилок бібліотеки."""
    pass


class BookNotFoundError(LibraryError):
    """Виняток: книга не знайдена в каталозі."""
    pass


class BookNotAvailableError(LibraryError):
    """Виняток: всі примірники книги видані."""
    pass


class BookAlreadyReturnedError(LibraryError):
    """Виняток: книга вже повернута або не була видана."""
    pass


class InvalidQuantityError(LibraryError):
    """Виняток: некоректна кількість книг."""
    pass


class Library:
    """Клас для управління бібліотекою."""

    def __init__(self):
        self.catalog = {}

    def add_book(self, title, quantity=1):
        if quantity <= 0:
            raise InvalidQuantityError("Кількість книг повинна бути додатною")

        if title not in self.catalog:
            self.catalog[title] = {
                "total": quantity,
                "available": quantity,
                "borrowed_by": []
            }
        else:
            self.catalog[title]["total"] += quantity
            self.catalog[title]["available"] += quantity

    def borrow_book(self, title, user):
        if title not in self.catalog:
            raise BookNotFoundError("Книгу не знайдено в каталозі")

        if self.catalog[title]["available"] <= 0:
            raise BookNotAvailableError("Усі примірники книги вже видані")

        self.catalog[title]["available"] -= 1
        self.catalog[title]["borrowed_by"].append(user)

    def return_book(self, title, user):
        if title not in self.catalog:
            raise BookNotFoundError("Книгу не знайдено в каталозі")

        if user not in self.catalog[title]["borrowed_by"]:
            raise BookAlreadyReturnedError(
                "Цей користувач не брав дану книгу"
            )

        self.catalog[title]["available"] += 1
        self.catalog[title]["borrowed_by"].remove(user)

    def show_catalog(self):
        if not self.catalog:
            print("Каталог порожній.")
            return

        print("Каталог бібліотеки:")
        for title, info in self.catalog.items():
            print(
                f"- {title}: "
                f"усього {info['total']}, "
                f"доступно {info['available']}, "
                f"видано: {', '.join(info['borrowed_by']) or 'немає'}"
            )


if __name__ == "__main__":
    library = Library()

    print("=== Система управління бібліотекою ===\n")

    try:
        # 1. Додаємо книги
        library.add_book("Майстер і Маргарита", 3)
        library.add_book("Кобзар", 2)

        # 2. Видаємо книги
        library.borrow_book("Майстер і Маргарита", "Олена")
        library.borrow_book("Кобзар", "Андрій")

        # 3. Повертаємо книгу
        library.return_book("Кобзар", "Андрій")

        # 4. Показуємо каталог
        library.show_catalog()

    except LibraryError as e:
        print("❌ Помилка бібліотеки:", e)
