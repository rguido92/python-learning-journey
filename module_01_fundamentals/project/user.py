##Ticket #003 — Clase User
# Un usuario tiene nombre, email y un carrito de compra. Debe poder añadir libros al carrito, eliminarlos, calcular el total y mostrar un resumen en texto. Piensa también en los casos raros: ¿qué pasa si intentas eliminar un libro que no está en el carrito?##


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []

    def add_to_cart(self, book):
        self.shopping_cart.append(book)

    def delete_book(self, book):
        self.shopping_cart = [item for item in self.shopping_cart if item != book]

    def get_total_of(self):
        return sum(book.price for book in self.shopping_cart)

    def __str__(self):
        cart_str = "\n".join(str(book) for book in self.shopping_cart)
        return f"Username: {self.name}\nEmail: {self.email}\nShopping cart:{cart_str}"
