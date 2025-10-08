from minesweeper_engine import *

if __name__ == '__main__':
    print('Welcome to Minesweeper')
    print('We expect you type correct values on the next questions:')
    rows = int(input('Write number of rows (2 - 15): '))
    cols = int(input('Write number of cols (2 - 15): '))
    total_mines = int(input(f'Write number of mines (1 - {rows * cols - 1}): '))
    # TODO validation of values

    print_game_options()

    total_safe_cells = cols * rows - total_mines
    safe_cells_remain = total_safe_cells
    mines_remain = total_mines

    # debug
    open_board_printed = False

    while safe_cells_remain != 0 and mines_remain == total_mines:
        if safe_cells_remain == total_safe_cells:
            print_empty_board(rows, cols)
        else:
            if not open_board_printed:
                print_open_board(board)
                open_board_printed = True
            print_board(board)

        line = input('Write your command\n')

        #TODO проверка, что введена команда формата слово число число
        
        command, row, col = line.split(' ')
        row = int(row)
        col = int(col)

        if command in ['open', 'o']:
            #TODO предусмотреть ввод некорректных чисел
            if safe_cells_remain == total_safe_cells:
                board = generate_board(rows, cols, total_mines, (row, col))
                board[row-1][col-1].is_revealed = True
                safe_cells_remain -= 1

            elif not board[row-1][col-1].is_revealed:
                # открывается новая клетка
                board[row-1][col-1].is_revealed = True
                # обработка типа ячейки
                if board[row-1][col-1].is_mine:
                    mines_remain -= 1
                else:
                    safe_cells_remain -= 1

            else:
                print('This cell is already revealed')
            
            # если рядом с выбранной клеткой рядом 0 бомб - открываются все соседние клетки и рекурсивно открываются соседи
            # if board[row - 1][col - 1].adjacent_mines == 0:

        elif command in ['flag', 'f']:
            #TODO предусмотреть ввод некорректных чисел
            #TODO учесть лимит флагов
            pass
        else:
            print('undefined command')
            continue

    
    
    print_board(board)
    if mines_remain < total_mines:
        print('Game over :(')
    else:
        print('Congratulations, you win :)')

