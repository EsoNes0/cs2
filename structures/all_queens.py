"""
    Description: Eight queens puzzle
    Author: Larsen Close
    Version: In progress
    Outline and initial tests provided in class by
    Professor Dr. Beaty at MSU Denver.

    The eight queens puzzle is the problem of placing eight chess queens on
    an 8×8 chessboard so that no two queens threaten each other. Thus, a
    solution requires that no two queens share the same row, column, or
    diagonal. The eight queens puzzle is an example of the more general n
    queens problem of placing n non-attacking queens on an n×n chessboard,
    for which solutions exist for all natural numbers n with the exception
    of n=2 and n=3.
    https://en.wikipedia.org/wiki/Eight_queens_puzzle
"""

from sys import argv


# runs method to find one solution
SOLVE_ONE = True
# runs method to find all solutions
SOLVE_ALL = True


class AllQueens:
    """Class for the all queens problem"""

    def safe(self, x_1=0, y_1=0, x_2=0, y_2=0):
        """AllQueens method to check single safe placement"""
        return not (
            x_1 == x_2 or y_1 == y_2 or abs(
                x_2 - x_1) == abs(y_2 - y_1))

    def all_safe(self, row, col, placed):
        """AllQueens method to check safety against all placements"""
        if not placed or placed == []:
            return True
        for i in placed:
            if not self.safe(row, col, i[0], i[1]):
                return False
        return True

    def print_board(self, solution):
        """AllQueens function for printing board"""
        length = SIZE
        print('-' * length)

        a = [[' Q ' if (i, j) in solution else ' ~ '
              for j in range(length)]
             for i in range(length)]
        for i in a:
            print(''.join(i))

        print('-' * length)

    def solve_one(self, size, row, placed):
        """
        Function to find one solution the the n queens problem and return it
        """

        if row >= size:
            return placed

        for col in range(0, size):
            if self.all_safe(row, col, placed):
                solution = self.solve_one(size, row + 1, placed + [(row, col)])
                if len(solution) == size:
                    return solution

        return []

    def solve_all(self, size, row, placed, solutions):
        """
        Function like solve one but accumulate all the solutions in the last
        argument.
        """

        if row >= size:
            solutions += [placed]
            return solutions

        for col in range(0, size):
            if self.all_safe(row, col, placed):
                solutions = self.solve_all(
                    size, row + 1, placed + [(row, col)], solutions)
                if len(placed) == size:
                    return solutions
        return solutions


if __name__ == "__main__":
    SIZE = 8 if len(argv) == 1 else int(argv[1])

    if SOLVE_ONE:
        queen = AllQueens()
        queen.print_board(queen.solve_one(SIZE, 0, []))

    if SOLVE_ALL:
        queens = AllQueens()
        SOLUTIONS = queens.solve_all(SIZE, 0, [], [])
        print("there are", len(SOLUTIONS), "solutions for the",
              SIZE, "queens problem:")
        for solve in SOLUTIONS:
            queens.print_board(solve)
        for solve in SOLUTIONS:
            print(solve)
