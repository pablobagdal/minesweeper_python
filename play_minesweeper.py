from minesweeper_engine import *

from config import *

def welcome_menu():
    print('Welcome to Minesweeper')
    print('We expect you type correct values on the next questions:')

def input_values():
    global ROWS
    global COLS
    global TOTAL_MINES
    global TOTAL_SAFE_CELLS
    global BOARD
    global MINES_REMAIN
    global SAFE_CELLS_REMAIN
    global TOTAL_FLAGS
    global FLAGS_REMAIN
    # TODO validation of values
    ROWS = int(input('Write number of rows (2 - 15): '))
    COLS = int(input('Write number of cols (2 - 15): '))
    TOTAL_MINES = int(input(f'Write number of mines (1 - {ROWS * COLS - 1}): '))
    TOTAL_SAFE_CELLS = COLS * ROWS - TOTAL_MINES
    MINES_REMAIN = TOTAL_MINES
    SAFE_CELLS_REMAIN = TOTAL_SAFE_CELLS
    BOARD = create_empty_board(ROWS, COLS)
    TOTAL_FLAGS = TOTAL_MINES
    FLAGS_REMAIN = TOTAL_FLAGS

def all_commands() -> List[str]:
    commands = []
    for key in COMMANDS:
        commands.extend(COMMANDS[key])
    return commands

def input_command() -> tuple[str,int,int] | int:
    # иметь в виду, что пользователь вводит row col при счёте с 1, а не с нуля
    line = input('Write your command\n')
    words = line.split()
    if len(words) != 3:
        print(f'Your command consist of {len(words)} elements, must have only 3')
        return -1
    command, row, col = words

    if command not in all_commands():
        print('Wrong command')
        return -1
    # TODO check if digital
    if not (row.isdigit() and col.isdigit()):
        print(f'Error, row and column must be digital only')
        return -1
    
    row = int(row)
    col = int(col)
    if not (1 <= row <= ROWS and 1 <= col <= COLS):
        print(f'Error, row and column must be in intervals: row - [1, {ROWS}], col - [1, {COLS}]')
        return -1
    
    return (command, row - 1, col - 1)

def copy_flags(board_from: List[List[Cell]], board_to: List[List[Cell]]) -> None:
    for i in range(len(board_from)):
        for j in range(len(board_from[0])):
            if board_from[i][j].is_flagged:
                board_to[i][j].is_flagged = True

def decrease_cell_counters(cell: Cell):
    global MINES_REMAIN
    global SAFE_CELLS_REMAIN

    if cell.is_mine:
        MINES_REMAIN -= 1
    else:
        SAFE_CELLS_REMAIN -= 1

def unflag_cell(row: int, col: int):
    global FLAGS_REMAIN

    if BOARD[row][col].is_flagged:
        BOARD[row][col].is_flagged = False
        FLAGS_REMAIN += 1

def try_unreveal_around(row, col, recursive = True) -> None:
    cell = BOARD[row][col]
    queue = []
    if cell.adjacent_mines == 0:
        count = 0
        neighbors = neighbors_of(BOARD, (row, col))
        for x, y in neighbors:
            if not BOARD[x][y].is_revealed:
                queue.append((x, y))
                if BOARD[x][y].is_flagged:
                    unflag_cell(x, y)
                BOARD[x][y].is_revealed = True
    for x, y in queue:
        try_unreveal_around(x, y)
        


def open_cell(row, col):
    global BOARD

    if BOARD[row][col].is_flagged:
        print('Can\'t open flagged cell')
        return
    if BOARD[row][col].is_revealed:
        print('Can\'t open already revealed cell')
        return
    # первое открытие
    if SAFE_CELLS_REMAIN == TOTAL_SAFE_CELLS:
        new_board = generate_board(ROWS, COLS, TOTAL_MINES, (row, col))
        copy_flags(BOARD, new_board)
        BOARD = new_board

    cur_cell = BOARD[row][col]
    cur_cell.is_revealed = True
    decrease_cell_counters(cur_cell)
    try_unreveal_around(row, col)    
    # если рядом с выбранной клеткой рядом 0 бомб - открываются все соседние клетки и рекурсивно открываются соседи
    # if board[row - 1][col - 1].adjacent_mines == 0:

def flag_cell(row, col) -> None:
    global FLAGS_REMAIN

    cell = BOARD[row][col]

    if cell.is_revealed:
        print('You already opened the cell, you can\'t flag it')
    elif cell.is_flagged:
        unflag_cell(row, col)
    elif FLAGS_REMAIN == 0:
        print('You don\'t have flags anymore. To put new one unflag some cell')
    else:
        cell.is_flagged = True
        FLAGS_REMAIN -= 1

def do_command(command, row, col):
    if command in COMMANDS['open']:
        open_cell(row, col)
    elif  command in COMMANDS['flag']:
        flag_cell(row, col)
    else:
        print('undefined command')

def print_stats():
    print(f'Total cells: {TOTAL_SAFE_CELLS + TOTAL_MINES}')
    print(f'Safe cells remain: {SAFE_CELLS_REMAIN} / {TOTAL_SAFE_CELLS}')
    print(f'Mines: {TOTAL_MINES}')
    print(f'Flags remain: {FLAGS_REMAIN} / {TOTAL_FLAGS}')

def main():
    global BOARD
    
    welcome_menu()
    input_values()

    print_game_options()

    # main game board
    while MINES_REMAIN == TOTAL_MINES and SAFE_CELLS_REMAIN != 0:
        print_stats()
        print_board(BOARD)
        # print_board(BOARD, show_mines=True)
        command, row, col = input_command()
        do_command(command, row, col)
    
    
    print_board(BOARD, show_mines=True)
    if MINES_REMAIN < TOTAL_MINES:
        print('Game over :(')
    else:
        print('Congratulations, you win :)')

if __name__ == '__main__':
    main()

