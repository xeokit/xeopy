from xeopy import *

content = []  # Starting a content for the file

content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings())  # Adding Camera with default settings

# Setting up the IFC setup
content.append(IFCAPIInitiationStart())  # WebIFCLoaderPlugin needs this IFC API initiation start
content.append(WebIFCLoaderPlugin(path="example_models/Duplex.ifc"))  # Loading IFC file
content.append(End())  # WebIFCLoaderPlugin needs this IFC API initiation end

# Creating a file

xeokit = Xeokit(content=content, file_path="read_ifc.html")
xeokit.create_and_save()
