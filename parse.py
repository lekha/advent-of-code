"""
Functions to parse Advent of Code input.
"""
from typing import Iterable


def read_file(file_path: str) -> Iterable[str]:
    """Read file contents. Remove newline characters."""
    with open(file_path) as opened_file:
        contents = opened_file.readlines()
    return [line.strip() for line in contents]

