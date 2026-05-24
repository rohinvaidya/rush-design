import sys


def rush(x, y):
    """
    Display a square using 'A' for top-left corner, 'B' for borders, 'C' for bottom-left corner.

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    # Your implementation here
    pass
