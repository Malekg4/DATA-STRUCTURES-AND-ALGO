# Packages.py

# Definition of the Packages class
class Packages:
    # Constructor to initialize package attributes
    def __init__(self, id, address, city, state, zip, deadline, weight, status):
        # Assigning values to package attributes
        self.id = id                                                # Package ID
        self.address = address                                      # Delivery address
        self.city = city                                            # City
        self.state = state                                          # State
        self.zip = zip                                              # Zip code
        self.deadline = deadline                                    # Delivery deadline
        self.weight = weight                                        # Package weight
        self.status = status                                        # Delivery status
        self.departure_time = None                                  # Departure time of the package (initially None)
        self.delivery_time = None                                   # Delivery time of the package (initially None)

    # Method to update the status of the package based on the current time
    def update_status(self, time):
        if self.delivery_time < time:
            self.status = "Delivered"
        elif self.departure_time > time:
            self.status = "En route"
        else:
            self.status = "At the Hub"

    # Static method to get the address index from the address CSV
    @staticmethod
    def getAddress(address, addressCSV):
        for row in addressCSV:
            if address in row[2]:                                   # Assuming the address is found in the third column of the addressCSV
                return int(row[0])                                  # Returning the address index
        return None                                                 # Returning None if the address is not found

    # Method to represent the package object as a string
    def __str__(self):
        return ("%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip, self.deadline, self.weight, self.delivery_time, self.status))
