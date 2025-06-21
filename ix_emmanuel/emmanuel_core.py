"""
IX-Emmanuel Core Module

Provides advanced aerospace and physics knowledge processing,
calculations, and query handling for high-level scientific support.
"""

import math

class EmmanuelCore:
    def __init__(self):
        # Initialize constants for physics calculations
        self.speed_of_light = 299_792_458  # meters per second
        self.gravitational_constant = 6.67430e-11  # m^3 kg^-1 s^-2
        self.planck_constant = 6.62607015e-34  # Js

    def calculate_escape_velocity(self, mass_kg: float, radius_m: float) -> float:
        """
        Calculate escape velocity for a celestial body.

        Args:
            mass_kg (float): Mass of the body in kilograms.
            radius_m (float): Radius of the body in meters.

        Returns:
            float: Escape velocity in meters per second.
        """
        return math.sqrt(2 * self.gravitational_constant * mass_kg / radius_m)

    def photon_energy(self, frequency_hz: float) -> float:
        """
        Calculate photon energy using Planck's equation.

        Args:
            frequency_hz (float): Frequency of the photon in hertz.

        Returns:
            float: Energy in joules.
        """
        return self.planck_constant * frequency_hz

    def relativistic_time_dilation(self, velocity_m_s: float, proper_time_s: float) -> float:
        """
        Calculate time dilation at relativistic speeds.

        Args:
            velocity_m_s (float): Velocity of the moving object in m/s.
            proper_time_s (float): Proper time interval in seconds.

        Returns:
            float: Dilated time interval in seconds.
        """
        c = self.speed_of_light
        if velocity_m_s >= c:
            raise ValueError("Velocity cannot exceed the speed of light.")
        gamma = 1 / math.sqrt(1 - (velocity_m_s ** 2) / (c ** 2))
        return gamma * proper_time_s
