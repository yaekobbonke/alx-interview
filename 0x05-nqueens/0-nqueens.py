#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if placing a queen at the given position
    (row, col) on the board is safe.
    """
    # Check the row
    for c in range(col):
        if board[row][c] == 'Q':
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    """
    Solve the N-queens problem and return a list of all possible solutions.

    Args:
        N (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of solutions, where each solution is represented as a list
              of strings, with each string representing a row on the chessboard.

    """
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_util(board, 0, N, solutions)
    return solutions


def solve_util(board, col, N, solutions):
    """
    A recursive utility function to solve the N-queens problem.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column being considered.
        N (int): The size of the chessboard and the number of queens.
        solutions (list): A list to store the solutions.

    """
    if col == N:
        # Found a solution, add it to the list of solutions
        solutions.append([''.join(row) for row in board])
        return

    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_util(board, col + 1, N, solutions)
            board[row][col] = '.'


def print_solutions(solutions):
    """
    Print the solutions to the N-queens problem.

    Args:
        solutions (list): A list of solutions,
        where each solution is represented
                          as a list of strings,
                          with each string representing a row
                          on the chessboard.
    """
    for solution in solutions:
        for row in solution:
            print(row)
        print()


def main():
    """entry point"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == '__main__':
    main()
