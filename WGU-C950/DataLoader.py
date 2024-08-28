# DataLoader.py

# Importing the csv module
import csv

# Definition of the DataLoader class
class DataLoader:
    # Method to load data from a CSV file
    @staticmethod
    def load_data(file_name):
        # Opening the CSV file in a context manager
        with open(file_name) as file:
            # Reading the contents of the CSV file and converting it into a list of lists
            data = list(csv.reader(file))
        # Returning the loaded data
        return data
