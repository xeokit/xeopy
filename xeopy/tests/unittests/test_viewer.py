import pytest
from xeopy import Viewer


def test_init_default():
    viewer = Viewer()

    assert viewer.viewer_id == "viewer"
    assert viewer.canvas_id == "xeokit_canvas"
    assert viewer.transparent is True
    assert viewer.dtx_enabled is True


def test_init_all_filled():
    viewer = Viewer(viewer_id="another_viewer", canvas_id="another_canvas", transparent=False, dtx_enabled=False)

    assert viewer.viewer_id == "another_viewer"
    assert viewer.canvas_id == "another_canvas"
    assert viewer.transparent is False
    assert viewer.dtx_enabled is False


def test_str():
    viewer = Viewer()

    assert viewer.__str__() == """const viewer = new Viewer({
    canvasId: "xeokit_canvas",
    transparent: true,
    dtxEnabled: true
});"""


def test_get_additional_styles():
    viewer = Viewer()

    assert viewer.get_additional_styles() == {}


def test_get_additional_imports():
    viewer = Viewer()

    assert viewer.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    viewer = Viewer()

    assert viewer.get_xeokit_modules_needed() == {"Viewer"}
