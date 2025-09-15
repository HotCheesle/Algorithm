class Board: 
    def __init__(self, N, M, x, y):
        self.N = N
        self.M = M
        self.dice = Dice(x, y)

class Dice: 
    def __init__(self, x, y):
        self.x = x
        self.y = y