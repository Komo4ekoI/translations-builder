"""
This module provides a class for building translation file with classes
"""
__all__ = ("InvalidNameError", "DuplicateNameError", "ClassBuilder")

from .errors import InvalidNameError, DuplicateNameError
from ._builder import ClassBuilder
