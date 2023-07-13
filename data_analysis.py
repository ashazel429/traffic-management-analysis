from db_utils import get_db_connection


def get_violations_per_camera():
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

    print("\nViolations per camera:")
    for row in results:
        print(f"Camera ID: {row[0]} - Violations: {row[1]}")

    conn.close()


def get_top_violating_vehicles():
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


if __name__ == "__main__":
    get_violations_per_camera()
    get_top_violating_vehicles()




