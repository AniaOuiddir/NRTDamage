---
title: 'NRTDamage: A Python library for estimating radiation damage in materials using the NRT model'
tags:
  - Python
  - nuclear physics
  - radiation damage
  - materials science
  - displacements per atom
authors:
  - name: Ania Ouiddir
    affiliation: 1
affiliations:
  - name: University of Bologna, Italy
    index: 1
date: 2026-07-07
---

# Summary

Radiation damage in materials is a critical concern in the design and
operation of nuclear reactors, particle accelerators, and space systems.
When energetic particles such as neutrons interact with a solid material,
they can displace atoms from their equilibrium lattice positions, creating
defects that degrade the mechanical and physical properties of the material
over time.

`NRTDamage` is a Python library and command-line tool that implements the
Norgett-Robinson-Torrens (NRT) standard model to estimate the number of
atomic displacements produced in a material under irradiation. The key
output quantity is the **displacement per atom (DPA)**, which is the
standard metric used internationally to quantify radiation damage in
nuclear materials.

# Statement of Need

The NRT model is the internationally accepted standard for estimating
radiation damage in materials, adopted by the ASTM and used in nuclear
engineering codes worldwide. Despite its importance, no simple,
well-documented, and easily installable Python implementation existed.

`NRTDamage` fills this gap by providing:

- A clean Python API for computing DPA in common nuclear materials
- A command-line interface for quick calculations
- A built-in database of material properties
- Full test coverage and documentation

# Physics

The NRT model estimates the number of displaced atoms as:

$$N_{dpa} = \frac{0.8 \cdot T_{dam}}{2 \cdot E_d}$$

Where:

- $T_{dam}$ is the damage energy deposited in the material (eV)
- $E_d$ is the threshold displacement energy of the material (eV)
- $0.8$ is an empirical efficiency factor

The total DPA accumulated in a material is then:

$$DPA = \phi \cdot \sigma \cdot N_{dpa} \cdot t$$

Where $\phi$ is the neutron flux, $\sigma$ is the cross-section, and
$t$ is the irradiation time.

# References

Norgett, M.J., Robinson, M.T., Torrens, I.M. (1975). A proposed method
of calculating displacement dose rates. *Nuclear Engineering and Design*,
33(1), 50-54.