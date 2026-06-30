from module_02_data_analysis.project.catalogue_analysis import CatalogueAnalysis
from module_02_data_analysis.project.visualizer import SalesVisualizer

# Carga los datos reales
analysis = CatalogueAnalysis("module_02_data_analysis/data/sales.csv")

# Crea el visualizador
visualizer = SalesVisualizer(analysis)

# Prueba el método
# visualizer.sales_over_time()
