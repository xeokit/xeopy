from xeopy import *

content = []  # Starting a content for the file

content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings())  # Adding Camera with default settings
content.append(WebIFCLoaderPlugin(path="example_models/Duplex.ifc"))  # Loading IFC file

# Creating a file

xeokit = Xeokit(content=content, file_path="read_ifc.html")
xeokit.create_and_save()
