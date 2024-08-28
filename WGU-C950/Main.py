# Main.py

# name: Malek Gaghman
# student id: 011396393

# Importing necessary modules and classes
import csv
import datetime

from Trucks import Trucks
from Packages import Packages
from HashTable import HashTable
from DataLoader import DataLoader
from Distances import Distances
from PackageLoader import PackageLoader

# Loading data from CSV files
package_file = DataLoader.load_data("packageCSV.csv")
address_file = DataLoader.load_data("addressCSV.csv")
distance_file = DataLoader.load_data("distanceCSV.csv")

# Creating Truck objects with specified routes and departure times
truck1 = Trucks(None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East", datetime.timedelta(hours=8))
truck2 = Trucks(None, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,"4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck3 = Trucks(None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

# Creating HashTable object
Hash_Table = HashTable()

# Loading package data into the hash table
PackageLoader.loadData("packageCSV.csv", Hash_Table)

# Calculating package deliveries for each truck
Distances.PackageDeliveries(truck1, Hash_Table, address_file, distance_file)
Distances.PackageDeliveries(truck2, Hash_Table, address_file, distance_file)

# Setting the departure time of truck3 to the minimum time among truck1 and truck2
truck3.depart_time = min(truck1.time, truck2.time)
Distances.PackageDeliveries(truck3, Hash_Table, address_file, distance_file)

class Main:
    # Printing menu options for the user
    print("=============================================================================")
    print("Please select one of the following options:")
    print("")
    print(" 1. Generate General Report   (enter: 'g')")
    print(" 2. Perform Package Query     (enter: 'p')")
    print(" 3. Exit                      (enter: 'q')")
    print("")
    print("=============================================================================")
    Customer_input = input()
    print("")

    # Generating general report if the user chooses option 'g'
    if Customer_input == 'g':
        user_input = input("Enter the time you would like to see the status of the packages (HH:MM:SS): ")
        print("")
        try:
            (h, m, s) = user_input.split(":")
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        except ValueError:
            print("Error: Invalid Format!!!")
            exit()

        # Updating and printing status of each package
        for id in range(1, 41):
            package = Hash_Table.search(id)
            package.update_status(time)

            # Correcting address for package #9 at 10:20 a.m.
            if id == 9 and time >= datetime.timedelta(hours=10, minutes=20):
                package.address = "410 S State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zip = "84111"

            # Determine which truck delivered the package
            delivering_truck = None
            if id in truck1.packages:
                delivering_truck = "Truck 1"
            elif id in truck2.packages:
                delivering_truck = "Truck 2"
            elif id in truck3.packages:
                delivering_truck = "Truck 3"

            # Print package status along with delivering truck information
            print(f"{str(package)} , {delivering_truck}")

        # Printing mileage information for each truck and total mileage
        print("")
        print("Truck 1's mileage: {:.1f}".format(truck1.mileage))
        print("Truck 2's mileage: ", truck2.mileage)
        print("Truck 3's mileage: ", truck3.mileage)
        print("")
        print("Total mileage: ", (truck1.mileage + truck2.mileage + truck3.mileage))

    # Performing package query if the user chooses option 'p'
    elif Customer_input == 'p':
        user_input = input("Enter the time you would like to see the status of the package (HH:MM:SS): ")
        print("")
        try:
            (h, m, s) = user_input.split(":")
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        except ValueError:
            print("")
            print("Error: Invalid Format!!!")
            exit()

        # Searching for package by ID and updating its status
        package_ID = input("Enter package ID: ")
        package = Hash_Table.search(int(package_ID))
        package.update_status(time)

        # Correcting address for package #9 at 10:20 a.m.
        if int(package_ID) == 9 and time >= datetime.timedelta(hours=10, minutes=20):
            package.address = "410 S State St"
            package.city = "Salt Lake City"
            package.state = "UT"
            package.zip = "84111"

        # Determine which truck delivered the package
        delivering_truck = None
        if int(package_ID) in truck1.packages:
            delivering_truck = "Truck 1"
        elif int(package_ID) in truck2.packages:
            delivering_truck = "Truck 2"
        elif int(package_ID) in truck3.packages:
            delivering_truck = "Truck 3"

        # Print package status along with delivering truck information
        print("")
        print(f"{str(package)} , {delivering_truck}")

    # Exiting the program if the user chooses option 'q'
    elif Customer_input == 'q':
        print("Exiting...")
        exit()
