# Distances.py

# Importing the datetime module
import datetime

# Definition of the Distances class
class Distances:

    # Method to calculate the distance between two addresses
    def distance_difference(address1, address2, distance_file):
        # Fetching the distance between the given addresses from the distance file
        distance = distance_file[address1][address2]
        # Checking if the distance is empty (indicating reverse direction), then fetching from the other direction
        if distance == '':
            distance = distance_file[address2][address1]
        return float(distance)  # Returning the distance as a float value

    # Method to perform package deliveries for trucks
    def PackageDeliveries(trucks, Hash_Table, address_file, distance_file):
        # List to store packages to be delivered by the truck
        packagesToDeliver = []

        # Iterating through each package ID assigned to the truck
        for id in trucks.packages:
            # Retrieving package object from the hash table using its ID
            package = Hash_Table.search(id)
            # Adding the package to the list of packages to be delivered
            packagesToDeliver.append(package)

        # Looping until all packages are delivered
        while len(packagesToDeliver) > 0:
            next_Address = 2000  # Initializing the next address variable with a large value
            next_Package = None  # Initializing the next package variable as None

            # Iterating through each package to find the nearest one for delivery
            for package in packagesToDeliver:
                # Calculating the distance between the truck's current address and the package's address
                distance = Distances.distance_difference(package.getAddress(trucks.address, address_file), package.getAddress(package.address, address_file), distance_file)
                # Updating the nearest address and package if found
                if distance <= next_Address:
                    next_Address = distance
                    next_Package = package

            # Adding the ID of the next package to the truck's package list
            trucks.packages.append(next_Package.id)
            # Removing the delivered package from the list of packages to be delivered
            packagesToDeliver.remove(next_Package)

            # Updating the truck's mileage and address
            trucks.mileage = trucks.mileage + next_Address
            trucks.address = next_Package.address
            # Updating the truck's time based on the distance travelled
            trucks.time = trucks.time + datetime.timedelta(hours=next_Address / 18)
            # Updating the delivery time of the package
            next_Package.delivery_time = trucks.time
            # Setting the departure time of the package as the truck's departure time
            next_Package.departure_time = trucks.depart_time
