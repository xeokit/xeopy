from xeopy import *

content = []  # Starting a content for the file

content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings())  # Adding Camera with default settings
content.append(WebIFCLoaderPlugin(path="example_models/IfcOpenHouse2x3.ifc"))  # Loading IFC file

content.append(SectionPlanesPlugin())  # Starting SectionPlanesPlugin needed for SectionPlanes
content.append(SectionPlane())  # Adding SectionPlane

# Creating a file

xeokit = Xeokit(content=content, file_path="create_section_planes.html")
xeokit.create_and_save()
