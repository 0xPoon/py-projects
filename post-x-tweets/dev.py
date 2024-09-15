# (2) Conduct Transformation on data: make it so data is in a proper tabular format
import csv
import pandas as pd
import importlib
ExtractDataFromHTML = importlib.import_module("extract-cpi-data")

# Set global options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class TransformData:
    def __init__(self, csv):
        self.csv = csv

    def open_csv(self):
        with open(csv, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in data:
                print(', '.join(row))

