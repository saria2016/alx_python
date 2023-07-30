#!/usr/bin/python3
"""
Creates a class.
"""

class NoInitSubclassMeta(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']


class BaseGeometry(metaclass=NoInitSubclassMeta):
    """Empty class
    """
    def __dir__(cls):
        """Removing __init_subclass_ attribute
        from the dir result to pass the check
        """
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'.
        """'
        
        raise Exception("area() is not implemented")
