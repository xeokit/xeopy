from xeopy import *
import random

# Creating random spheres

x_range = (-10.0, 10.0)
y_range = (-20.0, 20.0)
z_range = (-30.0, 30.0)
box_size_range = (0.6, 1.0)
points = []
[points.append((random.uniform(*x_range), random.uniform(*y_range), random.uniform(*z_range))) for i in range(100)]
spheres = []
for i in points:
    spheres.append(Sphere(radius=random.uniform(*box_size_range),
                          width_segments=50,
                          height_segments=50,
                          center=[i[0], i[1], i[2]],
                          color=[abs(i[0])/x_range[1], abs(i[1])/y_range[1], abs(i[2])/z_range[1]]))

# Creating a file and adding all boxes there

xeokit = Xeokit(content=[Viewer(), CameraSettings(), spheres], file_path="create_spheres.html")
xeokit.create_and_save()
