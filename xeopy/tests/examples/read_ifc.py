from xeopy import *

xeokit = Xeokit(content=[Viewer(), CameraSettings(), IfcLoader(path="Duplex.ifc")], file_path="read_ifc.html")
xeokit.create_and_save()
