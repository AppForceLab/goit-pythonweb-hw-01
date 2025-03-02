from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Клас для представлення книги
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

# Інтерфейс для бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        pass

# Реалізація бібліотеки
class Library(LibraryInterface):
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f'Книга додана: {book}')

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logger.info(f'Книга видалена: {title}')

    def get_books(self) -> list[Book]:
        return self.books

# Клас для управління бібліотекою
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        books = self.library.get_books()
        if books:
            for book in books:
                logger.info(book)
        else:
            logger.info("Бібліотека порожня")

# Головна функція
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Введіть команду (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Введіть назву книги: ").strip()
                author = input("Введіть автора книги: ").strip()
                year = int(input("Введіть рік видання: ").strip())
                manager.add_book(title, author, year)
            case "remove":
                title = input("Введіть назву книги для видалення: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Невідома команда. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
