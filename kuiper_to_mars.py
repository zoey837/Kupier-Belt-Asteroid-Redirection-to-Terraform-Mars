# Standard library
import argparse
import math
from pathlib import Path

# Scientific packages
import numpy as np
import matplotlib.pyplot as plt
import rebound
import yaml


# Constants that never change
G_AU3_MSUN_YR2 = 4 * math.pi**2
AU_KM = 149_597_870.7
G0_M_S2 = 9.80665


def load_config(config_path):
    """Load, validate, and return the YAML configuration."""
    ...


def vis_viva(r_au, a_au):
    """Return orbital speed in AU/yr."""
    ...


def transfer_orbit(aphelion_au, target_radius_au):
    """Calculate transfer semimajor axis, speed, and flight time."""
    ...


def departure_burn(initial_speed_au_yr, transfer_speed_au_yr, isp_s):
    """Calculate departure delta-v and rocket-equation mass ratio."""
    ...


def phase_angle(planet_radius_au, flight_time_yr, phase_offset_rad=0.0):
    """Calculate the planet's initial orbital phase."""
    ...


def build_simulation(config, planet_section, flight_time_yr, transfer_speed_au_yr):
    """Build the Sun-planet-asteroid REBOUND simulation."""
    ...


def find_encounter(simulation, planet_radius_au, planet_mass_msun,
                   planet_radius_km, flight_time_yr, config):
    """Integrate the trajectory and find encounter details."""
    ...


def jacobi_constant(simulation, planet_mass_msun, planet_radius_au):
    """Calculate the restricted three-body Jacobi constant."""
    ...


def flyby_summary(encounter, simulation, config):
    """Calculate flyby velocity, turn angle, and post-flyby orbit."""
    ...


def make_figures(results, config, output_dir):
    """Create and save the trajectory and encounter-distance figures."""
    ...


def write_summary(results, config, output_dir):
    """Print and save the headline results."""
    ...


def main():
    """Select the run mode and coordinate the functions."""
    ...


if __name__ == "__main__":
    main()
