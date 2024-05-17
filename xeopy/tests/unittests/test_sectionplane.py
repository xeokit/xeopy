import pytest
from xeopy import SectionPlane


def test_init_default():
    section_plane = SectionPlane()

    assert section_plane.variable_name == "sectionPlane"
    assert section_plane.section_planes_plugin_variable_name == "sectionPlanes"
    assert section_plane.id == "mySectionPlane"
    assert section_plane.position == [10.95, 1.95, -10.35]
    assert section_plane.direction == [0.0, -1.0, 0.0]
    assert section_plane.show_control is True


def test_init_all_filled():
    section_plane = SectionPlane(variable_name="another_variable_name",
                                 section_planes_plugin_variable_name="another_section_planes_plugin_variable_name",
                                 id="anotherId",
                                 position=[0.1, 0.2, 0.3],
                                 direction=[-0.4, -0.5, -0.6],
                                 show_control=False)

    assert section_plane.variable_name == "another_variable_name"
    assert section_plane.section_planes_plugin_variable_name == "another_section_planes_plugin_variable_name"
    assert section_plane.id == "anotherId"
    assert section_plane.position == [0.1, 0.2, 0.3]
    assert section_plane.direction == [-0.4, -0.5, -0.6]
    assert section_plane.show_control is False


def test_str_show_control():
    section_plane = SectionPlane()

    assert section_plane.__str__() == ('const sectionPlane = sectionPlanes.createSectionPlane({\n'
 'id: "mySectionPlane"\n'
 'pos: [10.95, 1.95, -10.35]\n'
 'dir: [0.0, -1.0, 0.0]\n'
 '});\n'
 'sectionPlanes.showControl(mySectionPlane)\n')


def test_str_not_show_control():
    section_plane = SectionPlane(show_control=False)

    assert section_plane.__str__() == ('const sectionPlane = sectionPlanes.createSectionPlane({\n'
 'id: "mySectionPlane"\n'
 'pos: [10.95, 1.95, -10.35]\n'
 'dir: [0.0, -1.0, 0.0]\n'
 '});')


def test_get_additional_styles():
    section_plane = SectionPlane()

    assert section_plane.get_additional_styles() == {}


def test_get_additional_imports():
    section_plane = SectionPlane()

    assert section_plane.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    section_plane = SectionPlane()

    assert section_plane.get_xeokit_modules_needed() == {}

