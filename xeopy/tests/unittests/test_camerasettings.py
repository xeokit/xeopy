import pytest
from xeopy import CameraSettings


def test_init_default():
    camera_settings = CameraSettings()

    assert camera_settings.viewer_id == "viewer"
    assert camera_settings.eye == [-3.933, 2.855, 27.018]
    assert camera_settings.look == [4.400, 3.724, 8.899]
    assert camera_settings.up == [-0.018, 0.999, 0.039]


def test_init_all_filled():
    camera_settings = CameraSettings(viewer_id="another_viewer", eye=[0.91, 0.83, -0.71], look=[0.12, 0.13, 0.14],
                                     up=[0.34, 0.21, 0.31])

    assert camera_settings.viewer_id == "another_viewer"
    assert camera_settings.eye == [0.91, 0.83, -0.71]
    assert camera_settings.look == [0.12, 0.13, 0.14]
    assert camera_settings.up == [0.34, 0.21, 0.31]


def test_str():
    camera_settings = CameraSettings()

    assert camera_settings.__str__() == """viewer.camera.eye = + [-3.933, 2.855, 27.018];
viewer.camera.look = + [4.4, 3.724, 8.899];
viewer.camera.up = + [-0.018, 0.999, 0.039];
"""


def test_get_xeokit_modules_needed():
    camera_settings = CameraSettings()

    assert camera_settings.get_xeokit_modules_needed() == {}

