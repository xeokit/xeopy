from xeopy import *

content = []

content.append(Viewer())
content.append(CameraSettings())
content.append(WebIFCLoaderPlugin(path="example_models/Duplex.ifc"))

xeokit = Xeokit(content=content, file_path="read_ifc.html")

xeokit.create_and_save()
