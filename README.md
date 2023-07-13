Traffic Management Analysis
This project leverages the power of Python and SQLite to analyze traffic violations in a simulated city environment. The project synthesizes data for traffic cameras, vehicles, and their violations and extracts meaningful insights from them.

Scripts:
1. populate_db.py
This script acts as a data generator. It synthesizes and populates three tables - Cameras, Vehicles, and TrafficData with synthetic data representing traffic cameras, vehicles, and traffic violations respectively.

2. db_utils.py
A utility script that serves the purpose of establishing a connection to our SQLite database. It's the bridge between our Python scripts and the database.

3. data_analysis.py
Our main analysis script. It contains functions to analyze the traffic violation data. It provides insights like the number of violations per camera and the top violating vehicles.

4. violations_per_camera.py
A visualization script. It uses the matplotlib library to generate a bar plot of the number of violations per camera. It visualizes the output of the get_violations_per_camera function from data_analysis.py.

Instructions:
To extract insights from the traffic data, follow these simple steps:

1. Generate and insert data into the SQLite database
python populate_db.py

2. Analyze the data and print insights to the console
python data_analysis.py

3. Generate a visual plot of the number of violations per camera
python violations_per_camera.py

Dependencies
The project runs on Python 3.7 or later and requires the following Python libraries:
SQLite
Faker
Matplotlib

These dependencies can be installed using pip:
pip install sqlite3 faker matplotlib
