import io
import json
from unittest.mock import MagicMock, patch
import pytest
from module_04_web.project.app import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


class TestLibraryRoutes:
    def test_list_books(self, client):
        resp = client.get("/books")
        assert resp.status_code == 200
        data = resp.get_json()
        assert isinstance(data, list)
        assert len(data) == 3

    def test_list_books_paginated_page_1(self, client):
        resp = client.get("/books?page=1&page_size=2")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["page"] == 1
        assert data["page_size"] == 2
        assert data["total_pages"] == 2
        assert data["total_books"] == 3
        assert len(data["books"]) == 2

    def test_list_books_paginated_page_2(self, client):
        resp = client.get("/books?page=2&page_size=2")
        assert resp.status_code == 200
        data = resp.get_json()
        assert len(data["books"]) == 1

    def test_list_books_paginated_out_of_range(self, client):
        resp = client.get("/books?page=99&page_size=2")
        assert resp.status_code == 404

    def test_get_book_found(self, client):
        resp = client.get("/books/1984")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["title"] == "1984"
        assert data["author"] == "George Orwell"
        assert data["price"] == 8.99

    def test_get_book_not_found(self, client):
        resp = client.get("/books/nonexistent")
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "Book not found"

    def test_add_book(self, client):
        resp = client.post("/books", json={
            "title": "Clean Code",
            "author": "Robert Martin",
            "price": 55.0,
        })
        assert resp.status_code == 201
        data = resp.get_json()
        assert data["title"] == "Clean Code"

    def test_add_duplicate_book(self, client):
        resp = client.post("/books", json={
            "title": "1984",
            "author": "George Orwell",
            "price": 8.99,
        })
        assert resp.status_code == 409

    def test_add_book_missing_fields(self, client):
        resp = client.post("/books", json={"title": "Incomplete"})
        assert resp.status_code == 400

    def test_add_book_invalid_price(self, client):
        resp = client.post("/books", json={
            "title": "Bad",
            "author": "Author",
            "price": "not-a-number",
        })
        assert resp.status_code == 400

    def test_filter_books_by_author(self, client):
        resp = client.get("/library/books?author=George Orwell")
        assert resp.status_code == 200
        data = resp.get_json()
        assert len(data) == 1
        assert data[0]["title"] == "1984"

    def test_filter_books_by_max_price(self, client):
        resp = client.get("/library/books?max_price=10")
        assert resp.status_code == 200
        data = resp.get_json()
        assert len(data) == 2
        assert all(b["price"] <= 10 for b in data)

    def test_filter_books_invalid_max_price(self, client):
        resp = client.get("/library/books?max_price=abc")
        assert resp.status_code == 400


class TestExportImportRoutes:
    def test_export_csv(self, client):
        resp = client.post("/library/export/csv")
        assert resp.status_code == 200
        data = resp.get_json()
        assert "catalogue.csv" in data["message"]

    def test_export_json(self, client):
        resp = client.post("/library/export/json")
        assert resp.status_code == 200
        data = resp.get_json()
        assert "catalogue.json" in data["message"]

    def test_export_invalid_format(self, client):
        resp = client.post("/library/export/xml")
        assert resp.status_code == 400

    def test_import_csv(self, client):
        csv_content = b"title,author,price\nTest Book,Test Author,9.99\n"
        resp = client.post(
            "/library/import/csv",
            data={"file": (io.BytesIO(csv_content), "test.csv")},
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["total_books"] == 4

    def test_import_json(self, client):
        json_content = json.dumps([
            {"title": "Test Book", "author": "Test Author", "price": 9.99},
        ]).encode()
        resp = client.post(
            "/library/import/json",
            data={"file": (io.BytesIO(json_content), "test.json")},
        )
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["total_books"] == 4

    def test_import_no_file(self, client):
        resp = client.post("/library/import/csv")
        assert resp.status_code == 400

    def test_import_invalid_format(self, client):
        resp = client.post("/library/import/xml")
        assert resp.status_code == 400


class TestSalesRoutes:
    @patch("module_04_web.project.app.CatalogueAnalysis")
    def test_total_revenue(self, mock_catalogue, client):
        mock_instance = MagicMock()
        mock_instance.get_total_revenue.return_value = 50000.0
        mock_catalogue.return_value = mock_instance
        resp = client.get("/sales/revenue")
        assert resp.status_code == 200
        assert resp.get_json()["total_revenue"] == 50000.0

    @patch("module_04_web.project.app.CatalogueAnalysis")
    def test_best_seller(self, mock_catalogue, client):
        mock_instance = MagicMock()
        mock_instance.get_best_seller.return_value = "Atomic Habits"
        mock_catalogue.return_value = mock_instance
        resp = client.get("/sales/best-seller")
        assert resp.status_code == 200
        assert resp.get_json()["best_seller"] == "Atomic Habits"

    @patch("module_04_web.project.app.CatalogueAnalysis")
    def test_revenue_by_genre(self, mock_catalogue, client):
        mock_instance = MagicMock()
        mock_instance.get_revenue_by_genre.return_value = {
            "Fiction": 5000, "Programming": 8000,
        }
        mock_catalogue.return_value = mock_instance
        resp = client.get("/sales/revenue-by-genre")
        assert resp.status_code == 200
        assert resp.get_json() == {"Fiction": 5000, "Programming": 8000}

    def test_get_chart_not_found(self, client):
        resp = client.get("/sales/charts/nonexistent.png")
        assert resp.status_code == 404

    def test_get_chart_found(self, client, tmp_path, monkeypatch):
        monkeypatch.setattr("module_04_web.project.app.CHARTS_DIR", tmp_path)
        dummy_png = tmp_path / "test_chart.png"
        dummy_png.write_text("fake-png-content")
        resp = client.get("/sales/charts/test_chart.png")
        assert resp.status_code == 200
        assert resp.mimetype == "image/png"
