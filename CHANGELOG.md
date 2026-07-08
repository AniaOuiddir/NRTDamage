# Changelog

All notable changes to NRTDamage will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-07-07

### Added
- Core NRT physics model (`nrtdamage/physics.py`)
  - `nrt_displacements()` function to compute displaced atoms
  - `compute_dpa()` function to compute total DPA
- Materials database (`nrtdamage/materials.py`)
  - 5 materials: iron, zirconium, tungsten, aluminum, copper
  - `get_material()` function to retrieve material properties
  - `list_materials()` function to list available materials
- Command-line interface (`nrtdamage/cli.py`)
  - `compute` subcommand to calculate DPA
  - `list` subcommand to list available materials
- Visualization module (`nrtdamage/plots.py`)
  - `plot_dpa_vs_time()` function
  - `plot_dpa_comparison()` function
- Test suite with 17 passing tests
- Full documentation in README.md
- JOSS paper description in paper.md