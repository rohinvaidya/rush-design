import sys


def rush(x, y):
    """
    Display a square outline using 'o' for corners and '-'/'|' for edges.

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    if y == 1:
        print('o' + '-' * (x - 2) + 'o' if x > 1 else 'o')
        return

    top_bottom = 'o' + '-' * (x - 2) + 'o' if x > 1 else 'o'
    middle = '|' + ' ' * (x - 2) + '|' if x > 1 else '|'

    print(top_bottom)
    for _ in range(y - 2):
        print(middle)
    print(top_bottom)
