from collections import deque

class Board: 
    def __init__(self, N, M, x, y, board):
        self.N = N
        self.M = M
        self.dice = Dice(y, x)
        self.board = board

    def role_dice(self, direction): 
        cur = self.dice.get_coord()
        if cur[0] == 0 and direction == 3: return None
        elif cur[0] == self.N-1 and direction == 4: return None
        elif cur[1] == 0 and direction == 2: return None
        elif cur[1] == self.M-1 and direction == 1: return None
        bottom = self.dice.role(direction)
        cur = self.dice.get_coord()
        if self.board[cur[0]][cur[1]] == 0: 
            self.board[cur[0]][cur[1]] = bottom
        else: 
            self.dice.copy_to_dice(self.board[cur[0]][cur[1]])
            self.board[cur[0]][cur[1]] = 0
        return self.dice.get_top()

class Dice: 
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.horizon = deque([0, 0, 0, 0])  # 1 3 6 4
        self.vertical = deque([0, 0, 0, 0]) # 1 5 6 2

    def role(self, dir): 
        if dir == 1: 
            self.x += 1
            self.horizon.rotate(-1)
            self.vertical[0] = self.horizon[0]
            self.vertical[2] = self.horizon[2]
        elif dir == 2: 
            self.x -= 1
            self.horizon.rotate(1)
            self.vertical[0] = self.horizon[0]
            self.vertical[2] = self.horizon[2]
        elif dir == 3: 
            self.y -= 1
            self.vertical.rotate(1)
            self.horizon[0] = self.vertical[0]
            self.horizon[2] = self.vertical[2]
        elif dir == 4: 
            self.y += 1
            self.vertical.rotate(-1)
            self.horizon[0] = self.vertical[0]
            self.horizon[2] = self.vertical[2]
        return self.horizon[2]
    
    def get_coord(self): 
        return (self.y, self.x)
    
    def copy_to_dice(self, board): 
        self.vertical[2] = board
        self.horizon[2] = board

    def get_top(self): 
        return self.horizon[0]
    

N, M, x, y, K = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(N))
new_board = Board(N, M, x, y, board)
comm_list = list(map(int, input().split()))
for command in comm_list: 
    top = new_board.role_dice(command)
    if top is not None: 
        print(top)