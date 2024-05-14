import pytest
from xeopy import SceneModelOnLoaded


def test_init_default():
    scene_model_on_loaded = SceneModelOnLoaded()

    assert scene_model_on_loaded.scene_model_id == "sceneModel"
    assert scene_model_on_loaded.start is True


def test_init_all_filled():
    scene_model_on_loaded = SceneModelOnLoaded(scene_model_id="another_scene_model_id", start=False)

    assert scene_model_on_loaded.scene_model_id == "another_scene_model_id"
    assert scene_model_on_loaded.start is False


def test_str_start():
    scene_model_on_loaded = SceneModelOnLoaded()

    assert scene_model_on_loaded.__str__() == "sceneModel.on(\"loaded\", () => {"


def test_str_end():
    scene_model_on_loaded = SceneModelOnLoaded(start=False)

    assert scene_model_on_loaded.__str__() == "});"


def test_get_additional_styles():
    scene_model_on_loaded = SceneModelOnLoaded()

    assert scene_model_on_loaded.get_additional_styles() == {}


def test_get_additional_imports():
    scene_model_on_loaded = SceneModelOnLoaded()

    assert scene_model_on_loaded.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    scene_model_on_loaded = SceneModelOnLoaded()

    assert scene_model_on_loaded.get_xeokit_modules_needed() == {}

