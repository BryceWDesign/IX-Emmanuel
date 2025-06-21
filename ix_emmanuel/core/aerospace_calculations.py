"""
Core aerospace physics calculations for IX-Emmanuel

Includes functions to compute orbital velocities, escape velocities,
and relativistic effects relevant to aerospace engineering.
"""

from ix_emmanuel.config.emmanuel_config import (
    GRAVITATIONAL_CONSTANT,
    DEFAULT_EARTH_MASS_KG,
    DEFAULT_EARTH_RADIUS_M,
    SPEED_OF_LIGHT,
    MAX_VELOCITY,
    MIN_RADIUS_M,
)
from ix_emmanuel.utils.emmanuel_math_utils import vector_magnitude
import math

def escape_velocity(mass_kg: float = DEFAULT_EARTH_MASS_KG, radius_m: float = DEFAULT_EARTH_RADIUS_M) -> float:
    """
    Calculate the escape velocity from a celestial body.

    Args:
        mass_kg (float): Mass of the body in kilograms.
        radius_m (float): Radius from the center of the body in meters.

    Returns:
        float: Escape velocity in meters per second.
    """
    if radius_m < MIN_RADIUS_M:
        radius_m = MIN_RADIUS_M
    return math.sqrt(2 * GRAVITATIONAL_CONSTANT * mass_kg / radius_m)

def orbital_velocity(mass_kg: float = DEFAULT_EARTH_MASS_KG, radius_m: float = DEFAULT_EARTH_RADIUS_M) -> float:
    """
    Calculate the circular orbital velocity at a given radius.

    Args:
        mass_kg (float): Mass of the central body in kilograms.
        radius_m (float): Radius from the center of the body in meters.

    Returns:
        float: Orbital velocity in meters per second.
    """
    if radius_m < MIN_RADIUS_M:
        radius_m = MIN_RADIUS_M
    return math.sqrt(GRAVITATIONAL_CONSTANT * mass_kg / radius_m)

def relativistic_velocity_adjustment(velocity_m_s: float) -> float:
    """
    Adjust velocity based on relativistic effects.

    Args:
        velocity_m_s (float): Velocity in meters per second.

    Returns:
        float: Velocity adjusted for relativistic effects (less than SPEED_OF_LIGHT).
    """
    if velocity_m_s >= MAX_VELOCITY:
        velocity_m_s = MAX_VELOCITY
    beta = velocity_m_s / SPEED_OF_LIGHT
    gamma = 1 / math.sqrt(1 - beta**2)
    return velocity_m_s / gamma
