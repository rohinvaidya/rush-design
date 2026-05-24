import sys


def rush(x, y):
    """
    Display a square using '*' for borders and '/' '\' for corners.

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if x == 1:
        for _ in range(y):
            print('*')
        return

    if y == 1:
        print('*' * x)
        return

    print('/' + '*' * (x - 2) + '\\')
    for _ in range(y - 2):
        print('*' + ' ' * (x - 2) + '*')
    print('\\' + '*' * (x - 2) + '/')
