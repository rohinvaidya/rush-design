import sys


def rush(x, y):
    """
    Display a square using 'A' for top corners, 'C' for bottom corners, 'B' for borders.

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

    print('A' + 'B' * (x - 2) + 'A')
    for _ in range(y - 2):
        print('B' + ' ' * (x - 2) + 'B')
    print('C' + 'B' * (x - 2) + 'C')
