"""
nrtdamage - A Python tool to estimate radiation damage in materials
using the NRT (Norgett-Robinson-Torrens) model.
"""

__version__ = "0.1.0"
__author__ = "AniaOuiddir"

from nrtdamage.physics import nrt_displacements, compute_dpa
from nrtdamage.materials import get_material, list_materials

__all__ = [
    "nrt_displacements",
    "compute_dpa",
    "get_material",
    "list_materials",
]