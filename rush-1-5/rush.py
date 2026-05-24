import sys


def rush(x, y):
    """
    Display a square using 'A', 'B', 'C' where the bottom row is the horizontal
    mirror of the top row.

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if x == 1:
        for _ in range(y):
            print('B')
        return

    if y == 1:
        print('B' * x)
        return

    top = 'A' + 'B' * (x - 2) + 'C'
    middle = 'B' + ' ' * (x - 2) + 'B'
    bottom = top[::-1]

    print(top)
    for _ in range(y - 2):
        print(middle)
    print(bottom)
