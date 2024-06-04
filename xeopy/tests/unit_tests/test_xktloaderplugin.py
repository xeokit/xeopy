import pytest
from xeopy import XKTLoaderPlugin


def test_init_default():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.variable_name == "xktLoader"
    assert xkt_loader.viewer_variable_name == "viewer"


def test_init_all_filled():
    xkt_loader = XKTLoaderPlugin(variable_name="another_xktLoader", viewer_variable_name="another_viewer")

    assert xkt_loader.variable_name == "another_xktLoader"
    assert xkt_loader.viewer_variable_name == "another_viewer"


def test_str():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.__str__() == '\n    const xktLoader = new XKTLoaderPlugin(viewer);\n'


def test_get_additional_styles():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.get_additional_styles() == {}


def test_get_additional_imports():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    xkt_loader = XKTLoaderPlugin()

    assert xkt_loader.get_xeokit_modules_needed() == {"XKTLoaderPlugin"}
