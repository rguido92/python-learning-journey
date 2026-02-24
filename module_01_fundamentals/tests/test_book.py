from module_01_fundamentals.project.book import Book

# Test  1 . CRear un libro correctamente
def test_book_creation():
    book = Book("Clean Code", "Robert Martin", 35.0)
    assert book.title == "Clean Code"
    assert book.author == "Robert Martin"
    assert book.price == 35.0

# Test 2. El titulo no puede estar vacio
def test_book_title_not_empty():
    book = Book("El Quijote", "Cervantes", 20.0)
    assert book.title != ""
    
# Test 3. El precio no puede ser negativo
def test_book_price_is_positive():
    book = Book("Python Crash Course", "Eric Matthes", 29.99)
    assert book.price > 0
        
# Test 4. Aplicar un descuento al precio del libro

def test_book_apply_discount():
    book = Book("Clean Code","Robert Martin",40.0)
    result = book.apply_discount(25)
    assert result == 30.0
    
# Test 5. El descuento no puede ser mayor al 100%

def test_discount_canoot_exceed_100():
    book = Book("Clean Code","Robert Martin",40)
    result = book.apply_discount(110)
    assert result == 0.0 

# Test 6. Representación en texto del libro

def test_book_str_representation():
    book = Book("Clean Code", "Robert Martin", 35.0)
    assert str(book) == "Clean Code by Robert Martin - 35.0€"