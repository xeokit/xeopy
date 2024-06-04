import pytest
from xeopy import SceneModelLoading


def test_init_default():
    scene_model_loading = SceneModelLoading()

    assert scene_model_loading.variable_name == "sceneModel"
    assert scene_model_loading.loader_variable_name == "loader"
    assert scene_model_loading.path == "Duplex.ifc"
    assert scene_model_loading.edges is True


def test_init_all_filled():
    scene_model_loading = SceneModelLoading(variable_name="another_sceneModel",
                                            loader_variable_name="another_loader",
                                            path="Duplex.xkt",
                                            edges=False)

    assert scene_model_loading.variable_name == "another_sceneModel"
    assert scene_model_loading.loader_variable_name == "another_loader"
    assert scene_model_loading.path == "Duplex.xkt"
    assert scene_model_loading.edges is False


def test_str():
    scene_model_loading = SceneModelLoading()

    assert scene_model_loading.__str__() == ('\n'
 '        const sceneModel = loader.load({\n'
 '            src: "Duplex.ifc",\n'
 '            edges: true\n'
 '        });\n')


def test_get_additional_styles():
    scene_model_loading = SceneModelLoading()

    assert scene_model_loading.get_additional_styles() == {}


def test_get_additional_imports():
    scene_model_loading = SceneModelLoading()

    assert scene_model_loading.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    scene_model_loading = SceneModelLoading()

    assert scene_model_loading.get_xeokit_modules_needed() == {}
