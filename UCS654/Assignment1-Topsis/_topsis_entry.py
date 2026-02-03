"""Entry point for the topsis console script (package name has a hyphen)."""
from importlib import import_module


def main():
    mod = import_module("102303812-topsis.topsis")
    mod.main()
