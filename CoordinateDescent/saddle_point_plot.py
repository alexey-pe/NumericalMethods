import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def Z(x, y):
    return -(x - 1) ** 2 + (y - 1) ** 2

# Generate x and y data
x = np.linspace(-1, 4, 100)
y = np.linspace(-0.5, 3.5, 100)
x, y = np.meshgrid(x, y)
z = Z(x, y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('z(x, y) = -(x - 1)^2 + (y - 1)^2')

# Show plot
# plt.show()
plt.savefig("img/saddle_point.png")