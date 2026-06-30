from module_01_fundamentals.project.library import Library
from module_01_fundamentals.project.book import Book
from module_05_advanced.project.decorators import log_call
from module_05_advanced.project.context_managers import Timer


class FileManager:
    def __init__(self, library):
        self.library = library

    def ensure_directory_exists(self, file_path):
        import os

        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    @log_call
    def export_to_csv(self, file_path):
        import csv

        self.ensure_directory_exists(file_path)
        with Timer():
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["title", "author", "price"])
                for book in self.library.books:
                    writer.writerow([book.title, book.author, book.price])

    @log_call
    def export_to_json(self, file_path):
        import json

        self.ensure_directory_exists(file_path)
        with Timer():
            with open(file_path, "w") as file:
                json.dump(
                    [
                        {
                            "title": book.title,
                            "author": book.author,
                            "price": book.price,
                        }
                        for book in self.library.books
                    ],
                    file,
                    indent=4,
                )

    @log_call
    def import_from_csv(self, file_path):
        import csv
        import os

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe.")

        with Timer():
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(
                        title=row["title"],
                        author=row["author"],
                        price=float(row["price"]),
                    )
                    self.library.add_book(book)

    @log_call
    def import_from_json(self, file_path):
        import json
        import os

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe.")

        with Timer():
            with open(file_path, "r") as file:
                books = json.load(file)
                for book in books:
                    book = Book(
                        title=book["title"],
                        author=book["author"],
                        price=float(book["price"]),
                    )
                    self.library.add_book(book)
