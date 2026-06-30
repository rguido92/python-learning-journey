import pandas as pd
from module_05_advanced.project.decorators import log_call


class CatalogueAnalysis:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df["revenue"] = self.df["price"] * self.df["units_sold"]
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["month"] = self.df["date"].dt.to_period("M")

    @log_call
    def get_total_revenue(self):
        return self.df["revenue"].sum()

    @log_call
    def get_best_seller(self):
        return self.df.loc[self.df["units_sold"].idxmax(), "title"]

    @log_call
    def get_revenue_by_genre(self):
        return self.df.groupby("genre")["revenue"].sum().to_dict()

    @log_call
    def get_top_authors(self, n):
        return self.df.groupby("author")["revenue"].sum().nlargest(n).to_dict()

    def get_revenue_by_month(self):
        return self.df.groupby("month")["revenue"].sum().to_dict()
