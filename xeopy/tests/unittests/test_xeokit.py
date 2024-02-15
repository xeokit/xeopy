import pytest
from xeopy import Xeokit


def test_create():
    xeokit = Xeokit()
    actual = xeokit.create()
    f = open("actual_created.html", "w")
    f.write(actual)
    f.close()
    expected = """"""
    assert actual == expected
