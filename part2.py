import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import zoom

batman = np.array([
    [0, 0],
    [1, 0.2],
    [0.4, 1],
    [0.5, 0.4],
    [0, 0.8],
    [-0.5, 0.4],
    [-0.4, 1],
    [-1, 0.2],
    [0, 0]
])

plt.figure()

rotate_matrix = np.rot90(batman, 2)
plt.plot(batman[:, 0], batman[:, 1], 'b')
plt.plot(rotate_matrix[:, 0], rotate_matrix[:, 1], 'r')

scaled_matrix = zoom(batman, [1.5, 1.5])
plt.plot(scaled_matrix[:, 0], scaled_matrix[:, 1], 'g')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True)

plt.show()
