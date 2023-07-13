import sqlite3
import random
from faker import Faker

fake = Faker()

conn = sqlite3.connect('traffic_management_db.db')
cursor = conn.cursor()

# Delete existing data from Cameras
cursor.execute("DELETE FROM Cameras")

# Generate data for Cameras
for i in range(10):
    query = f"""
    INSERT INTO Cameras (camera_id, location, installation_date)
    VALUES ({i}, "{fake.street_address()}", "{fake.date()}");
    """
    cursor.execute(query)

# Delete existing data from Vehicles
cursor.execute("DELETE FROM Vehicles")

# Generate data for Vehicles
for i in range(100):
    query = f"""
    INSERT INTO Vehicles (vehicle_id, registration_number, owner)
    VALUES ({i}, "{fake.license_plate()}", "{fake.name()}");
    """
    cursor.execute(query)

# Delete existing data from TrafficData
cursor.execute("DELETE FROM TrafficData")

# Generate data for TrafficData
for i in range(1000):
    query = f"""
    INSERT INTO TrafficData (timestamp, camera_id, vehicle_id, speed)
    VALUES ("{fake.date_time_this_year()}", {random.randint(0, 9)}, {random.randint(0, 99)}, {random.randint(30, 120)});
    """
    cursor.execute(query)

# Commit the changes and close the connection
conn.commit()
conn.close()

