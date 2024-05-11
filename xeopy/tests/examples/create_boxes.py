from xeopy import *
import random

x_range = (-10.0, 10.0)
y_range = (-20.0, 20.0)
z_range = (-30.0, 30.0)
box_size_range = (0.6, 1.0)
points = []
[points.append((random.uniform(*x_range), random.uniform(*y_range), random.uniform(*z_range))) for i in range(100)]
boxes = []
for i in points:
    boxes.append(Box(x_size=random.uniform(*box_size_range),
                     y_size=random.uniform(*box_size_range),
                     z_size=random.uniform(*box_size_range),
                     center=[i[0], i[1], i[2]],
                     color=[abs(i[0])/x_range[1], abs(i[1])/y_range[1], abs(i[2])/z_range[1]]))

xeokit = Xeokit(content=[Viewer(), CameraSettings(), boxes], file_path="create_boxes.html")
xeokit.create_and_save()
