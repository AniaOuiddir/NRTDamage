"""
cli.py - Command line interface for NRTDamage.

This module provides the command line interface to estimate
radiation damage in materials using the NRT model.
"""

import argparse
import sys

from nrtdamage.physics import compute_dpa
from nrtdamage.materials import get_material, list_materials


def create_parser():
    """Create and return the argument parser for NRTDamage.

    Returns
    -------
    argparse.ArgumentParser
        The configured argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="nrtdamage",
        description=(
            "Estimate radiation damage in materials using "
            "the NRT (Norgett-Robinson-Torrens) model."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    # --- compute command ---
    compute_parser = subparsers.add_parser(
        "compute",
        help="Compute DPA for a given material and irradiation conditions.",
    )
    compute_parser.add_argument(
        "--material", "-m",
        type=str,
        required=True,
        help="Material name (e.g. iron, zirconium, tungsten).",
    )
    compute_parser.add_argument(
        "--flux", "-f",
        type=float,
        required=True,
        help="Neutron flux in n/cm2/s.",
    )
    compute_parser.add_argument(
        "--time", "-t",
        type=float,
        required=True,
        help="Irradiation time in seconds.",
    )
    compute_parser.add_argument(
        "--damage-energy", "-e",
        type=float,
        default=1000.0,
        help="Average damage energy per collision in eV (default: 1000.0).",
    )

    # --- list command ---
    subparsers.add_parser(
        "list",
        help="List all available materials.",
    )

    return parser


def run_compute(args):
    """Execute the compute command.

    Parameters
    ----------
    args : argparse.Namespace
        Parsed command line arguments.
    """
    try:
        material = get_material(args.material)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        dpa = compute_dpa(
            flux=args.flux,
            cross_section=material["cross_section"],
            damage_energy=args.damage_energy,
            displacement_energy=material["displacement_energy"],
            time=args.time,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Material:         {material['description']}")
    print(f"Neutron flux:     {args.flux:.2e} n/cm2/s")
    print(f"Irradiation time: {args.time:.2e} s")
    print(f"Damage energy:    {args.damage_energy:.1f} eV")
    print(f"DPA:              {dpa:.4e}")


def run_list():
    """Execute the list command."""
    print("Available materials:")
    for name in list_materials():
        mat = __import__(
            "nrtdamage.materials", fromlist=["MATERIALS"]
        ).MATERIALS[name]
        print(f"  {name:<12} ({mat['symbol']}) - {mat['description']}")


def main():
    """Main entry point for the NRTDamage CLI."""
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "compute":
        run_compute(args)
    elif args.command == "list":
        run_list()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()