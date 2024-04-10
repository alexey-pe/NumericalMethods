import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle

import main

vertices = main.q

# Define the range for x and y axes
x_range = (-2, 5)
y_range = (-1, 4)

# Create a new figure
fig, ax = plt.subplots(figsize=(8, 6))

# Plot x and y axes
ax.axhline(0, color='black',linewidth=1)
ax.axvline(0, color='black',linewidth=1)

# Set x and y axis limits
# ax.set_xlim(x_range)
ax.set_ylim(y_range)

# Set equal scale along the X and Y axes
ax.axis('equal')

# Set ticks and labels
ax.set_xticks(range(x_range[0], x_range[1]+1))
ax.set_yticks(range(y_range[0], y_range[1]+1))

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Set grid
ax.grid(True)

# Title
# plt.title('Coordinate System with Triangle')

# Plot the triangle
triangle = Polygon(vertices, closed=True, fill=None, edgecolor='#416BA9', linewidth=4)
ax.add_patch(triangle)

# Plot the inscribed circle
circle = Circle((1.0, 1.0), 1.0, fill=None, edgecolor='#416BA9', linewidth=2)
ax.add_patch(circle)

center = Circle((1.0, 1.0), 0.02, fill='black', edgecolor='black', linewidth=3)
ax.add_patch(center)

# Mark the center of the circle with a label
ax.text(1.15, 1.15, 'O(1, 1)', color='black', ha='left', va='bottom')

p0 = Circle((0, 0.5), 0.02, fill='black', edgecolor='black', linewidth=3)
ax.add_patch(p0)

# Mark p0 of the circle with a label
ax.text(0.15, 0.55, 'p0(0, 0.5)', color='black', ha='left', va='bottom')

# Add dimension line and label
# dimension_x = main.q[1][0] - main.q[0][0]
# dimension_y = 0.3  # Adjust the distance of the dimension line from the triangle
# dimension_label = r'$2 \times \sqrt{3}$'
#
# ax.plot([main.q[0][0], main.q[1][0]], [-dimension_y, -dimension_y], color='black')
# ax.text((main.q[0][0] + main.q[1][0]) / 2, -2 * dimension_y, dimension_label, color='black', ha='center')

# Show plot
# plt.show()
plt.savefig("img/triangle.png")