import pytest
from xeopy import Sphere


def test_init_default():
    sphere = Sphere()

    assert sphere.radius == 1.0
    assert sphere.height_segments == 60
    assert sphere.width_segments == 60
    assert sphere.center == [0.0, 0.0, 0.0]
    assert sphere.color == [0.0, 0.0, 0.0]
    assert sphere.viewer_variable_name == "viewer"


def test_init_all_filled():
    sphere = Sphere(radius=2.0, height_segments=30, width_segments=40, center=[1.1, 2.2, 3.3], color=[0.1, 0.2, 0.3],
              viewer_variable_name="another_viewer")

    assert sphere.radius == 2.0
    assert sphere.height_segments == 30
    assert sphere.width_segments == 40
    assert sphere.center == [1.1, 2.2, 3.3]
    assert sphere.color == [0.1, 0.2, 0.3]
    assert sphere.viewer_variable_name == "another_viewer"


def test_str():
    sphere = Sphere()

    assert sphere.__str__() == ('new Mesh(viewer.scene,{\n'
 '   geometry: new ReadableGeometry(viewer.scene, buildSphereGeometry({\n'
 '       center: [0.0, 0.0, 0.0],\n'
 '       radius: 1.0,\n'
 '       heightSegments: 60,\n'
 '       widthSegments: 60,\n'
 '   })),\n'
 '   material: new PhongMaterial(viewer.scene, {\n'
 '       diffuse: [0.0, 0.0, 0.0],\n'
 '   })});')


def test_get_additional_styles():
    sphere = Sphere()

    assert sphere.get_additional_styles() == {}


def test_get_additional_imports():
    sphere = Sphere()

    assert sphere.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    sphere = Sphere()

    assert sphere.get_xeokit_modules_needed() == {"ReadableGeometry", "buildSphereGeometry", "Mesh", "PhongMaterial"}
