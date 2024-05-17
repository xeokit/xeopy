import pytest
from xeopy import Box


def test_init_default():
    box = Box()

    assert box.x_size == 1.0
    assert box.y_size == 1.0
    assert box.z_size == 1.0
    assert box.center == [0.0, 0.0, 0.0]
    assert box.color == [0.0, 0.0, 0.0]
    assert box.viewer_variable_name == "viewer"


def test_init_all_filled():
    box = Box(x_size=2.0, y_size=3.0, z_size=4.0, center=[1.1, 2.2, 3.3], color=[0.1, 0.2, 0.3],
              viewer_variable_name="another_viewer")

    assert box.x_size == 2.0
    assert box.y_size == 3.0
    assert box.z_size == 4.0
    assert box.center == [1.1, 2.2, 3.3]
    assert box.color == [0.1, 0.2, 0.3]
    assert box.viewer_variable_name == "another_viewer"


def test_str():
    box = Box()

    assert box.__str__() == ('new Mesh(viewer.scene,{\n'
 '   geometry: new ReadableGeometry(viewer.scene, buildBoxGeometry({\n'
 '       center: [0.0, 0.0, 0.0],\n'
 '       xSize: 1.0,\n'
 '       ySize: 1.0,\n'
 '       zSize: 1.0,\n'
 '   })),\n'
 '   material: new PhongMaterial(viewer.scene, {\n'
 '       diffuse: [0.0, 0.0, 0.0],\n'
 '   })});')


def test_get_additional_styles():
    box = Box()

    assert box.get_additional_styles() == {}


def test_get_additional_imports():
    box = Box()

    assert box.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    box = Box()

    assert box.get_xeokit_modules_needed() == {"ReadableGeometry", "buildBoxGeometry", "Mesh", "PhongMaterial"}
