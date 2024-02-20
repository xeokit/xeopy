import pytest
from xeopy import IfcLoader


def test_init_default():
    ifcLoader = IfcLoader()

    assert ifcLoader.path == "Duplex.ifc"
    assert ifcLoader.edges is True
    assert ifcLoader.viewer_id == "viewer"


def test_init_all_filled():
    ifcLoader = IfcLoader(path="IfcOpenHouse2x3.ifc", edges=False, viewer_id="another_viewer")

    assert ifcLoader.path == "IfcOpenHouse2x3.ifc"
    assert ifcLoader.edges is False
    assert ifcLoader.viewer_id == "another_viewer"


def test_str():
    ifcLoader = IfcLoader()

    assert ifcLoader.__str__() == """
    const webIFCLoader = new WebIFCLoaderPlugin(viewer, {
        wasmPath: "https://cdn.jsdelivr.net/npm/@xeokit/xeokit-sdk/dist/"
    });

    const model = webIFCLoader.load({
        src: \"Duplex.ifc\",
        edges: true
    });
"""


def test_get_xeokit_modules_needed():
    ifcLoader = IfcLoader()

    assert ifcLoader.get_xeokit_modules_needed() == {"WebIFCLoaderPlugin"}