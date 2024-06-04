import pytest
from xeopy import IFCAPIInitiationStart


def test_init_default():
    ifc_api_initiation_start = IFCAPIInitiationStart()

    assert ifc_api_initiation_start.wasm_path == "https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/"

def test_init_all_filled():
    ifc_api_initiation_start = IFCAPIInitiationStart(wasm_path="https://cdn.jsdelivr.net/npm/web-ifc@0.0.52/")

    assert ifc_api_initiation_start.wasm_path == "https://cdn.jsdelivr.net/npm/web-ifc@0.0.52/"


def test_str():
    ifc_loader = IFCAPIInitiationStart()

    assert ifc_loader.__str__() == ('\n'
 '    const IfcAPI = new WebIFC.IfcAPI();\n'
 '    IfcAPI.SetWasmPath("https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/");\n'
 '\n'
 '    IfcAPI.Init().then(() => {')


def test_get_additional_styles():
    ifc_loader = IFCAPIInitiationStart()

    assert ifc_loader.get_additional_styles() == {}


def test_get_additional_imports():
    ifc_loader = IFCAPIInitiationStart()

    assert ifc_loader.get_additional_imports() == {'import * as WebIFC from "https://cdn.jsdelivr.net/npm/web-ifc@0.0.51/web-ifc-api.js";'}


def test_get_xeokit_modules_needed():
    ifc_loader = IFCAPIInitiationStart()

    assert ifc_loader.get_xeokit_modules_needed() == {}
