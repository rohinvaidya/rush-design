import sys


def rush(x, y):
    """
    Display a square using '*' for borders and diagonals '/' '\\' for corners.

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    # Your implementation here
    pass
