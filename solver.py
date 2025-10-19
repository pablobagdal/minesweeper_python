# from minesweeper_engine import *
# from random import randint
# from collections import deque

# class Solver:
#     def solve_step(self, board: list[list[Cell]]) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
#         global BOARD
#         global SAFE_CELLS_REMAIN
#         global FLAGS_REMAIN
#         # board = []
#         safe_cells = set()
#         mines = set()

#         deq = deque()
#         # take all elements for the beginning
#         for i in range(ROWS):
#             for j in range(COLS):
#                 if board[i][j].is_revealed:
#                     deq.append((i, j))
#         while len(deq) != 0:
#             coord = deq[0]
#             neighbors = neighbors_of(board, coord)
#             if board[i][j].adjacent_mines == len(neighbors):

#             deq.remove(deq[0])






#         return (safe_cells, mines)

# if __name__ == '__main__':
#     ROWS = randint(MIN_LINES_COUNT, MAX_LINES_COUNT)
#     COLS = randint(MIN_LINES_COUNT, MAX_LINES_COUNT)
#     MIN_TOTAL_MINES = 1
#     MAX_TOTAL_MINES = ROWS * COLS - 9
#     TOTAL_MINES = randint(MIN_TOTAL_MINES, MAX_TOTAL_MINES)

#     first_coord = (randint(1, ROWS), randint(1, COLS))
#     BOARD = generate_board(ROWS, COLS, TOTAL_MINES, first_coord)
#     s = Solver()

#     res = s.solve_step()
#     safe_cells = res[0]
#     mines = res[1]
