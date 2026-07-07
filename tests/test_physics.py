"""
test_physics.py - Tests for the NRT physics module.
"""

import pytest
from nrtdamage.physics import nrt_displacements, compute_dpa


def test_nrt_displacements_typical_case():
    """Test NRT formula with typical iron parameters.

    GIVEN: a damage energy of 1000 eV and displacement energy of 40 eV
    WHEN: nrt_displacements is called
    THEN: the result should be 10.0 displaced atoms
    """
    result = nrt_displacements(1000.0, 40.0)
    assert result == pytest.approx(10.0)


def test_nrt_displacements_scales_with_damage_energy():
    """Test that NRT result scales linearly with damage energy.

    GIVEN: two damage energies where one is double the other
    WHEN: nrt_displacements is called for both
    THEN: the result should also be double
    """
    result_1 = nrt_displacements(1000.0, 40.0)
    result_2 = nrt_displacements(2000.0, 40.0)
    assert result_2 == pytest.approx(2 * result_1)


def test_nrt_displacements_raises_for_zero_damage_energy():
    """Test that ValueError is raised for zero damage energy.

    GIVEN: a damage energy of 0
    WHEN: nrt_displacements is called
    THEN: a ValueError should be raised
    """
    with pytest.raises(ValueError):
        nrt_displacements(0.0, 40.0)


def test_nrt_displacements_raises_for_negative_damage_energy():
    """Test that ValueError is raised for negative damage energy.

    GIVEN: a negative damage energy
    WHEN: nrt_displacements is called
    THEN: a ValueError should be raised
    """
    with pytest.raises(ValueError):
        nrt_displacements(-100.0, 40.0)


def test_nrt_displacements_raises_for_zero_displacement_energy():
    """Test that ValueError is raised for zero displacement energy.

    GIVEN: a displacement energy of 0
    WHEN: nrt_displacements is called
    THEN: a ValueError should be raised
    """
    with pytest.raises(ValueError):
        nrt_displacements(1000.0, 0.0)


def test_compute_dpa_returns_positive_value():
    """Test that compute_dpa returns a positive value.

    GIVEN: valid physical parameters for iron
    WHEN: compute_dpa is called
    THEN: the result should be positive
    """
    result = compute_dpa(
        flux=1e14,
        cross_section=2.56e-24,
        damage_energy=1000.0,
        displacement_energy=40.0,
        time=3.15e7,
    )
    assert result > 0


def test_compute_dpa_scales_with_flux():
    """Test that DPA scales linearly with neutron flux.

    GIVEN: two flux values where one is double the other
    WHEN: compute_dpa is called for both
    THEN: the DPA should also be double
    """
    dpa_1 = compute_dpa(1e14, 2.56e-24, 1000.0, 40.0, 3.15e7)
    dpa_2 = compute_dpa(2e14, 2.56e-24, 1000.0, 40.0, 3.15e7)
    assert dpa_2 == pytest.approx(2 * dpa_1)


def test_compute_dpa_raises_for_negative_flux():
    """Test that ValueError is raised for negative flux.

    GIVEN: a negative neutron flux
    WHEN: compute_dpa is called
    THEN: a ValueError should be raised
    """
    with pytest.raises(ValueError):
        compute_dpa(-1e14, 2.56e-24, 1000.0, 40.0, 3.15e7)