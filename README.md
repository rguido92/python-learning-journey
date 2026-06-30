# Python Learning Journey

A professional Python learning project built alongside the **Microsoft Python Development Professional Certificate** (Coursera). Each module adds real functionality to a bookstore management system, with automated testing from day one.

---

## Project Concept

Rather than isolated exercises, every module contributes to a single coherent system: a **library management application**. By the end of the certificate, this repository will be a complete, deployable project, not just a collection of snippets.

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Python Fundamentals | Complete |
| 02 | Data Analysis and Visualization | Complete |
| 03 | Automation and Scripting | Complete |
| 04 | Web Development with Python | Complete |
| 05 | Advanced Python Techniques | Complete |
| 06 | Project Development and Career | Complete |

---

## Project Structure

```
python-learning-journey/
|
+-- README.md
+-- requirements.txt
+-- pytest.ini
|
+-- module_01_fundamentals/
|   +-- project/
|   |   +-- book.py          # Book entity
|   |   +-- library.py       # Library management
|   |   +-- user.py          # User and shopping cart
|   +-- tests/
|       +-- test_book.py
|       +-- test_library.py
|       +-- test_user.py
|
+-- module_02_data_analysis/
|   +-- data/                # CSV datasets
|   +-- project/             # Analysis and visualization modules
|   +-- tests/
|
+-- .venv/                   # Virtual environment (not tracked by Git)
```

---

## Setup

**Requirements:** Python 3.10+, Git

```bash
# Clone the repository
git clone https://github.com/rguido92/python-learning-journey.git
cd python-learning-journey

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scriptsctivate

# macOS / Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

```bash
# Run all tests
pytest

# Run a specific module
pytest module_01_fundamentals/

# Run with coverage report
pytest --cov=. --cov-report=term-missing
```

Current status: **81 tests passing — all modules complete**

---

## Dependencies

| Package | Purpose |
|---------|---------|
| pytest | Testing framework |
| pytest-cov | Test coverage reports |
| pandas | Data manipulation and analysis |
| matplotlib | Data visualization |

---

## Module Highlights

### Module 01 - Python Fundamentals
Core domain classes for the bookstore system:
- `Book` - title, author, price, discount logic
- `Library` - collection management, search, filtering
- `User` - shopping cart, total calculation

### Module 02 - Data Analysis
Sales and catalogue analysis using pandas and Matplotlib:
- Dataset loading and cleaning
- Exploratory data analysis
- Sales visualizations

### Module 03 - Automation
File management and data serialization:
- CSV and JSON export/import
- Error handling and directory creation

### Module 04 - Web Development
REST API with Flask integrating all previous modules:
- Book CRUD endpoints
- Library search and filter
- Catalogue export/import via API
- Sales data and chart endpoints

### Module 05 - Advanced Python Techniques
Advanced Python concepts applied to the bookstore system:
- **Decorators**: `@log_call`, `@measure_time`, `@retry` applied to Flask routes, FileManager, and CatalogueAnalysis
- **Generators**: `paginate_books` for paginated book listings, `chunked_import` and `stream_csv_rows` for efficient data processing
- **Context Managers**: `Timer` for measuring execution time, `ManagedFile` for safe file handling, `ChangeDirectory` for temporary directory changes

### Module 06 - Project Development and Career
Production-ready project packaging and tooling:
- **`pyproject.toml`**: Package configuration with entry point (`plj` CLI command)
- **`cli.py`**: Click-based CLI (`serve`, `test`, `export`, `sales`, `add`, `books`)
- **`Dockerfile`**: Containerized Flask API for deployment
- **GitHub Actions CI**: Automated test runner across Python 3.10-3.12
- **`Makefile`**: Convenience commands (`test`, `serve`, `lint`, `clean`)

---

## Commit Convention

| Prefix | Usage |
|--------|-------|
| feat: | New project functionality |
| exercise: | Completed exercise |
| test: | New or updated tests |
| docs: | Documentation updates |
| chore: | Configuration and setup |

---

## Author

**Rodrigo** - learning Python through real project development.  
Microsoft Python Development Professional Certificate - Coursera - 2025
