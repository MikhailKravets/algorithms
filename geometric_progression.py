
def chess_progression(row: int, col: int) -> int:
    q = 2
    max_side = 8

    if row == 1:
        elem = col
    else:
        elem = (row - 1) * max_side + col

    return 1 * q ** (elem - 1)


if __name__ == '__main__':
    print(chess_progression(8, 8))
