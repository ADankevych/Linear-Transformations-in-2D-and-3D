import numpy as np
import matplotlib.pyplot as plt


def rotate(object, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return np.dot(object, rotation_matrix)


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

rotate_star = rotate(star, 180)
plt.plot(rotate_star[:, 0], rotate_star[:, 1], 'b')

rotate_batman = rotate(batman, 90)
plt.plot(rotate_batman[:, 0], rotate_batman[:, 1], 'g')

plt.show()
