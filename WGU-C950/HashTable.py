# HashTable.py

# Definition of the HashTable class
class HashTable:
    # Constructor to initialize the hash table with an initial capacity
    def __init__(self, initial_capacity=40):
        # Creating an empty data structure to store buckets
        self.data_structure = []
        # Creating 'initial_capacity' number of buckets in the data structure
        for i in range(initial_capacity):
            self.data_structure.append([])

    # Method to insert key-value pair into the hash table
    def insert(self, key, value):
        # Calculating the bucket index using the hash of the key
        bucket = hash(key) % len(self.data_structure)
        # Accessing the bucket corresponding to the calculated index
        bucket_content = self.data_structure[bucket]

        # Iterating through each entry in the bucket
        for entry in bucket_content:
            # Checking if the key already exists in the bucket
            if entry[0] == key:
                # Updating the value if the key exists
                entry[1] = value
                return True

        # Appending the key-value pair to the bucket if the key doesn't exist
        bucket_content.append([key, value])
        return True

    # Method to search for a value by key in the hash table
    def search(self, key):
        # Calculating the bucket index using the hash of the key
        bucket = hash(key) % len(self.data_structure)
        # Accessing the bucket corresponding to the calculated index
        bucket_content = self.data_structure[bucket]

        # Iterating through each entry in the bucket
        for entry in bucket_content:
            # Checking if the key matches the searched key
            if entry[0] == key:
                # Returning the corresponding value if the key is found
                return entry[1]
        # Returning None if the key is not found
        return None

    # Method to remove a key-value pair from the hash table
    def remove(self, key):
        # Calculating the bucket index using the hash of the key
        bucket = hash(key) % len(self.data_structure)
        # Accessing the bucket corresponding to the calculated index
        bucket_content = self.data_structure[bucket]

        # Iterating through each entry in the bucket
        for entry in bucket_content:
            # Checking if the key matches the searched key
            if entry[0] == key:
                # Removing the entry from the bucket if the key is found
                bucket_content.remove(entry)
                return True
        # Returning False if the key is not found
        return False
