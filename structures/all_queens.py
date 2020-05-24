"""
    Description: Eight queens puzzle
    Author: Larsen Close
    Version: In progress
    Outline and initial tests provided in class by Professor Dr. Beaty at MSU Denver

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


# start with solving this
SOLVE_ONE = True
# then worry about this if you have time
SOLVE_ALL = False


class AllQueens:
    """Class for the all queens problem"""



    def safe(self, x_1=0, y_1=0, x_2=0, y_2=0):
        """AllQueens function for safe placements"""
        return not (x_1 == x_2 or y_1 == y_2 or abs(x_2 - x_1) == abs(y_2 - y_1))

    def all_safe(self, row, col, placed):
        if not placed:
            return True
        for i in placed:
            if not self.safe(row, col, i[0], i[1]):
                return False
        return True

    def print_board(self, solution):
        """AllQueens function for printing board"""
        length = SIZE
        print('-' * length)

        a = [[' Q ' if (i, j) in solution else ' . '
            for j in range(length)]
            for i in range(length)]
        for i in a:
            print(''.join(i))

        print('-' * length)

    # '''
    #     size is the overall size of the problem we're solving.
    #     row is the row we're currently on, starting with 0.
    #     placed is a list of queens -- a list of tuples with (x,y) -- that
    #         have already been placed on the board.
    # '''

    def solve_one(self, size, row, placed):
        # if we're past the last row, return placed as it has the answer.
        # for each column
        # see if placing a queen at row and column is safe from all placed
        # queens.
        # if it is safe
        # make a recursive call with the next row and placed + (row, column)
        # if there was a solution with those parameters, return it.
        # return the empty list



        if row == size:
            return placed
        for col in range(0, size):
            if placed == []:
                return self.solve_one(size, row + 1, placed + [(row, col)])
            if self.all_safe(row, col, placed):
                return self.solve_one(size, row + 1, placed + [(row, col)])
            
        if len(placed) == size:
            return  placed

            
        return self.solve_one(size, row, [(row + 1, 1)])
        
        


    def new_solution(self, row, col, solutions):
        if solutions == []:
            return True
        for solution in solutions:
            if row == solution[0] and col == solution[1]:
                return False
        return True
            
        



    def solve_all(self, size, row, placed, solutions):
        """
        Function like solve one but accumulate all the solutions in the last
        argument.
        """
        
        for r in range(size):
            for c in range(size):
                if len(self.solve_one(size, row + 1, placed + [(r, c)])) == size:
                    solutions += self.solve_one(size, row + 1, placed + [(r, c)])
        
        return solutions
        
        

        # if len(placed) == size:
        #     return self.solve_all(size, row, [], solutions + (placed))
        # if row == size:
        #     return placed
        
        # for col in range(0, size):
        #     if placed == []:
        #         if self.new_solution(row, col, solutions):
        #             return self.solve_all(size, row + 1, placed + [(row, col)], solutions)
                
        #     if self.all_safe(row, col, placed):
        #         if self.new_solution(row, col, solutions):
        #             return self.solve_all(size, row + 1, placed + [(row, col)], solutions)
        
        # return solutions + (placed)             #self.solve_all(size, row, [], solutions + placed)


      





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
