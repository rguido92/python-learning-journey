import pandas as pd


class CatalogueAnalysis:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df["revenue"] = self.df["price"] * self.df["units_sold"]
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["month"] = self.df["date"].dt.to_period("M")

    def get_total_revenue(self):
        return self.df["revenue"].sum()

    def get_best_seller(self):
        return self.df.loc[self.df["units_sold"].idxmax(), "title"]

    def get_revenue_by_genre(self):
        return self.df.groupby("genre")["revenue"].sum().to_dict()

    def get_top_authors(self, n):
        return self.df.groupby("author")["revenue"].sum().nlargest(n).to_dict()

    # dt.to_period("M") convierte 2024-01-15 en 2024-01. Así todas las ventas del mismo mes quedan agrupadas juntas.
    def get_revenue_by_month(self):
        return self.df.groupby("month")["revenue"].sum().to_dict()
