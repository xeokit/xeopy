from xeopy import *
import inspect

content = []  # Starting a content for the file
content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings(eye=[0, 0, 100], look=[0, 0, 0], up=[0, 1, 0]))  # Adding Camera

# Creating a vector text

code = inspect.getsource(inspect.getmodule(inspect.currentframe()))  # We are getting a code of this file to display it

content.append(VectorText(text=code, position=[-60, 50, 0]))  # Adding vector text

# Creating a file

xeokit = Xeokit(content=content, file_path="create_vector_text.html")
xeokit.create_and_save()
