from game import GameBoard

class Algorithm:
    def __init__(self, pos: tuple[int, int], board: GameBoard):
        self.x = pos[0]
        self.y = pos[1]
        self.board = board
        self.board.fill_cell(self.x, self.y)

    def is_valid(self, x: int, y: int): 
        return (0 <= x < self.board.width) and (0 <= y < self.board.height) and not self.board.get_cell(x, y)

    # TODO: Add support for additional algorithms
    def run(self) -> bool:
        return False

class Greedy(Algorithm):
    # moves to the next available spot
    def run(self) -> bool:
        candidates = [(self.x + 1, self.y), 
                      (self.x - 1, self.y),
                      (self.x, self.y + 1),
                      (self.x, self.y - 1)]
        # check all possible coordinates to find the first empty space and move there
        for x, y in candidates:
            if self.is_valid(x, y):
                self.board.fill_cell(x, y)
                self.x = x
                self.y = y
                return True
        return False
    
class TunnelVis(Algorithm):
    def __init__(self, pos, board):
        super().__init__(pos, board)
        self.direction = self.next_direct()
    
    # greedily sets next direction
    def next_direct(self) -> str | None:
        candidates = [(self.x + 1, self.y, 'right'), 
                      (self.x - 1, self.y, 'left'),
                      (self.x, self.y + 1, 'north'),
                      (self.x, self.y - 1, 'south')]
        for x, y, dir in candidates:
            if self.is_valid(x, y):
                return dir
        return None
    
    def run(self):
        next = (-1, -1)
        match self.direction:
            case 'right': 
                next = (self.x + 1, self.y)
            case 'left':
                next = (self.x - 1, self.y)
            case 'north':
                next = (self.x , self.y + 1)
            case 'south':
                next = (self.x, self.y - 1)
        x, y = next
        if (self.is_valid(x, y)):
            self.x = x
            self.y = y
            self.board.fill_cell(x, y)
            return True
        self.direction = self.next_direct()
        if not self.direction:
            return False
        return self.run()


