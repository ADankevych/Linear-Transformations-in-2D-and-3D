import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('image.png')

cv2.imshow('Original', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

scaled_image = cv2.resize(image, None, fx=5, fy=5)

cv2.imshow('Rotated', rotated_image)
cv2.imshow('Scaled', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
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

scaled_matrix = cv2.resize(batman, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
plt.plot(scaled_matrix[:, 0], scaled_matrix[:, 1], 'g')

flipped_matrix = np.flip(batman, axis=1)
plt.plot(flipped_matrix[:, 0], flipped_matrix[:, 1], 'y')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True)

plt.show()
"""
