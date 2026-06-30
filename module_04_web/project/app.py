from pathlib import Path
from flask import Flask, jsonify, request, send_file
from module_01_fundamentals.project.book import Book
from module_01_fundamentals.project.library import Library
from module_03_automation.project.file_manager import FileManager
from module_02_data_analysis.project.catalogue_analysis import CatalogueAnalysis
from module_05_advanced.project.decorators import measure_time, log_call
from module_05_advanced.project.generators import paginate_books

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SALES_CSV = BASE_DIR / "module_02_data_analysis" / "data" / "sales.csv"
CHARTS_DIR = BASE_DIR / "module_02_data_analysis" / "data" / "charts"
EXPORTS_DIR = BASE_DIR / "module_04_web" / "exports"


def create_app():
    app = Flask(__name__)

    library = Library("Online Library")
    file_manager = FileManager(library)

    for book_data in [
        ("The Great Gatsby", "F. Scott Fitzgerald", 12.99),
        ("To Kill a Mockingbird", "Harper Lee", 9.99),
        ("1984", "George Orwell", 8.99),
    ]:
        library.add_book(Book(*book_data))

    @app.route("/books", methods=["GET"])
    def list_books():
        page = request.args.get("page", default=None, type=int)
        page_size = request.args.get("page_size", default=10, type=int)
        all_books = [
            {"title": b.title, "author": b.author, "price": b.price}
            for b in library.books
        ]
        if page is not None:
            pages = list(paginate_books(all_books, page_size))
            if page < 1 or page > len(pages):
                return jsonify({"error": "Page out of range"}), 404
            return jsonify({
                "page": page,
                "page_size": page_size,
                "total_pages": len(pages),
                "total_books": len(all_books),
                "books": pages[page - 1],
            })
        return jsonify(all_books)

    @app.route("/books/<title>", methods=["GET"])
    @measure_time
    def get_book(title):
        book = library.search_by_title(title)
        if book is None:
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"title": book.title, "author": book.author, "price": book.price})

    @app.route("/books", methods=["POST"])
    @measure_time
    def add_book():
        data = request.get_json(silent=True)
        if not data or not all(k in data for k in ("title", "author", "price")):
            return jsonify({"error": "Missing required fields: title, author, price"}), 400
        try:
            price = float(data["price"])
        except (ValueError, TypeError):
            return jsonify({"error": "Price must be a number"}), 400
        if library.search_by_title(data["title"]):
            return jsonify({"error": "Book already exists"}), 409
        book = Book(data["title"], data["author"], price)
        library.add_book(book)
        return jsonify({"title": book.title, "author": book.author, "price": book.price}), 201

    @app.route("/library/books", methods=["GET"])
    def filter_books():
        author = request.args.get("author")
        max_price = request.args.get("max_price")
        books = library.books
        if author:
            books = library.get_books_by_author(author)
        if max_price:
            try:
                max_price_f = float(max_price)
                books = [b for b in books if b.price <= max_price_f]
            except ValueError:
                return jsonify({"error": "max_price must be a number"}), 400
        return jsonify([
            {"title": b.title, "author": b.author, "price": b.price}
            for b in books
        ])

    @app.route("/library/export/<fmt>", methods=["POST"])
    def export_catalogue(fmt):
        if fmt not in ("csv", "json"):
            return jsonify({"error": "Format must be 'csv' or 'json'"}), 400
        EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
        file_path = EXPORTS_DIR / f"catalogue.{fmt}"
        if fmt == "csv":
            file_manager.export_to_csv(str(file_path))
        else:
            file_manager.export_to_json(str(file_path))
        return jsonify({"message": f"Catalogue exported to {file_path.name}"})

    @app.route("/library/import/<fmt>", methods=["POST"])
    def import_catalogue(fmt):
        if fmt not in ("csv", "json"):
            return jsonify({"error": "Format must be 'csv' or 'json'"}), 400
        if "file" not in request.files:
            return jsonify({"error": "No file provided"}), 400
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No file selected"}), 400
        import tempfile
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=f".{fmt}")
        file.save(tmp.name)
        tmp.close()
        try:
            if fmt == "csv":
                file_manager.import_from_csv(tmp.name)
            else:
                file_manager.import_from_json(tmp.name)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        finally:
            Path(tmp.name).unlink(missing_ok=True)
        return jsonify({"message": f"Imported from {file.filename}", "total_books": len(library.books)})

    def get_sales_analysis():
        return CatalogueAnalysis(str(SALES_CSV))

    @app.route("/sales/revenue", methods=["GET"])
    @log_call
    def total_revenue():
        analysis = get_sales_analysis()
        return jsonify({"total_revenue": analysis.get_total_revenue()})

    @app.route("/sales/best-seller", methods=["GET"])
    @log_call
    def best_seller():
        analysis = get_sales_analysis()
        return jsonify({"best_seller": analysis.get_best_seller()})

    @app.route("/sales/revenue-by-genre", methods=["GET"])
    def revenue_by_genre():
        analysis = get_sales_analysis()
        return jsonify(analysis.get_revenue_by_genre())

    @app.route("/sales/charts/<name>", methods=["GET"])
    def get_chart(name):
        chart_path = CHARTS_DIR / name
        if not chart_path.exists():
            return jsonify({"error": f"Chart '{name}' not found"}), 404
        return send_file(str(chart_path), mimetype="image/png")

    return app
