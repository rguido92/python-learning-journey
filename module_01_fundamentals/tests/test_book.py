from module_01_fundamentals.project.book import Book

# Test  1 . CRear un libro correctamente
def test_create_book():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"
    assert book.price == 10.99

# Test 2. El titulo no puede estar vacio
def test_book_title_not_empty():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    assert book.title != ""
    
# Test 3. El precio no puede ser negativo
def test_book_price_not_negative():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
    assert book.price >= 0
    