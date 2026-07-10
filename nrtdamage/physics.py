"""
physics.py - Core NRT damage model calculations.

This module implements the Norgett-Robinson-Torrens (NRT) model
for estimating atomic displacement damage in irradiated materials.
"""


def nrt_displacements(damage_energy, displacement_energy):
    """Calculate the number of displaced atoms using the NRT model.

    The NRT model estimates the number of Frenkel pairs (vacancies and
    interstitials) produced when a Primary Knock-on Atom (PKA) receives
    a given damage energy. This is the standard model used in nuclear
    materials science.

    Parameters
    ----------
    damage_energy : float
        The damage energy deposited in the material, in eV.
        Must be positive.
    displacement_energy : float
        The threshold displacement energy of the material, in eV.
        Must be positive.

    Returns
    -------
    float
        The estimated number of displaced atoms (dimensionless).

    Raises
    ------
    ValueError
        If damage_energy or displacement_energy are not positive.

    Examples
    --------
    >>> nrt_displacements(1000.0, 40.0)
    10.0
    """
    if damage_energy <= 0:
        raise ValueError("damage_energy must be positive, "
                         f"got {damage_energy}")
    if displacement_energy <= 0:
        raise ValueError("displacement_energy must be positive, "
                         f"got {displacement_energy}")

    # 0.8 is the displacement efficiency factor from the NRT standard (ASTM E693)
    return 0.8 * damage_energy / (2.0 * displacement_energy)


def compute_dpa(flux, cross_section, damage_energy,
                displacement_energy, time):
    """Calculate the total DPA (displacements per atom).

    Computes the accumulated radiation damage in a material
    exposed to a neutron flux over a given time period.

    Parameters
    ----------
    flux : float
        Neutron flux in n/cm²/s. Must be positive.
    cross_section : float
        Neutron cross-section of the material in cm². Must be positive.
    damage_energy : float
        Average damage energy per collision in eV. Must be positive.
    displacement_energy : float
        Threshold displacement energy of the material in eV.
        Must be positive.
    time : float
        Irradiation time in seconds. Must be positive.

    Returns
    -------
    float
        The total DPA value (dimensionless).

    Raises
    ------
    ValueError
        If any parameter is not positive.

    Examples
    --------
    >>> compute_dpa(1e14, 1e-24, 1000.0, 40.0, 3.15e7)
    0.0025199999999999997
    """
    for name, value in [("flux", flux),
                        ("cross_section", cross_section),
                        ("damage_energy", damage_energy),
                        ("displacement_energy", displacement_energy),
                        ("time", time)]:
        if value <= 0:
            raise ValueError(f"{name} must be positive, got {value}")

    n_displaced = nrt_displacements(damage_energy, displacement_energy)
    return flux * cross_section * n_displaced * time