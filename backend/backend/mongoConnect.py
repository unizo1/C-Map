from pymongo import MongoClient
from pymongo.errors import PyMongoError

# MongoDB connection details
username = "ljohns76"  # Replace with your MongoDB username
password = "GMUHackathon"   # Replace with your MongoDB password
host = "localhost"          # Use your Docker container's IP address if necessary
port = 27017                # Default MongoDB port
database_name = "event_data"  # Name of your database
collection_name = "events"     # Name of the collection you want to use

# Create a MongoDB connection string
connection_string = f"mongodb://{username}:{password}@{host}:{port}/admin"

try:
    # Create a MongoClient
    client = MongoClient(connection_string)

    # Access the event_data database and the specified collection
    db = client[database_name]
    collection = db[collection_name]

    # Sample data to insert
    data_to_insert = {
        "event_name": "Sample Event",
        "date": "2024-10-12",
        "location": "Sample Location",
        "description": "This is a sample event description."
    }

    # Insert the data into the collection
    result = collection.insert_one(data_to_insert)

    print(f"Data inserted successfully with document ID: {result.inserted_id}")

except PyMongoError as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection if it was established
    if 'client' in locals():
        client.close()
