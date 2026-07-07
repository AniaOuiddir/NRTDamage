"""Setup configuration for NRTDamage package."""

from setuptools import setup, find_packages

setup(
    name="nrtdamage",
    version="0.1.0",
    author="AniaOuiddir",
    author_email="ania.ania@studio.unibo.it",
    description=(
        "A Python tool to estimate radiation damage in materials "
        "using the NRT model (displacements per atom)"
    ),
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "nrtdamage = nrtdamage.cli:main",
        ]
    },
)