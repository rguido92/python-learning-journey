import matplotlib.pyplot as plt
from pathlib import Path
from module_02_data_analysis.project.catalogue_analysis import CatalogueAnalysis


class SalesVisualizer:
    def __init__(self, catalogue_analysis):
        self.catalogue_analysis = catalogue_analysis
        self.charts_dir = Path("module_02_data_analysis/data/charts")
        self.charts_dir.mkdir(
            parents=True, exist_ok=True
        )  # Crea la carpeta si no existe

    # Grafico de barras con ingresos por genero
    def plot_revenue_by_genre(self):
        # Obtencion de datos
        data = self.catalogue_analysis.get_revenue_by_genre()
        # Creacion el gráfico
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(data.keys(), data.values())
        # Titulo y etiquetas
        ax.set_title("Grafico ")
        ax.set_xlabel("Genero")
        ax.set_ylabel("Ingresos (€)")
        # Guardar y mostrar
        plt.tight_layout()
        plt.savefig(self.charts_dir / "revenue_by_genre.png")
        plt.show()

    def plot_top_authors(self, n):
        data = self.catalogue_analysis.get_top_authors(n)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(list(data.keys()), list(data.values()))
        ax.set_title("Grafico top autores")
        ax.set_xlabel("Ingresos (€) ")
        ax.set_ylabel("Autor")
        plt.tight_layout()
        plt.savefig(self.charts_dir / "revenue_top_authors.png")
        plt.show()

    # línea con ax.plot(), agrupa el CSV por mes antes de graficar
    def plot_sales_over_time(self):
        data = self.catalogue_analysis.get_revenue_by_month()
        _, ax = plt.subplots(figsize=(10, 6))
        ax.plot([str(k) for k in data.keys()], list(data.values()))
        ax.set_title("Evolucion de ingresos por mes")
        ax.set_xlabel("Mes")
        ax.set_ylabel("Ingresos (€)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(self.charts_dir / "revenue_over_time.png")
        plt.show()
