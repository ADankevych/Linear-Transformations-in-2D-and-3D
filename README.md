# Linear Transformations in 2D and 3D

This project demonstrates various linear transformations on 2D and 3D objects using custom functions and the OpenCV library. The project is divided into two main parts: implementing the transformations manually and using library functions.

## Part 1: Custom Implementation of Linear Transformations

### 1 Creating and Visualizing Objects

We start by creating two 2D objects: a "batman" shape and a "star" shape. Additionally, we create a 3D object, a "pyramid." These objects are defined as arrays of coordinates.

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 2D objects
batman = np.array([[0, 0], [1, 0.2], [0.4, 1], [0.5, 0.4], [0, 0.8], [-0.5, 0.4], [-0.4, 1], [-1, 0.2], [0, 0]])
star = np.array([[0, 0], [0.5, 1.5], [1, 0], [0, 1], [1, 1], [0, 0]])

# 3D object
pyramid = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]])
```

### 2 Implementing Linear Transformations
We implement functions for the following transformations:
  - Rotation: Rotating the object by a specified angle.
  - Scaling: Scaling the object by a given coefficient.
  - Reflection: Reflecting the object across a specified axis.
  - Tilting: Skewing the object by a certain angle along a specified axis.
  - Universal Transformation: Applying a custom transformation matrix.

Example function for rotation:
```python
def rotate(object, angle):
    angle = np.radians(angle)
    rotation_matrix = np.array([
                                [np.cos(angle), -np.sin(angle)],
                                [np.sin(angle),  np.cos(angle)]
                                ])
    return np.dot(object, rotation_matrix)
```

### 3 Visualizing Transformations
After each transformation, the resulting objects and their matrices are printed and visualized using matplotlib.
### 4 3D Transformations
We extend the transformations to 3D, demonstrating rotation and scaling on a pyramid.
## Part 2: Using OpenCV for Transformations

### 1 Applying Transformations with OpenCV
We use the OpenCV library to apply similar transformations on 2D objects and images. OpenCV provides built-in functions for rotations, scaling, and flipping images.
Example code:
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.png')
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
scaled_image = cv2.resize(image, None, fx=5, fy=5)
cv2.imshow('Rotated', rotated_image)
cv2.imshow('Scaled', scaled_image)
```
### 2 Comparison and Analysis
We compare the results from our custom implementations with those from OpenCV, noting differences in precision and efficiency. We also explore how different elements of transformation matrices affect the output.
## Conclusion

This project illustrates the fundamental concepts of linear transformations in both 2D and 3D spaces. By manually implementing these transformations and comparing them with library functions, we gain a deeper understanding of how these transformations work and their practical applications in computer graphics and image processing.
