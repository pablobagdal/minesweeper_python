from dataclasses import dataclass

@dataclass
class Cell:
    """Класс, представляющий ячейку"""
    is_mine: bool = False
    is_revealed: bool = False
    is_flagged: bool = False
    adjacent_mines: int = 0

    def __str__(self):
        if not self.is_revealed:
            return '#'
        if self.is_mine:
            return '*'
        return f'{self.adjacent_mines}'
    
    def revealed(self):
        if self.is_mine:
            return '*'
        return f'{self.adjacent_mines}'
