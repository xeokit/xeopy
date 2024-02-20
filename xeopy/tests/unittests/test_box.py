import pytest
from xeopy import Box


def test_init_default():
    box = Box()

    assert box.x_size == 1.0
    assert box.y_size == 1.0
    assert box.z_size == 1.0
    assert box.position == [0.0, 0.0, 0.0]


def test_init_all_filled():
    box = Box(x_size=2.0, y_size=3.0, z_size=4.0, position=[1.1, 2.2, 3.3])

    assert box.x_size == 2.0
    assert box.y_size == 3.0
    assert box.z_size == 4.0
    assert box.position == [1.1, 2.2, 3.3]

