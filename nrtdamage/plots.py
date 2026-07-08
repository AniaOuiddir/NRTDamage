"""
plots.py - Visualization functions for NRT damage results.

This module provides plotting functions to visualize radiation
damage as a function of various parameters.

Note: visualization functions are not tested as per project guidelines.
"""

import numpy as np
import matplotlib.pyplot as plt

from nrtdamage.physics import compute_dpa
from nrtdamage.materials import get_material, list_materials


def plot_dpa_vs_time(material_name, flux, damage_energy=1000.0,
                     max_time_years=10, save_path=None):
    """Plot DPA accumulation over time for a given material.

    Parameters
    ----------
    material_name : str
        Name of the material to plot.
    flux : float
        Neutron flux in n/cm2/s.
    damage_energy : float, optional
        Average damage energy per collision in eV. Default is 1000.0.
    max_time_years : float, optional
        Maximum irradiation time in years. Default is 10.
    save_path : str or None, optional
        If provided, saves the plot to this path. Default is None.
    """
    material = get_material(material_name)
    times_years = np.linspace(0, max_time_years, 100)
    times_seconds = times_years * 3.15e7

    dpa_values = [
        compute_dpa(
            flux=flux,
            cross_section=material["cross_section"],
            damage_energy=damage_energy,
            displacement_energy=material["displacement_energy"],
            time=t,
        )
        for t in times_seconds
    ]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(times_years, dpa_values, linewidth=2)
    ax.set_xlabel("Irradiation time (years)")
    ax.set_ylabel("DPA (displacements per atom)")
    ax.set_title(
        f"Radiation damage in {material_name.capitalize()} "
        f"(flux = {flux:.1e} n/cm²/s)"
    )
    ax.grid(True, alpha=0.3)

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    return fig, ax


def plot_dpa_comparison(flux, damage_energy=1000.0,
                        time_years=1.0, save_path=None):
    """Plot DPA comparison across all available materials.

    Parameters
    ----------
    flux : float
        Neutron flux in n/cm2/s.
    damage_energy : float, optional
        Average damage energy per collision in eV. Default is 1000.0.
    time_years : float, optional
        Irradiation time in years. Default is 1.0.
    save_path : str or None, optional
        If provided, saves the plot to this path. Default is None.
    """
    time_seconds = time_years * 3.15e7
    materials = list_materials()
    dpa_values = []

    for name in materials:
        mat = get_material(name)
        dpa = compute_dpa(
            flux=flux,
            cross_section=mat["cross_section"],
            damage_energy=damage_energy,
            displacement_energy=mat["displacement_energy"],
            time=time_seconds,
        )
        dpa_values.append(dpa)

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(materials, dpa_values, color="steelblue", alpha=0.8)
    ax.set_xlabel("Material")
    ax.set_ylabel("DPA (displacements per atom)")
    ax.set_title(
        f"DPA comparison after {time_years} year(s) "
        f"(flux = {flux:.1e} n/cm²/s)"
    )
    ax.grid(True, alpha=0.3, axis="y")

    for bar, value in zip(bars, dpa_values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:.2e}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    if save_path:
        fig.savefig(save_path, dpi=150, bbox_inches="tight")

    return fig, ax