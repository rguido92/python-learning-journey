import pandas as pd


class CatalogueAnalysis:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df["revenue"] = self.df["price"] * self.df["units_sold"]

    def get_total_revenue(self):
        return self.df["revenue"].sum()

    def get_best_seller(self):
        return self.df.loc[self.df["units_sold"].idxmax(), "title"]

    def get_revenue_by_genre(self):
        return self.df.groupby("genre")["revenue"].sum()

    def get_top_authors(self, n):
        return self.df.groupby("author")["revenue"].sum().nlargest(n)
