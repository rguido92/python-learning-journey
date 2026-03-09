# Generar los test para el módulo file_manager.py, asegurando que se cubran los casos de exportación e importación tanto para CSV como para JSON, incluyendo la gestión de errores al intentar importar desde archivos inexistentes. Usar rutas con tmp.path para evitar problemas de permisos y limpieza de archivos después de las pruebas.
# los archivos exportados deben poder ser reimportados sin pérdida de datos


import pytest
import os
from module_01_fundamentals.project import library
from module_01_fundamentals.project.library import Library
from module_01_fundamentals.project.book import Book
from module_03_automation.project import file_manager
from module_03_automation.project.file_manager import FileManager


@pytest.fixture
def setup():
    library = Library("Test Library")
    book1 = Book("Book One", "Author A", 10.99)
    book2 = Book("Book Two", "Author B", 15.99)
    library.add_book(book1)
    library.add_book(book2)
    file_manager = FileManager(library)
    return library, file_manager


def test_export_to_csv(tmp_path, setup):
    library, file_manager = setup
    csv_file = tmp_path / "library.csv"
    file_manager.export_to_csv(str(csv_file))
    assert os.path.exists(csv_file)
    # Verificar que el archivo CSV se pueda reimportar sin pérdida de datos
    new_library = Library("New Library")
    new_file_manager = FileManager(new_library)
    new_file_manager.import_from_csv(str(csv_file))
    assert len(new_library.books) == len(library.books)
    for original, imported in zip(library.books, new_library.books):
        assert original.title == imported.title
        assert original.author == imported.author
        assert original.price == imported.price


def test_export_to_json(tmp_path, setup):
    library, file_manager = setup
    json_file = tmp_path / "library.json"
    file_manager.export_to_json(str(json_file))
    assert os.path.exists(json_file)
    # Verificar que el archivo JSON se pueda reimportar sin pérdida de datos
    new_library = Library("New Library")
    new_file_manager = FileManager(new_library)
    new_file_manager.import_from_json(str(json_file))
    assert len(new_library.books) == len(library.books)
    for original, imported in zip(library.books, new_library.books):
        assert original.title == imported.title
        assert original.author == imported.author
        assert original.price == imported.price


def test_import_from_nonexistent_csv(tmp_path, setup):
    library, file_manager = setup
    non_existent_file = tmp_path / "non_existent.csv"
    with pytest.raises(FileNotFoundError):
        file_manager.import_from_csv(str(non_existent_file))


def test_import_from_nonexistent_json(tmp_path, setup):
    library, file_manager = setup
    non_existent_file = tmp_path / "non_existent.json"
    with pytest.raises(FileNotFoundError):
        file_manager.import_from_json(str(non_existent_file))
