import pytest
from xeopy import *


def test_run():
    xeokit = Xeokit(content=[Viewer(), CameraSettings(), IfcLoader(path="Duplex.ifc")], file_path="actual_created.html")
    xeokit.create_and_save()
