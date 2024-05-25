from xeopy import *

content = []  # Starting a content for the file

content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings(eye=[-10, 10, -10], look=[0, 0, 0]))  # Adding Camera with default settings
content.append(WebIFCLoaderPlugin(path="example_models/Duplex.ifc"))  # Loading IFC file

content.append(SectionPlanesPlugin())  # Starting SectionPlanesPlugin needed for SectionPlanes
content.append(SectionPlane(position=[10.95, 1.5, -10.35]))  # Adding SectionPlane

# Creating a file

xeokit = Xeokit(content=content, file_path="create_section_planes.html")
xeokit.create_and_save()
