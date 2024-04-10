import numpy as np
import matplotlib.pyplot as plt

import main

# Define the function Z(x, y)
def z_function(x, y):
    z = list()
    for xrow, yrow in zip(x, y):
        z.append(list())
        for xx, yy in zip(xrow, yrow):
            z[-1].append(main.Z((xx, yy)))
    return z

# Generate x and y data
x = np.linspace(-1, 3, 100)
y = np.linspace(-0.5, 3.5, 100)
x, y = np.meshgrid(x, y)
z = z_function(x, y)

# Create a new figure
fig, ax = plt.subplots(figsize=(6, 6))

# Plot surface isolines
contour = ax.contour(x, y, z, cmap='viridis')

# Add points from gradient_steps with arrows connecting consecutive points
# gradient_steps = [
#     (0.0000, 0.5000),
#     (0.6794, 0.8397),
#     (0.9485, 0.9743),
#     (0.9931, 0.9965)]

coordinate_steps = [
    (0.0000, 0.5000),
    (0.6794, 0.5000),
    (0.9354, 0.5000),
    (0.9881, 0.5000),
    (0.9881, 0.9082),
    (0.9881, 0.9875),
    (0.9881, 0.9983),
    (0.9984, 0.9983)]

for i in range(len(coordinate_steps) - 1):
    ax.plot(*coordinate_steps[i], 'ro')  # Plot point
    ax.annotate('', xy=coordinate_steps[i + 1], xytext=coordinate_steps[i], arrowprops=dict(facecolor='red', arrowstyle='->'))

# Set x and y axis limits
ax.set_xlim(-1, 3)
ax.set_ylim(-0.5, 3.5)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# plt.savefig("img/gradient_steps_isolines.png")
plt.savefig("img/coordinate_steps_isolines.png")