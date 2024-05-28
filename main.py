import numpy as np
import matplotlib.pyplot as plt

batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
star = np.array([[-0.5, 0], [0, 1.5], [0.5, 0], [-0.5, 1], [0.5, 1], [-0.5, 0]])

plt.figure()

plt.plot(batman[:, 0], batman[:, 1], 'g')
plt.plot(star[:, 0], star[:, 1], 'b')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True)

plt.show()
