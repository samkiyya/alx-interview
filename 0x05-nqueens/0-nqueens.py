#!/usr/bin/python3
"""N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP)"""
import sys


class NQueen:
    """Class for solving the N-Queen Problem"""

    def __init__(self, n):
        """Initialize the board size and solution storage"""
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """
        Check if the k-th queen can be placed in the i-th column.
        Ensures no queens are in the same row or diagonal.
        """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def n_queen(self, k):
        """
        Attempts to place queens on the board starting from the k-th queen.
        Uses recursion and backtracking to find all solutions.
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = [[j - 1, self.x[j] - 1] for j in range(1, self.n + 1)]
                    self.res.append(solution)
                else:
                    self.n_queen(k + 1)
        return self.res


# Main script execution
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

# Initialize and solve the N-Queens problem
queen = NQueen(N)
solutions = queen.n_queen(1)

# Output each solution in the specified format
for solution in solutions:
    print(solution)
