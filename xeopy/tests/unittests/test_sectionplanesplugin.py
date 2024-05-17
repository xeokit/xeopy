import pytest
from xeopy import SectionPlanesPlugin


def test_init_default():
    section_planes_plugin = SectionPlanesPlugin()

    assert section_planes_plugin.viewer_id == "viewer"
    assert section_planes_plugin.overview_canvas_id == "mySectionPlanesOverviewCanvas"
    assert section_planes_plugin.overview_visible is True
    assert section_planes_plugin.section_planes_plugin_id == "sectionPlanes"


def test_init_all_filled():
    section_planes_plugin = SectionPlanesPlugin(viewer_id="another_viewer",
                                                overview_canvas_id="another_canvas",
                                                overview_visible=False,
                                                section_planes_plugin_id="another_id")

    assert section_planes_plugin.viewer_id == "another_viewer"
    assert section_planes_plugin.overview_canvas_id == "another_canvas"
    assert section_planes_plugin.overview_visible is False
    assert section_planes_plugin.section_planes_plugin_id == "another_id"


def test_str():
    section_planes_plugin = SectionPlanesPlugin()

    assert section_planes_plugin.__str__() == ('const sectionPlanes= new SectionPlanesPlugin(viewer, {\n'
 'overviewCanvasId: "mySectionPlanesOverviewCanvas",\n'
 'overviewVisible: true,\n'
 '});')


def test_get_additional_styles():
    section_planes_plugin = SectionPlanesPlugin()

    assert section_planes_plugin.get_additional_styles() == {'#mySectionPlanesOverviewCanvas {\n'
 '            position: absolute;\n'
 '            width: 250px;\n'
 '            height: 250px;\n'
 '            bottom: 70px;\n'
 '            right: 10px;\n'
 '            z-index: 200000;\n'
 '            /*border: 1px solid blue;*/\n'
 '        }'}


def test_get_additional_imports():
    section_planes_plugin = SectionPlanesPlugin()

    assert section_planes_plugin.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    section_planes_plugin = SectionPlanesPlugin()

    assert section_planes_plugin.get_xeokit_modules_needed() == {"SectionPlanesPlugin"}
