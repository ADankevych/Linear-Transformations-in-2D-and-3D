import numpy as np
import matplotlib.pyplot as plt

# batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])

batman = np.array([
   [0, 0], [0, 0.75],
   [0, 0.75], [0.75, 0],
   [0.75, 0], [-0.75, 0],
   [0.75, 0.75], [0, -0.75]
   ])

plt.figure()

for i in range(0, len(batman)-1, 2):
    plt.quiver(batman[i][0], batman[i][1], batman[i+1][0], batman[i+1][1], angles='xy', scale_units='xy', scale=1, color='g')


plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True)

plt.show()