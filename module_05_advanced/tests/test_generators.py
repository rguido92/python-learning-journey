import pytest
from module_05_advanced.project.generators import (
    paginate_books,
    chunked_import,
    stream_csv_rows,
)


class TestPaginateBooks:
    def test_default_page_size(self):
        books = list(range(25))
        pages = list(paginate_books(books))
        assert len(pages) == 3
        assert len(pages[0]) == 10
        assert len(pages[1]) == 10
        assert len(pages[2]) == 5

    def test_custom_page_size(self):
        books = list(range(25))
        pages = list(paginate_books(books, page_size=7))
        assert len(pages) == 4
        assert len(pages[0]) == 7

    def test_empty_list(self):
        pages = list(paginate_books([]))
        assert pages == []

    def test_single_page(self):
        books = list(range(5))
        pages = list(paginate_books(books, page_size=10))
        assert len(pages) == 1
        assert pages[0] == [0, 1, 2, 3, 4]

    def test_returns_iterator(self):
        books = [1, 2, 3]
        result = paginate_books(books, page_size=2)
        assert iter(result) is result


class TestStreamCsvRows:
    def test_streams_rows(self, tmp_path):
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("a,b\n1,2\n3,4\n")
        rows = list(stream_csv_rows(str(csv_file)))
        assert len(rows) == 2
        assert rows[0] == {"a": "1", "b": "2"}
        assert rows[1] == {"a": "3", "b": "4"}

    def test_empty_csv(self, tmp_path):
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text("a,b\n")
        rows = list(stream_csv_rows(str(csv_file)))
        assert rows == []


class TestChunkedImport:
    def test_chunks_correctly(self, tmp_path):
        csv_file = tmp_path / "data.csv"
        csv_file.write_text(
            "title,author,price\n"
            "A,Auth1,10\nB,Auth2,20\nC,Auth3,30\n"
        )
        chunks = list(chunked_import(str(csv_file), chunk_size=2))
        assert len(chunks) == 2
        assert len(chunks[0]) == 2
        assert len(chunks[1]) == 1

    def test_single_chunk(self, tmp_path):
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("x,y\n1,2\n")
        chunks = list(chunked_import(str(csv_file), chunk_size=10))
        assert len(chunks) == 1
        assert chunks[0] == [{"x": "1", "y": "2"}]
