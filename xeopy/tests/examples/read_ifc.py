from xeopy import *

content = []

content.append(Viewer())
content.append(CameraSettings())
content.append(IfcLoader(path="IfcOpenHouse2x3.ifc"))

xeokit = Xeokit(content=content, file_path="read_ifc.html")

xeokit.create_and_save()
