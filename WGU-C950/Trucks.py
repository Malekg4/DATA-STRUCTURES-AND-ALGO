# Trucks.py

# Definition of the Trucks class
class Trucks:
    # Constructor to initialize truck attributes
    def __init__(self, load, packages, mileage, address, depart_time):
        # Setting constant values for truck attributes
        self.max_storage = 16                                   # Maximum storage capacity of the truck
        self.mph = 18                                           # Maximum speed of the truck in miles per hour

        # Assigning values for variable truck attributes
        self.load = load                                        # Current load of packages in the truck
        self.packages = packages                                # List of package IDs assigned to the truck
        self.mileage = mileage                                  # Total mileage covered by the truck
        self.address = address                                  # Current address of the truck
        self.depart_time = depart_time                          # Departure time of the truck
        self.time = depart_time                                 # Current time of the truck (initialized as the departure time)


