import pytest
from unittest.mock import MagicMock, patch
from module_02_data_analysis.project.visualizer import SalesVisualizer


# Mockear las funciones de pyplot para que no se ejecuten de verdad
@patch("module_02_data_analysis.project.visualizer.plt")
def test_plot_revenue_by_genre_calls_matplotlib(mock_plt):
    # 1. Simular CatalogueAnalysis y sus datos
    mock_catalogue = MagicMock()
    mock_catalogue.get_revenue_by_genre.return_value = {
        "Fiction": 1000,
        "Programming": 1500,
    }
    # Decirle al mock que devuelve subplots()
    mock_fig = MagicMock()
    mock_ax = MagicMock()
    mock_plt.subplots.return_value = (mock_fig, mock_ax)
    visualizer = SalesVisualizer(mock_catalogue)
    # Ejecutar el metodo
    visualizer.plot_revenue_by_genre()
    # Assert : Verificar que se llamó a las funciones críticas de pyplot
    # Comprobar que se creó la figura
    mock_plt.subplots.assert_called_once()

    # Comprobar que se guardó el archivo con el nombre correcto
    # Usar ANY o verificar el final de la ruta porque es un objeto Path
    mock_plt.savefig.assert_called_once()
    args, _ = mock_plt.savefig.call_args
    assert "revenue_by_genre.png" in str(args[0])

    # comprobar que se llamo a show
    mock_plt.show.assert_called_once()


@patch("module_02_data_analysis.project.visualizer.plt")
def test_plot_top_author_calls_matplotlib(mock_plt):
    mock_catalogue = MagicMock()
    mock_catalogue.get_top_authors.return_value = {"CLRS": 75, "Grant Fritchey": 84}
    mock_fig = MagicMock()
    mock_ax = MagicMock()
    mock_plt.subplots.return_value = (mock_fig, mock_ax)
    visualizer = SalesVisualizer(mock_catalogue)
    visualizer.plot_top_authors(3)
    mock_plt.subplots.assert_called_once()
    mock_plt.savefig.assert_called_once()
    args, _ = mock_plt.savefig.call_args
    assert "revenue_top_authors.png" in str(args[0])
    mock_plt.show.assert_called_once()


@patch("module_02_data_analysis.project.visualizer.plt")
def test_plot_sales_over_time_calls_matplotlib(mock_plt):
    mock_catalogue = MagicMock()
    mock_catalogue.get_revenue_by_month.return_value = {
        "2024-01": 1000,
        "2024-02": 1500,
    }
    mock_fig = MagicMock()
    mock_ax = MagicMock()
    mock_plt.subplots.return_value = (mock_fig, mock_ax)
    visualizer = SalesVisualizer(mock_catalogue)
    visualizer.plot_sales_over_time()
    mock_plt.subplots.assert_called_once()
    mock_plt.savefig.assert_called_once()
    args, _ = mock_plt.savefig.call_args
    assert "revenue_over_time" in str(args[0])
    mock_plt.show.assert_called_once()
