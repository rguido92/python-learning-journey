import sys
from pathlib import Path

import click

from module_01_fundamentals.project.book import Book
from module_01_fundamentals.project.library import Library
from module_03_automation.project.file_manager import FileManager
from module_04_web.project.app import create_app

BASE_DIR = Path(__file__).resolve().parent
EXPORTS_DIR = BASE_DIR / "module_04_web" / "exports"


@click.group()
def main():
    """Python Learning Journey - Library Management System."""


@main.command()
@click.option("--port", default=5000, help="Port to run the server on")
@click.option("--debug", is_flag=True, help="Run in debug mode")
def serve(port, debug):
    """Start the Flask web server."""
    app = create_app()
    click.echo(f"Starting server on http://127.0.0.1:{port}")
    app.run(port=port, debug=debug)


@main.command()
@click.option("--coverage", is_flag=True, help="Run with coverage report")
def test(coverage):
    """Run the test suite."""
    import subprocess

    cmd = [sys.executable, "-m", "pytest"]
    if coverage:
        cmd.extend(["--cov=.", "--cov-report=term-missing"])
    result = subprocess.run(cmd, cwd=str(BASE_DIR))
    sys.exit(result.returncode)


@main.group()
def export():
    """Export library catalogue."""


@export.command()
@click.argument("output", default=None, required=False)
def csv(output):
    """Export catalogue to CSV."""
    library = Library("Export")
    file_manager = FileManager(library)
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    file_path = Path(output) if output else EXPORTS_DIR / "catalogue.csv"
    file_manager.export_to_csv(str(file_path))
    click.echo(f"Exported to {file_path}")


@export.command()
@click.argument("output", default=None, required=False)
def json(output):
    """Export catalogue to JSON."""
    library = Library("Export")
    file_manager = FileManager(library)
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    file_path = Path(output) if output else EXPORTS_DIR / "catalogue.json"
    file_manager.export_to_json(str(file_path))
    click.echo(f"Exported to {file_path}")


@main.command()
@click.argument("title")
@click.argument("author")
@click.argument("price", type=float)
def add(title, author, price):
    """Add a book to the library (in-memory)."""
    library = Library("CLI Library")
    book = Book(title, author, price)
    library.add_book(book)
    click.echo(f"Added: {book}")


@main.command()
@click.option("--name", default="Library CLI", help="Library name")
def books(name):
    """List all books in the in-memory library."""
    library = Library(name)
    if not library.books:
        click.echo("No books in the library. Use 'plj add' first.")
        return
    for book in library.books:
        click.echo(f"  - {book}")


@main.command()
def sales():
    """Show sales summary from the CSV dataset."""
    from module_02_data_analysis.project.catalogue_analysis import (
        CatalogueAnalysis,
    )

    csv_path = BASE_DIR / "module_02_data_analysis" / "data" / "sales.csv"
    if not csv_path.exists():
        click.echo("Sales CSV not found.", err=True)
        sys.exit(1)
    analysis = CatalogueAnalysis(str(csv_path))
    click.echo(f"Total revenue: ${analysis.get_total_revenue():.2f}")
    click.echo(f"Best seller: {analysis.get_best_seller()}")
    click.echo("Revenue by genre:")
    for genre, rev in analysis.get_revenue_by_genre().items():
        click.echo(f"  - {genre}: ${rev:.2f}")


if __name__ == "__main__":
    main()
