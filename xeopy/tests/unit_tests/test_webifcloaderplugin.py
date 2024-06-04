import pytest
from xeopy import WebIFCLoaderPlugin


def test_init_default():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.variable_name == "ifcLoader"
    assert ifc_loader.viewer_variable_name == "viewer"


def test_init_all_filled():
    ifc_loader = WebIFCLoaderPlugin(variable_name="another_ifcLoader",
                                    viewer_variable_name="another_viewer")

    assert ifc_loader.variable_name == "another_ifcLoader"
    assert ifc_loader.viewer_variable_name == "another_viewer"


def test_str():
    ifc_loader = WebIFCLoaderPlugin()

    assert ifc_loader.__str__() == ('\n'
 '        const ifcLoader = new WebIFCLoaderPlugin(viewer, {\n'
 '            WebIFC,\n'
 '            IfcAPI\n'
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
