from module_01_fundamentals.project.book import Book

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            return None
    
    def search_by_title(self,title):
        for book in self.books:
            if book.title==title:
                return book
        return None


    def get_books_by_author(self,author):
        books_finded = []
        for book in self.books:
            if book.author==author:
                books_finded.append(book)
        return books_finded
    
    def get_total_value(self):
        value = 0
        for book in self.books:
            value+= book.price
        return value