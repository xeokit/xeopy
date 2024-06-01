import pytest
from xeopy import VectorText


def test_init_default():
    vector_text = VectorText()

    assert vector_text.text == "Vector text content"
    assert vector_text.size == 2
    assert vector_text.line_width == 2
    assert vector_text.position == [0.0, 0.0, 0.0]
    assert vector_text.color == [0.0, 0.0, 0.0]
    assert vector_text.viewer_variable_name == "viewer"


def test_init_all_filled():
    vector_text = VectorText(text="Another text", size=5, line_width=3, position=[1.1, 2.2, 3.3], color=[0.1, 0.2, 0.3],
              viewer_variable_name="another_viewer")

    assert vector_text.text == "Another text"
    assert vector_text.size == 5
    assert vector_text.line_width == 3
    assert vector_text.position == [1.1, 2.2, 3.3]
    assert vector_text.color == [0.1, 0.2, 0.3]
    assert vector_text.viewer_variable_name == "another_viewer"


def test_str():
    vector_text = VectorText()

    assert vector_text.__str__() == ('new Mesh(viewer.scene,{\n'
 '   geometry: new ReadableGeometry(viewer.scene, buildVectorTextGeometry({\n'
 '       text: `Vector text content`,\n'
 '       size: 2,\n'
 '   })),\n'
 '   material: new PhongMaterial(viewer.scene, {\n'
 '       diffuse: [0.0, 0.0, 0.0],\n'
 '       lineWidth: 2,\n'
 '   }),\n'
 'position: [0.0, 0.0, 0.0]\n'
 '});')


def test_get_additional_styles():
    vector_text = VectorText()

    assert vector_text.get_additional_styles() == {}


def test_get_additional_imports():
    vector_text = VectorText()

    assert vector_text.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    vector_text = VectorText()

    assert vector_text.get_xeokit_modules_needed() == {"ReadableGeometry", "buildVectorTextGeometry", "Mesh", "PhongMaterial"}
