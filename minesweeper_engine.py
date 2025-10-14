from random import randint
from dataclasses import dataclass
from typing import *
    
@dataclass
class Cell:
    is_mine: bool = False
    is_revealed: bool = False
    is_flagged: bool = False
    adjacent_mines: int = 0

    def __str__(self):
        if self.is_flagged:
            return 'F'
        if not self.is_revealed:
            return '#'
        if self.is_mine:
            return '*'
        return str(self.adjacent_mines)

    def revealed(self):
        if self.is_mine:
            return '*'
        return str(self.adjacent_mines)

def create_empty_board(rows: int, cols: int) -> List[List[Cell]]:
    board = []
    # fill board with basic Cells
    for _ in range(rows):
        new_row = []
        for _ in range(cols):
            new_row.append(Cell())
        board.append(new_row)
    return board

def neighbors_of(board: List[List[Cell]], coord: tuple[int, int]) -> set[tuple[int,int]]:
    neighbors = set()

    rows = len(board)
    cols = len(board[0])

    r = coord[0]
    c = coord[1]

    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if not (0 <= i <= rows - 1 and 0 <= j <= cols - 1) or (i, j) == (r, c):
                continue
            neighbors.add((i, j))
    
    return neighbors

def increase_adjacent_mines_around(board: List[List[Cell]], coord: tuple[int, int]) -> None:
    rows = len(board)
    cols = len(board[0])

    r = coord[0]
    c = coord[1]

    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if not (0 <= i <= rows - 1 and 0 <= j <= cols - 1):
                continue
            if (i, j) == (r, c):
                continue
            board[i][j].adjacent_mines += 1

def count_neighbors(board: List[List[Cell]], coord: tuple[int, int]) -> int:
    rows = len(board)
    cols = len(board[0])

    r = coord[0]
    c = coord[1]

    count = 0

    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if not (0 <= i <= rows - 1 and 0 <= j <= cols - 1):
                continue
            if (i, j) == (r, c):
                continue
            count += 1
    return count

def generate_board(rows: int, cols: int, num_mines: int, first_click_coords: tuple[int,int]) -> list[list[Cell]]:
    board = create_empty_board(rows, cols)

    safe_cells = {first_click_coords}
    print(neighbors_of(board, first_click_coords))
    # for cell in neighbors_of(board, first_click_coords):
    #     safe_cells.add(cell)

    # fill board with mines & adjacent_mines to its neighbors
    for _ in range(num_mines):
        found_place = False
        while not found_place:
            r = randint(0, rows - 1)
            c = randint(0, cols - 1)
            # if (r, c) == first_click_coords or board[r][c].is_mine:
            if (r, c) in safe_cells or board[r][c].is_mine:
                continue
            found_place = True
            board[r][c].is_mine = True
            # set all around adjacent_mines +1
            increase_adjacent_mines_around(board, (r, c))

    return board

def print_board(board, opened: bool = False, show_mines: bool = False):
    # TODO при размерах поля 10 и более будут съезжать цифры. Нужно выделить доп.строку и сделать выравнивание
    rows = len(board)
    cols = len(board[0])
    # first line of col nums
    print()
    print('  ', end='')
    for i in range(cols):
        print(f'{i + 1}', end='')
    print() 
    # board
    for i in range(rows):
        # row num
        print(f'{i + 1} ',end='')
        # board line
        line = []
        if opened:
            for cell in board[i]:
                line += cell.revealed()
        else:
            for cell in board[i]:
                if show_mines and cell.is_mine:
                    temp_cell = Cell()
                    temp_cell.is_revealed = True
                    temp_cell.is_mine = True
                    line += str(temp_cell)
                else:
                    line += str(cell)
        print(*line, sep='')
    print()

def print_with_open_mines(board):
    pass


def print_game_options():
    print('Game options')
    print('- `open <row> <col>` (или `o <row> <col>`): Open cell.')
    print('- `flag <row> <col>` (или `f <row> <col>`): set/unset flag.')

def print_empty_board(rows: int, cols: int) -> None:
    c = Cell()
    line = []
    for _ in range(cols):
        line.append(c)
    for _ in range(rows):
        print(*line)


# def generate_board(rows: int, cols: int, num_mines: int, first_coordniate: Tuple[int, int]) -> list[list[Cell]]:
#     total_cells = rows * cols


#     board = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             row.append(Cell())
#         board.append(row)

#     # Когда человек вводит например 5 строку и 4 столбец, то для питона это была 6 строка и 5 столбец, так как индекс с 0
#     first_human_row, first_human_col = first_coordniate
#     first_row, first_col = first_human_row - 1, first_human_col - 1

#     if not (0 <= first_row < rows and 0 <= first_col < cols):
#         raise ValueError('Координаты первой клетки не в границах поля')

#     safe_positions = set()
#     for neighbour_row in [first_row - 1, first_row, first_row + 1]:
#         for neighbour_col in [first_col - 1, first_col, first_col + 1]:

#             if neighbour_row >= 0 and neighbour_row < rows and \
#                     neighbour_col >= 0 and neighbour_col < cols:
#                 safe_positions.add((neighbour_row, neighbour_col))

#     positions = [(row, col) for row in range(rows) for col in range(cols) if (row, col) not in safe_positions]

#     if num_mines > total_cells - len(safe_positions):
#         raise ValueError('Колиечство мин не может быть больше количества ячеек поля')

#     mine_positions = set(random.sample(positions, num_mines))

#     for row, col in mine_positions:
#         cell = board[row][col]
#         cell.is_mine = True

#     calculate_adjacent_mines(board)

#     return board

# def print_open_board(board: list[list[Cell]]) -> None:
#     for line in board:
#         for cell in line:
#             print(cell.revealed(), end='')
#         print()

# def create_empty_board(rows: int, cols: int) -> list[list[Cell]]:
#     board = []
#     for i in range(rows):
#         line = []
#         for g in range(cols):
#             line.append(Cell())
#         board.append(line)
#     return board

if __name__ == '__main__':
    board = generate_board(6,8,5,(4,5))
    print_board(board)
    print_board(board, opened=True)
    print_board(board, show_mines=True)


