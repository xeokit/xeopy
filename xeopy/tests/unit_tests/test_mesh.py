import pytest
from xeopy import Mesh


def test_init_default():
    mesh = Mesh()

    assert mesh.positions == [0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 5.0, 5.0, 0.0]
    assert mesh.indices == [0, 1, 2]
    assert mesh.normals == []
    assert mesh.uv == []
    assert mesh.color == [0.0, 1.0, 0.0]
    assert mesh.edges is True
    assert mesh.viewer_variable_name == "viewer"


def test_init_all_filled():
    positions = [1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1,
                 1,
                 -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1,
                 1,
                 -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1]
    indices = [0, 1, 2, 0, 2, 3, 4, 5, 6, 4, 6, 7, 8, 9, 10, 8, 10, 11, 12, 13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19,
               20,
               21, 22, 20, 22, 23]
    normals = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
               0, 1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, 0, -1,
               0, 0, -1, 0, 0, -1, 0, 0, -1]
    uv = [0.5, 0.6666, 0.25, 0.6666, 0.25, 0.3333, 0.5, 0.3333, 0.5, 0.6666, 0.5, 0.3333, 0.75, 0.3333, 0.75, 0.6666,
          0.5, 0.6666, 0.5, 1, 0.25, 1, 0.25, 0.6666, 0.25, 0.6666, 0.0, 0.6666, 0.0, 0.3333, 0.25, 0.3333,
          0.25, 0, 0.50, 0, 0.50, 0.3333, 0.25, 0.3333, 0.75, 0.3333, 1.0, 0.3333, 1.0, 0.6666, 0.75, 0.6666]

    mesh = Mesh(positions=positions,
                indices=indices,
                normals=normals,
                uv=uv,
                color=[1.0, 1.0, 0.0],
                edges=False,
                viewer_variable_name="another_viewer")

    assert mesh.positions == positions
    assert mesh.indices == indices
    assert mesh.normals == normals
    assert mesh.uv == uv
    assert mesh.color == [1.0, 1.0, 0.0]
    assert mesh.edges is False
    assert mesh.viewer_variable_name == "another_viewer"


def test_str():
    mesh = Mesh()

    assert mesh.__str__() == ('new Mesh(viewer.scene,{\n'
 '   geometry: new ReadableGeometry(viewer.scene, {\n'
 '       primitive: "triangles",\n'
 '       positions: [0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 5.0, 5.0, 0.0],\n'
 '       indices: [0, 1, 2],\n'
 '       normals: [],\n'
 '       uv: [],\n'
 '   }),\n'
 '   material: new PhongMaterial(viewer.scene, {\n'
 '       diffuse: [0.0, 1.0, 0.0],\n'
 '   }),\n'
 '   edges: true,\n'
 '});')


def test_get_additional_styles():
    mesh = Mesh()

    assert mesh.get_additional_styles() == {}


def test_get_additional_imports():
    mesh = Mesh()

    assert mesh.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    mesh = Mesh()

    assert mesh.get_xeokit_modules_needed() == {"ReadableGeometry", "Mesh", "PhongMaterial"}
