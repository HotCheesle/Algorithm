from collections import deque

class Board: 
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    def __init__(self, N, apple_list, turn_list):
        self.N = N
        self.apple = apple_list # set
        self.turn = turn_list   # deque
        self.time = 0
        self.direction = 1      # 위: 0, 오른쪽: 1, 아래: 2, 왼쪽: 3
        self.body = deque([])
        self.head = (0, 0)

    def move_foward(self): 
        nhead = (self.head[0]+Board.dr[self.direction], 
                 self.head[1]+Board.dc[self.direction])
        self.body.append(self.head)
        self.head = nhead
        self.time += 1
        crash = self.is_crashed()
        if nhead in self.apple: 
            self.apple.remove(nhead)
        else: 
            self.body.popleft()
        return crash
    
    def is_turn(self): 
        if self.turn: 
            if self.turn[0][0] == self.time: 
                self.direction += self.turn[0][1]
                self.direction %= 4
                self.turn.popleft()

    def is_crashed(self): 
        if self.head in self.body: 
            return self.time
        if (0 > self.head[0] or self.head[0] >= self.N
            or 0 > self.head[1] or self.head[1] >= self.N): 
            return self.time
        return False
    
N = int(input())
K = int(input())
apples = set()
for _ in range(K): 
    row, col = map(int, input().split())
    apples.add((row-1, col-1))
L = int(input())
turns = deque([])
for _ in range(L): 
    sec, dir = input().split()
    if dir == 'L': 
        d = 3
    else: 
        d = 1
    turns.append((int(sec), d))

snake = Board(N, apples, turns)
crash = False
while not crash: 
    crash = snake.move_foward()
    snake.is_turn()
print(crash)