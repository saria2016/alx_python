#!/usr/bin/python3
"""
Creates a BaseGeometry class.
"""


class BaseGeometry:
    """class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
