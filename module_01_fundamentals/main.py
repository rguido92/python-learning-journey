# Pruebas de ejercicios modulo_01_fundamentals : Book, Library. User

from module_01_fundamentals.project.book import Book
from module_01_fundamentals.project.library import Library
from module_01_fundamentals.project.user import User

# Crear algunos libros
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 9.99)
book3 = Book("1984", "George Orwell", 8.99)
# Crear una biblioteca y agregar libros
library = Library("City Library")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
# Crear un usuario name,email, shopping_cart
user = User("Alice", "alice@gmail.com")
# Agregar libros al carrito del usuario
user.add_to_cart(book1)
user.add_to_cart(book2)
user.add_to_cart(book3)
# Mostrar el carrito del usuario
print(user)
# Calcular el total del carrito
total = user.get_total_of()
print(f"Total: ${total}")
# Eliminar un libro del carrito
user.delete_book(book1)
# Mostrar el carrito del usuario después de eliminar un libro
print(user)

total = user.get_total_of()


# Intentar eliminar un libro que no está en el carrito
user.delete_book(book3)
# Mostrar el carrito del usuario después de intentar eliminar un libro que no está en el carrito
print(user)
