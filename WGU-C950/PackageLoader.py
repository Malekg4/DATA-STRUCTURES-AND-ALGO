# PackageLoader.py

# Importing necessary modules and classes
import csv
from Packages import Packages

# Definition of PackageLoader class
class PackageLoader:

    # Method to load package data into the hash table
    def loadData(file_name, Hash_Table):
        # Opening the package file
        with open(file_name) as package_file:
            # Reading data from the CSV file
            p_data = csv.reader(package_file)
            # Iterating through each row of the CSV file
            for x in p_data:
                # Extracting data from each row
                id = int(x[0])
                address = x[1]
                city = x[2]
                state = x[3]
                zip = x[4]
                deadline = x[5]
                weight = x[6]
                status = "At Hub"  # Default status for new packages

                # Creating a Packages object with extracted data
                p_obj = Packages(id, address, city, state, zip, deadline, weight, status)

                # Inserting the Packages object into the hash table
                Hash_Table.insert(id, p_obj)
