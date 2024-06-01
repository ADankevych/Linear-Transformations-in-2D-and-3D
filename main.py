import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def rotate(object, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([
                                [np.cos(angle), -np.sin(angle)],
                                [np.sin(angle),  np.cos(angle)]
                                ])

    print(np.dot(object, rotation_matrix))

    return np.dot(object, rotation_matrix)


def scale(object, coefficient):
    scale_matrix = np.array([
                             [coefficient, 0],
                             [0, coefficient]
                             ])

    print(np.dot(object, scale_matrix))

    return np.dot(object, scale_matrix)


def reflect(object, mirror_axis):
    if mirror_axis == "x":
        reflect_object = np.array([
                                   [1,  0],
                                   [0, -1]
                                   ])
    else:
        reflect_object = np.array([
                                   [-1, 0],
                                   [0,  1]
                                   ])

    print(np.dot(object, reflect_object))

    return np.dot(object, reflect_object)


def tilt(object, angle, axis):
    angle = np.radians(angle)
    if axis == "x":
        tilt_matrix = np.array([
                                [1, np.tan(angle)],
                                [0, 1]
                                ])
    else:
        tilt_matrix = np.array([
                                [1, 0],
                                [np.tan(angle), 1]
                                ])

    print(np.dot(object, tilt_matrix))

    return np.dot(object, tilt_matrix)


def universal(object, rotate_angle, scale_coefficient, reflect_axis, tilt_angle, tilt_axis):
    object = rotate(object, rotate_angle)
    object = scale(object, scale_coefficient)
    object = reflect(object, reflect_axis)
    object = tilt(object, tilt_angle, tilt_axis)

    print(object)

    return object


def rotate3d(object, angle, axis):
    angle = np.radians(angle)
    if axis == "x":
        rotation_matrix = np.array([
                                    [1, 0, 0],
                                    [0, np.cos(angle), -np.sin(angle)],
                                    [0, np.sin(angle),  np.cos(angle)]
                                    ])
    elif axis == "y":
        rotation_matrix = np.array([
                                    [np.cos(angle), 0, np.sin(angle)],
                                    [0, 1, 0],
                                    [-np.sin(angle), 0, np.cos(angle)]
                                    ])
    else:
        rotation_matrix = np.array([
                                    [np.cos(angle), -np.sin(angle), 0],
                                    [np.sin(angle),  np.cos(angle), 0],
                                    [0, 0, 1]
                                    ])

    print(np.dot(object, rotation_matrix))

    return np.dot(object, rotation_matrix)


def scale3d(object, coefficient, axis):
    if axis == "x":
        scale_matrix = np.array([
                                [coefficient, 0, 0],
                                [0, 1, 0],
                                [0, 0, 1]
                                ])
    elif axis == "y":
        scale_matrix = np.array([
                                [1, 0, 0],
                                [0, coefficient, 0],
                                [0, 0, 1]
                                ])
    else:
        scale_matrix = np.array([
                                [1, 0, 0],
                                [0, 1, 0],
                                [0, 0, coefficient]
                                ])

    print(np.dot(object, scale_matrix))

    return np.dot(object, scale_matrix)


def reflect3d(object, mirror_axis):
    if mirror_axis == "x":
        reflect_matrix = np.array([
                                  [1, 0, 0],
                                  [0, -1, 0],
                                  [0, 0, -1]
                                  ])
    elif mirror_axis == "y":
        reflect_matrix = np.array([
                                  [-1, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, -1]
                                  ])
    else:
        reflect_matrix = np.array([
                                  [-1, 0, 0],
                                  [0, -1, 0],
                                  [0, 0, 1]
                                  ])

    print(np.dot(object, reflect_matrix))

    return np.dot(object, reflect_matrix)


pyramid = np.array([
                    [0,   0,   0],
                    [1,   0,   0],
                    [1,   1,   0],
                    [0,   1,   0],
                    [0.5, 0.5, 1]
                    ])
batman = np.array([
                   [0,       0],
                   [1,     0.2],
                   [0.4,     1],
                   [0.5,   0.4],
                   [0,     0.8],
                   [-0.5,  0.4],
                   [-0.4,    1],
                   [-1,    0.2],
                   [0,       0]
                   ])
star = np.array([
                 [0,     0],
                 [0.5, 1.5],
                 [1,     0],
                 [0,     1],
                 [1,     1],
                 [0,     0]
                 ])
plt.figure()

plt.plot(batman[:, 0], batman[:, 1], 'b')
plt.plot(star[:, 0], star[:, 1], 'g')

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.grid(True)

# rotate_batman = rotate(batman, 90)
# plt.plot(rotate_batman[:, 0], rotate_batman[:, 1], 'b')

# rotate_star = rotate(star, 180)
# plt.plot(rotate_star[:, 0], rotate_star[:, 1], 'g')

# scale_batman = scale(batman, 1.5)
# plt.plot(scale_batman[:, 0], scale_batman[:, 1], 'b')

# scale_star = scale(star, 0.5)
# plt.plot(scale_star[:, 0], scale_star[:, 1], 'g')

# reflect_batman = reflect(batman, "x")
# plt.plot(reflect_batman[:, 0], reflect_batman[:, 1], 'b')

# rotate_star = rotate(star, 180)
# plt.plot(rotate_star[:, 0], rotate_star[:, 1], 'g')

# tilt_batman = tilt(batman, 45, "x")
# plt.plot(tilt_batman[:, 0], tilt_batman[:, 1], 'b')

# tilt_star = tilt(star, 15, "y")
# plt.plot(tilt_star[:, 0], tilt_star[:, 1], 'g')

# universal_batman = universal(batman, 90, 1.5, "x", 45, "x")
# plt.plot(universal_batman[:, 0], universal_batman[:, 1], 'b')

# universal_star = universal(star, 180, 0.5, "y", 15, "y")
# plt.plot(universal_star[:, 0], universal_star[:, 1], 'g')


plt.show()


faces = [
    [pyramid[j] for j in [0, 1, 4]],
    [pyramid[j] for j in [1, 2, 4]],
    [pyramid[j] for j in [2, 3, 4]],
    [pyramid[j] for j in [3, 0, 4]],
    [pyramid[j] for j in [0, 1, 2, 3]]
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.add_collection3d(Poly3DCollection(faces, facecolors='g', linewidths=1, edgecolors='g', alpha=0.5))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

rotate_pyramid = rotate3d(pyramid, 90, "x")
faces = [
    [rotate_pyramid[j] for j in [0, 1, 4]],
    [rotate_pyramid[j] for j in [1, 2, 4]],
    [rotate_pyramid[j] for j in [2, 3, 4]],
    [rotate_pyramid[j] for j in [3, 0, 4]],
    [rotate_pyramid[j] for j in [0, 1, 2, 3]]
]
ax.add_collection3d(Poly3DCollection(faces, facecolors='b', linewidths=1, edgecolors='b', alpha=0.5))

scale_pyramid = scale3d(pyramid, 2, "z")
faces = [
    [scale_pyramid[j] for j in [0, 1, 4]],
    [scale_pyramid[j] for j in [1, 2, 4]],
    [scale_pyramid[j] for j in [2, 3, 4]],
    [scale_pyramid[j] for j in [3, 0, 4]],
    [scale_pyramid[j] for j in [0, 1, 2, 3]]
]
ax.add_collection3d(Poly3DCollection(faces, facecolors='r', linewidths=1, edgecolors='r', alpha=0.5))


plt.show()
