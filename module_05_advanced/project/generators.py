import csv
from typing import Iterator, Any


def paginate_books(books: list, page_size: int = 10) -> Iterator[list]:
    for i in range(0, len(books), page_size):
        yield books[i : i + page_size]


def chunked_import(file_path: str, chunk_size: int = 100) -> Iterator[list[dict]]:
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


def stream_csv_rows(file_path: str) -> Iterator[dict]:
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        yield from reader
