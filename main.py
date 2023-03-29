import numpy as np
import matplotlib.pyplot as plt

def translation(x, y, tx, ty):
    """
    Translates a 2D point by (tx, ty)
    """
    M = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    point = np.array([x, y, 1])
    return np.dot(M, point)[:2]

# Define original points
points = np.array([[0, 0],
                   [1, 0],
                   [1, 1],
                   [0, 1]])

# Define translation vector
tx, ty = 1, 2

# Apply translation to each point
translated_points = [translation(x, y, tx, ty) for x, y in points]

# Plot original and translated points
plt.plot(points[:, 0], points[:, 1], 'bo-', label='Original')
plt.plot(translated_points[:, 0], translated_points[:, 1], 'ro-', label='Translated')
plt.legend()
plt.show()