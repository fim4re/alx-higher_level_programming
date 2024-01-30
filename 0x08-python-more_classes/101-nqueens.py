#!/usr/bin/python3
"""Solves N-queens puzzle.

Attributes:
    brd: list of lists chessboard.
    solt: list of lists solutions.
queen must be placed on the chessboard.
"""
import sys


def init_brd(m):
    """def an `n`x`n` sized chessboard."""
    brd = []
    [brd.append([]) for j in range(m)]
    [rows.append(' ') for j in range(m) for rows in brd]
    return (brd)


def brd_dpcopy(brd):
    """deepcopy of chessboard."""
    if isinstance(brd, list):
        return list(map(brd_dpcopy, brd))
    return (brd)


def get_solt(brd):
    """Return the list of a solved chessboard."""
    solt = []
    for d in range(len(brd)):
        for x in range(len(brd)):
            if brd[d][x] == "Q":
                solt.append([d, x])
                break
    return (solt)


def _x_out(brd, rows, cols):
    """spots on a chessboard.

    Args:
        brd: current chessboard.
        rows: rows queen was last played.
        cols: column queen was last played.
    """

    for x in range(cols + 1, len(brd)):
        brd[rows][x] = "x"
    for x in range(cols - 1, -1, -1):
        brd[rows][x] = "x"
    for x in range(rows + 1, len(brd)):
        brd[d][cols] = "x"
    for d in range(rows - 1, -1, -1):
        brd[d][cols] = "x"
    for d in range(rows + 1, len(brd)):
        if x >= len(brd):
            break
        brd[d][x] = "x"
        x += 1
    for d in range(rows - 1, -1, -1):
        if x < 0:
            break
        brd[d][x]
        x -= 1
    for d in range(rows - 1, -1, -1):
        if x >= len(brd):
            break
        brd[d][x] = "x"
        x += 1
    for d in range(rows + 1, len(brd)):
        if x < 0:
            break
        brd[d][x] = "x"
        x -= 1


def rec_solve(brd, rows, queens, solt):
    """solve an N-queens puzzle.

        Args:
                brd: working chessboard.
                row: current working row.
                queens: current number of placed.
                solt: list of solutions.
        Returns: solt """
    if queens == len(brd):
        solt.append(get_solt(brd))
        return (solt)

    for x in range(len(brd)):
        if brd[rows][x] == " ":
            tmp_brd = brd_dpcopy(brd)
            tmp_brd[rows][x] = "Q"
            _x_out(tmp_brd, rows, x)
            solt = rec_solve(tmp_brd, rows + 1, queens + 1, solt)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = init_brd(int(sys.argv[1]))
    solt = rec_solve(brd, 0, 0, [])
    for s in solt:
        print(s)
