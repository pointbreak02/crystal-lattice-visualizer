import numpy as np
import matplotlib.pyplot as plt

def generate_lattice(rows=10, cols=10, spacing=1.0, lattice_type="square"):
    x_coords, y_coords = [], []

    for i in range(rows):
        for j in range(cols):
            x = j * spacing
            y = i * spacing

            if lattice_type == "hex":
                if i % 2 == 0:
                    x += spacing / 2
                y *= np.sqrt(3) / 2

            x_coords.append(x)
            y_coords.append(y)

    return np.array(x_coords), np.array(y_coords)

def plot_lattice(x, y, lattice_type="square"):
    plt.figure(figsize=(6,6))
    plt.scatter(x, y, c='blue', s=100, edgecolors='black')
    plt.title(f"{lattice_type.capitalize()} Lattice Structure")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x, y = generate_lattice(lattice_type="square")
    plot_lattice(x, y, lattice_type="square")
