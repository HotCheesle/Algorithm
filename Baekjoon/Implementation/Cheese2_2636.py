from collections import deque

class Board: 
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    def __init__(self, N, M, board) -> None:
        self.N = N
        self.M = M
        self.queue = deque([])
        self.visited = set()
        self.board = board
        self.time = 0
        self.cnt = 1

    def melting(self): 
        self.queue.append((0, 0))
        self.visited.clear()
        while self.queue: 
            now = self.queue.popleft()
            if now in self.visited: 
                continue
            self.visited.add(now)
            for r, c in zip(Board.dr, Board.dc): 
                nrow, ncol = now[0]+r, now[1]+c
                if (0 <= nrow < self.N and 0 <= ncol < self.M 
                    and (nrow, ncol) not in self.visited): 
                    if self.board[nrow][ncol] == 0: 
                        self.queue.append((nrow, ncol))
                    else: 
                        self.board[nrow][ncol] += 1
        
        self.cnt = 0
        for row in range(1, self.N-1): 
            for col in range(1, self.M-1): 
                if self.board[row][col] > 1: 
                    self.board[row][col] = 0
                elif self.board[row][col] == 1: 
                    self.cnt += 1
        self.time += 1

        return self.cnt, self.time
    
N, M = map(int, input().split())
cheeses = list(list(map(int, input().split())) for _ in range(N))
cnt = 0
for r in range(N): 
    for c in range(M):
        if cheeses[r][c] == 1: 
            cnt += 1
freezer = Board(N, M, cheeses)
pcnt, time = 0, 0
while cnt != 0: 
    pcnt = cnt
    cnt, time = freezer.melting()
print(time)
print(pcnt)