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

if __name__ == '__main__':
    board = generate_board(6,8,5,(4,5))
    print_board(board)
    print_board(board, opened=True)
    print_board(board, show_mines=True)


