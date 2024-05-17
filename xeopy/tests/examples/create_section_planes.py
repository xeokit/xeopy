from xeopy import *

content = []

content.append(Viewer())
content.append(CameraSettings())
content.append(WebIFCLoaderPlugin(path="IfcOpenHouse2x3.ifc"))

content.append(SectionPlanesPlugin())
content.append(SectionPlane())

xeokit = Xeokit(content=content, file_path="create_section_planes.html")

xeokit.create_and_save()
