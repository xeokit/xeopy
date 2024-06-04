from xeopy import *

content = []  # Starting a content for the file

content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings())  # Adding Camera with default settings

content.append(XKTLoaderPlugin(variable_name="loader"))  # Creating XKTLoaderPlugin needed to load XKT file
content.append(SceneModelLoading(loader_variable_name="loader", path="example_models/Duplex.xkt"))  # Loading XKT file and creating sceneModel

# Creating a file

xeokit = Xeokit(content=content, file_path="read_xkt.html")
xeokit.create_and_save()
