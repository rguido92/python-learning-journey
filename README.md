# Python Learning Journey

A professional Python learning project built alongside the **Microsoft Python Development Professional Certificate** (Coursera). Each module adds real functionality to a bookstore management system, with automated testing from day one.

---

## Project Concept

Rather than isolated exercises, every module contributes to a single coherent system: a **library management application**. By the end of the certificate, this repository will be a complete, deployable project, not just a collection of snippets.

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Python Fundamentals | Complete |
| 02 | Data Analysis and Visualization | In progress |
| 03 | Automation and Scripting | Pending |
| 04 | Web Development with Python | Pending |
| 05 | Advanced Python Techniques | Pending |
| 06 | Project Development and Career | Pending |

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

Current status: **20 tests passing**

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

### Module 02 - Data Analysis (in progress)
Sales and catalogue analysis using pandas and Matplotlib:
- Dataset loading and cleaning
- Exploratory data analysis
- Sales visualizations

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
