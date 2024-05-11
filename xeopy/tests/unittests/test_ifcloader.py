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

    assert ifcLoader.__str__() == ('\n'
 '    const IfcAPI = new WebIFC.IfcAPI();\n'
 '    IfcAPI.SetWasmPath("https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/");\n'
 '\n'
 '    IfcAPI.Init().then(() => {\n'
 '        const ifcLoader = new WebIFCLoaderPlugin(viewer, {\n'
 '            WebIFC,\n'
 '            IfcAPI\n'
 '        });\n'
 '\n'
 '        const model = ifcLoader.load({\n'
 '            src: "Duplex.ifc",\n'
 '            edges: true\n'
 '        });\n'
 '    });\n')


def test_get_additional_imports():
    ifcLoader = IfcLoader()

    assert ifcLoader.get_additional_imports() == {'import * as WebIFC from "https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/web-ifc-api.js";'}


def test_get_xeokit_modules_needed():
    ifcLoader = IfcLoader()

    assert ifcLoader.get_xeokit_modules_needed() == {"WebIFCLoaderPlugin"}
