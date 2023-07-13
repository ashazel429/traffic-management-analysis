import matplotlib.pyplot as plt
from data_analysis import get_violations_per_camera

def plot_violations_per_camera():
    # Call get_violations_per_camera to retrieve the data
    data = get_violations_per_camera()
    if data:
        cameras = [item[0] for item in data]
        violations = [item[1] for item in data]

        plt.bar(cameras, violations)
        plt.xlabel('Camera ID')
        plt.ylabel('Violations')
        plt.title('Violations per Camera')
        plt.show()

    # Print the list of violations per camera
    print("\nViolations per camera:")
    for item in data:
        print(f"Camera ID: {item[0]} - Violations: {item[1]}")

if __name__ == "__main__":
    plot_violations_per_camera()




