import pytest
from xeopy import End


def test_str():
    end = End()

    assert end.__str__() == '\n    });'

def test_get_additional_styles():
    end = End()

    assert end.get_additional_styles() == {}


def test_get_additional_imports():
    end = End()

    assert end.get_additional_imports() == {}


def test_get_xeokit_modules_needed():
    end = End()

    assert end.get_xeokit_modules_needed() == {}
