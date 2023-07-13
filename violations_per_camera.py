import matplotlib.pyplot as plt


def plot_violations_per_camera():
    data = get_violations_per_camera()
    cameras = [item[0] for item in data]
    violations = [item[1] for item in data]

    plt.bar(cameras, violations)
    plt.xlabel('Camera ID')
    plt.ylabel('Violations')
    plt.title('Violations per Camera')
    plt.show()
