import pytest
from xeopy import WebIFCLoaderPlugin


def test_init_default():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.path == "Duplex.ifc"
    assert ifc_loader.edges is True
    assert ifc_loader.viewer_variable_name == "viewer"
    assert ifc_loader.variable_name == "sceneModel"


def test_init_all_filled():
    ifc_loader = WebIFCLoaderPlugin(path="IfcOpenHouse2x3.ifc",
                                    edges=False,
                                    viewer_variable_name="another_viewer",
                                    variable_name="another_scene_model_id")

    assert ifc_loader.path == "IfcOpenHouse2x3.ifc"
    assert ifc_loader.edges is False
    assert ifc_loader.viewer_variable_name == "another_viewer"
    assert ifc_loader.variable_name == "another_scene_model_id"


def test_str():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.__str__() == ('\n'
 '        const ifcLoader = new WebIFCLoaderPlugin(viewer, {\n'
 '            WebIFC,\n'
 '            IfcAPI\n'
 '        });\n'
 '\n'
 '        const sceneModel = ifcLoader.load({\n'
 '            src: "Duplex.ifc",\n'
 '            edges: true\n'
 '        });\n')


def test_get_additional_styles():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.get_additional_styles() == {}


def test_get_additional_imports():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.get_xeokit_modules_needed() == {"WebIFCLoaderPlugin"}
