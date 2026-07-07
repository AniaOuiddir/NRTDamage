"""
materials.py - Database of materials for NRT damage calculations.

This module provides displacement energies and neutron cross-sections
for common nuclear and aerospace materials.
"""

MATERIALS = {
    "iron": {
        "symbol": "Fe",
        "displacement_energy": 40.0,
        "cross_section": 2.56e-24,
        "description": "Iron - common structural steel component",
    },
    "zirconium": {
        "symbol": "Zr",
        "displacement_energy": 40.0,
        "cross_section": 6.46e-24,
        "description": "Zirconium - used in nuclear fuel cladding",
    },
    "tungsten": {
        "symbol": "W",
        "displacement_energy": 90.0,
        "cross_section": 2.37e-24,
        "description": "Tungsten - used in fusion reactor components",
    },
    "aluminum": {
        "symbol": "Al",
        "displacement_energy": 25.0,
        "cross_section": 1.41e-24,
        "description": "Aluminum - used in aerospace structures",
    },
    "copper": {
        "symbol": "Cu",
        "displacement_energy": 30.0,
        "cross_section": 3.78e-24,
        "description": "Copper - used in electrical components",
    },
}


def get_material(name):
    """Retrieve material properties by name.

    Parameters
    ----------
    name : str
        Name of the material (case-insensitive).

    Returns
    -------
    dict
        Dictionary containing material properties.

    Raises
    ------
    ValueError
        If the material is not found in the database.

    Examples
    --------
    >>> mat = get_material("iron")
    >>> mat["displacement_energy"]
    40.0
    """
    name = name.lower().strip()
    if name not in MATERIALS:
        available = ", ".join(MATERIALS.keys())
        raise ValueError(
            f"Material '{name}' not found. "
            f"Available materials: {available}"
        )
    return MATERIALS[name]


def list_materials():
    """Return a list of all available material names.

    Returns
    -------
    list of str
        Sorted list of available material names.

    Examples
    --------
    >>> materials = list_materials()
    >>> "iron" in materials
    True
    """
    return sorted(MATERIALS.keys())