"""
Configuration for IX-Emmanuel

Holds constants and configuration parameters used across
the IX-Emmanuel aerospace physics modules.
"""

# Physical constants
SPEED_OF_LIGHT = 299_792_458  # meters per second
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m^3 kg^-1 s^-2
PLANCK_CONSTANT = 6.62607015e-34  # Js

# Default celestial body parameters (Earth as example)
DEFAULT_EARTH_MASS_KG = 5.972e24  # kilograms
DEFAULT_EARTH_RADIUS_M = 6.371e6  # meters

# Calculation limits
MAX_VELOCITY = SPEED_OF_LIGHT * 0.999  # Max velocity for relativistic calculations (avoid division by zero)
MIN_RADIUS_M = 1e-2  # Minimum radius to prevent division by zero in escape velocity calc
