from db_utils import get_db_connection


def get_violations_per_camera():
    """
    Retrieves the number of violations per camera from the TrafficData table.
    Returns a list of tuples containing camera ID and the corresponding violation count.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Assuming the speed limit is 60
        query = """
        SELECT camera_id, COUNT(*) as violation_count
        FROM TrafficData
        WHERE speed > 60
        GROUP BY camera_id
        ORDER BY violation_count DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        violations_per_camera = []
        for row in results:
            violations_per_camera.append((row[0], row[1]))

        conn.close()
        return violations_per_camera
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_top_violating_vehicles():
    """
    Retrieves the top 10 violating vehicles from the TrafficData table.
    Prints the vehicle ID and the corresponding violation count.
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get top 10 violating vehicles
        query = """
        SELECT vehicle_id, COUNT(*) as violation_count
        FROM TrafficData
        WHERE speed > 60
        GROUP BY vehicle_id
        ORDER BY violation_count DESC
        LIMIT 10;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\nTop violating vehicles:")
        for row in results:
            print(f"Vehicle ID: {row[0]} - Violations: {row[1]}")

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    get_violations_per_camera()
    get_top_violating_vehicles()






