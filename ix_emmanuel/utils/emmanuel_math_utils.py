"""
Mathematical utilities for IX-Emmanuel

Provides helper functions for aerospace physics calculations,
including vector operations and unit conversions.
"""

import math
from typing import Tuple

def vector_magnitude(vector: Tuple[float, float, float]) -> float:
    """
    Calculate the magnitude of a 3D vector.

    Args:
        vector (Tuple[float, float, float]): The (x, y, z) vector components.

    Returns:
        float: The magnitude (length) of the vector.
    """
    x, y, z = vector
    return math.sqrt(x**2 + y**2 + z**2)

def dot_product(v1: Tuple[float, float, float], v2: Tuple[float, float, float]) -> float:
    """
    Calculate the dot product of two 3D vectors.

    Args:
        v1, v2 (Tuple[float, float, float]): The vectors.

    Returns:
        float: The dot product scalar value.
    """
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def degrees_to_radians(degrees: float) -> float:
    """
    Convert degrees to radians.

    Args:
        degrees (float): Angle in degrees.

    Returns:
        float: Angle in radians.
    """
    return degrees * math.pi / 180.0

def radians_to_degrees(radians: float) -> float:
    """
    Convert radians to degrees.

    Args:
        radians (float): Angle in radians.

    Returns:
        float: Angle in degrees.
    """
    return radians * 180.0 / math.pi
