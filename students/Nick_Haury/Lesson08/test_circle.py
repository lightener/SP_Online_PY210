#!/usr/bin/env python3

import pytest
from circle import *

"""
Unit tests for Circle.py
"""

def test_instantiate_circle():
    # test if you can create circle and it saves radius
    circ = Circle(5)
    assert circ.radius == 5

def test_diameter():
    # test you can access diameter and is set correctly
    c = Circle(2)
    assert c.diameter == 4

def test_change_r_d():
    # test if you can change the circle properties
    c = Circle(5)
    c.radius = 10
    assert c.diameter == 20
    c.diameter = 30
    assert c.radius == 15.0

def test_area():
    """
    test if area is set properly, and test if AttributeError raised when trying
    to set area directly
    """
    c = Circle(5)
    assert math.isclose(78.54, c.area, abs_tol=0.001)
    with pytest.raises(AttributeError):
        c.area = 100
