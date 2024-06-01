import pytest
from xeopy import XKTLoaderPlugin


def test_init_default():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.path == "Duplex.xkt"
    assert xkt_loader.edges is True
    assert xkt_loader.viewer_variable_name == "viewer"
    assert xkt_loader.variable_name == "sceneModel"


def test_init_all_filled():
    xkt_loader = XKTLoaderPlugin(path="IfcOpenHouse2x3.xkt",
                                    edges=False,
                                    viewer_variable_name="another_viewer",
                                    variable_name="another_scene_model_id")

    assert xkt_loader.path == "IfcOpenHouse2x3.xkt"
    assert xkt_loader.edges is False
    assert xkt_loader.viewer_variable_name == "another_viewer"
    assert xkt_loader.variable_name == "another_scene_model_id"


def test_str():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.__str__() == ('\n'
 '    const ifcLoader = new XKTLoaderPlugin(viewer);\n'
 '\n'
 '    const sceneModel = ifcLoader.load({\n'
 '        src: "Duplex.xkt",\n'
 '        edges: true\n'
 '    });\n')


def test_get_additional_styles():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.get_additional_styles() == {}


def test_get_additional_imports():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.get_xeokit_modules_needed() == {"XKTLoaderPlugin"}
