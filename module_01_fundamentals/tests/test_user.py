from module_01_fundamentals.project.user import User
from module_01_fundamentals.project.book import Book


def test_user_creation():
    user = User("Rodrigo", "rodrigo@gmail.com")
    assert user.name == "Rodrigo"
    assert user.email == "rodrigo@gmail.com"
    user.shopping_cart = []


def test_user_name_not_empty():
    user = User("Alejandro", "alejandro@gmail.com")
    assert user.name != ""


def test_add_book_to_cart():
    user = User("Rodrigo", "rodrigo@gmail.com")
    book = Book("Clean Code", "Robert Martin", 35.0)
    user.add_to_cart(book)
    assert len(user.shopping_cart) == 1


def test_delete_book_to_cart():
    user = User("Rodrigo", "rodrigo@gmail.com")
    book = Book("Clean Code", "Robert Martin", 35.0)
    user.add_to_cart(book)
    user.delete_book(book)
    assert len(user.shopping_cart) == 0


def test_delete_nonexistent_book_returns_none():
    user = User("Rodrigo", "rodrigo@gmail.com")
    result = user.delete_book(Book("Libro fantasma", "Autor anonimo", 20.0))
    assert result is None


def test_get_total_value_cart():
    user = User("Rodrigo", "rodrigo@gmail.com")
    book = Book("Clean Code", "Robert Martin", 35.0)
    user.add_to_cart(book)
    book2 = Book("Clean Code", "Robert Martin", 40.0)
    user.add_to_cart(book2)
    assert user.get_total_of() == 75.0


def test_user_str_representation():
    user = User("Rodrigo", "rodrigo@gmail.com")
    book = Book("Clean Code", "Robert Martin", 35.0)
    user.shopping_cart.append(book)
    book = Book("Python Crash Course", "Eric Matthes", 29.99)
    user.shopping_cart.append(book)
    assert (
        str(user)
        == "Username: Rodrigo\nEmail: rodrigo@gmail.com\nShopping cart:Clean Code by Robert Martin - 35.0€\nPython Crash Course by Eric Matthes - 29.99€"
    )


# ¿Qué pasa si intentas eliminar un libro que no está en el carrito?¿El total del carrito se calcula correctamente?¿El resumen en texto del usuario tiene el formato correcto?##
