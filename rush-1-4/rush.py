import sys


def rush(x, y):
    """
    Display a square using 'A' for left corners, 'C' for right corners, 'B' for borders.
    Top and bottom rows are identical: A + B's + C.

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

    top_bottom = 'A' + 'B' * (x - 2) + 'C'
    middle = 'B' + ' ' * (x - 2) + 'B'

    print(top_bottom)
    for _ in range(y - 2):
        print(middle)
    print(top_bottom)
