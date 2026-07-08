Welcome to NRTDamage's documentation!
======================================

.. image:: https://github.com/AniaOuiddir/NRTDamage/actions/workflows/tests.yml/badge.svg

**NRTDamage** is a Python library and command-line tool to estimate 
radiation-induced atomic displacement damage in nuclear materials 
using the NRT (Norgett-Robinson-Torrens) model.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api

Installation
------------

.. code-block:: bash

   git clone https://github.com/AniaOuiddir/NRTDamage.git
   cd NRTDamage
   pip install -e .

Quick Start
-----------

.. code-block:: python

   from nrtdamage.physics import compute_dpa
   from nrtdamage.materials import get_material

   mat = get_material("iron")
   dpa = compute_dpa(
       flux=1e14,
       cross_section=mat["cross_section"],
       damage_energy=1000.0,
       displacement_energy=mat["displacement_energy"],
       time=3.15e7,
   )
   print(f"DPA: {dpa:.4e}")

API Reference
-------------

.. toctree::
   :maxdepth: 2

   nrtdamage

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`