from module_01_fundamentals.project.library import Library
from module_01_fundamentals.project.book import Book

def test_library_starts_empty():
    library = Library("Libreria Central")
    assert library.name == "Libreria Central"
    assert library.books == []

def test_add_book():
    library = Library("Libreria Central")
    book = Book("Clean Code","Robert Martin",35.0)
    library.add_book(book)
    assert len(library.books) == 1

def test_add_duplicate_book_raises_error():
    library = Library("Libreria Central")
    book = Book("Clean Code","Robert Martin",35.0)
    library.add_book(book)
    library.add_book(book)
    assert len(library.books) == 1

def test_search_by_title():
    library = Library("Libreria Central")
    library.add_book(Book("Clean Code", "Robert Martin", 35.0))
    library.add_book(Book("The Pragmatic Programmer", "David Thomas", 40.0))
    result = library.search_by_title("Clean Code")
    assert result.title == "Clean Code"

def test_search_nonexistent_book_returns_none():
    library = Library("Librería Central")
    result = library.search_by_title("Libro Fantasma")
    assert result is None

def test_get_books_by_author():
    library = Library("Libreria Central")
    library.add_book(Book("Clean Code", "Robert Martin", 35.0))
    library.add_book(Book("Clean Architecture", "Robert Martin", 38.0))
    library.add_book(Book("The Pragmatic Programmer", "David Thomas", 40.0))
    result = library.get_books_by_author("Robert Martin")
    assert len(result) == 2

def test_get_total_value():
    library = Library("Librería Central")
    library.add_book(Book("Clean Code", "Robert Martin", 35.0))
    library.add_book(Book("The Pragmatic Programmer", "David Thomas", 40.0))
    assert library.get_total_value() == 75.0