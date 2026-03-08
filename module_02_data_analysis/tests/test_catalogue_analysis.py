import pytest
import pandas as pd
from module_02_data_analysis.project.catalogue_analysis import CatalogueAnalysis

CSV_PATH = "module_02_data_analysis/data/sales.csv"


@pytest.fixture
def analisis():
    return CatalogueAnalysis(CSV_PATH)


def test_get_total_revenue(analisis):
    resultado = analisis.get_total_revenue()
    assert isinstance(resultado, (int, float))
    assert resultado > 0


def test_get_best_seller(analisis):
    resultado = analisis.get_best_seller()
    assert isinstance(resultado, str)
    assert resultado == "Atomic Habits"


def test_get_revenue_by_genre(analisis):
    resultado = analisis.get_revenue_by_genre()
    assert isinstance(resultado, dict)
    assert sum(resultado.values()) == analisis.get_total_revenue()


def test_get_top_authors(analisis):
    resultado = analisis.get_top_authors(3)
    assert isinstance(resultado, dict)
    assert len(resultado) == 3


def test_get_top_authors_with_different_n(analisis):
    resultado = analisis.get_top_authors(5)
    assert len(resultado) == 5
