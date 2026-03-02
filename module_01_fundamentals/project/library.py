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
        return next((book for book in self.books if book.title == title),None)
    


    def get_books_by_author(self,author):
        return [book for book in self.books if book.author == author]
    
    def get_total_value(self):
        return sum(book.price for book in self.books)