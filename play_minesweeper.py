from cell import Cell 
from random import randint

def generate_board(rows: int, cols: int, num_mines: int, first_click_coords: tuple[int,int]) -> list[list[Cell]]:
    board = []
    # fill board with basic Cells
    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(Cell())
        board.append(new_row)

    # fill board with mines & adjacent_mines to its neighbors
    for _ in range(num_mines):
        found_place = False
        while not found_place:
            r = randint(0, rows - 1)
            c = randint(0, cols - 1)
            if (r, c) == first_click_coords or board[r][c].is_mine:
                continue
            found_place = True
            board[r][c].is_mine = True
            # set all around adjacent_mines +1
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if not (0 <= i <= rows - 1 and 0 <= j <= cols - 1):
                        continue
                    if (i, j) == (r, c):
                        continue
                    board[i][j].adjacent_mines += 1
    
    return board


if __name__ == '__main__':
    board = generate_board(5, 6, 14, (2, 3))
    print('game board')
    for line in board:
        print(*line, sep='')
