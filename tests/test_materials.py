"""
test_materials.py - Tests for the materials database module.
"""

import pytest
from nrtdamage.materials import get_material, list_materials, MATERIALS


def test_get_material_iron():
    """Test that iron properties are correctly retrieved.

    GIVEN: the material name 'iron'
    WHEN: get_material is called
    THEN: the displacement energy should be 40.0 eV
    """
    mat = get_material("iron")
    assert mat["displacement_energy"] == pytest.approx(40.0)


def test_get_material_case_insensitive():
    """Test that material lookup is case-insensitive.

    GIVEN: the material name 'Iron' with uppercase I
    WHEN: get_material is called
    THEN: it should return the same result as 'iron'
    """
    mat_lower = get_material("iron")
    mat_upper = get_material("Iron")
    assert mat_lower == mat_upper


def test_get_material_raises_for_unknown_material():
    """Test that ValueError is raised for unknown materials.

    GIVEN: an unknown material name
    WHEN: get_material is called
    THEN: a ValueError should be raised
    """
    with pytest.raises(ValueError):
        get_material("unobtainium")


def test_get_material_returns_dict():
    """Test that get_material returns a dictionary.

    GIVEN: a valid material name
    WHEN: get_material is called
    THEN: the result should be a dictionary
    """
    mat = get_material("iron")
    assert isinstance(mat, dict)


def test_get_material_has_required_keys():
    """Test that all materials have the required keys.

    GIVEN: any valid material name
    WHEN: get_material is called
    THEN: the result should contain all required keys
    """
    required_keys = {"symbol", "displacement_energy",
                     "cross_section", "description"}
    for name in list_materials():
        mat = get_material(name)
        assert required_keys.issubset(mat.keys())


def test_list_materials_returns_list():
    """Test that list_materials returns a list.

    GIVEN: no input
    WHEN: list_materials is called
    THEN: the result should be a list
    """
    result = list_materials()
    assert isinstance(result, list)


def test_list_materials_contains_iron():
    """Test that iron is in the materials list.

    GIVEN: no input
    WHEN: list_materials is called
    THEN: 'iron' should be in the result
    """
    assert "iron" in list_materials()


def test_list_materials_is_sorted():
    """Test that list_materials returns a sorted list.

    GIVEN: no input
    WHEN: list_materials is called
    THEN: the result should be sorted alphabetically
    """
    result = list_materials()
    assert result == sorted(result)


def test_all_displacement_energies_are_positive():
    """Test that all displacement energies in the database are positive.

    GIVEN: the full materials database
    WHEN: checking displacement energies
    THEN: all values should be positive
    """
    for name, props in MATERIALS.items():
        assert props["displacement_energy"] > 0