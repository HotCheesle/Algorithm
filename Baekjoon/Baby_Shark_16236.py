from collections import deque

class Shark(): 
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.size = 2
        self.gauge = 0
        self.time = 0

    def is_grow(self): 
        if self.gauge == self.size: 
            self.size += 1
            self.gauge = 0

    def move_eat(self, row, col, dis, area): 
        area[self.row][self.col] = 0
        area[row][col] = 9
        self.row = row
        self.col = col
        self.gauge += 1
        self.time += dis


def scan(shark): 
    queue = deque([(shark.row, shark.col, 0)])
    visited = set()
    visited.add((shark.row, shark.col))
    while queue: 
        cur = queue.popleft()
        for r, c in zip(dr, dc): 
            if 0 <= cur[0]+r < N and 0 <= cur[1]+c < N and (cur[0]+r, cur[1]+c) not in visited: 
                if water[cur[0]+r][cur[1]+c] == 0 or water[cur[0]+r][cur[1]+c] == shark.size: 
                    visited.add((cur[0]+r, cur[1]+c))
                    queue.append((cur[0]+r, cur[1]+c, cur[2]+1))
                elif water[cur[0]+r][cur[1]+c] < shark.size: 
                    return cur[0]+r, cur[1]+c, cur[2]+1
    else:
        return -1, -1, -1

N = int(input())
water = list(list(map(int, input().split())) for _ in range(N))
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
for row in range(N): 
    for col in range(N): 
        if water[row][col] == 9: 
            s_row, s_col = row, col
            break
baby_shark = Shark(s_row, s_col)
tg_row, tg_col, tg_dis = scan(baby_shark)
while tg_row != -1: 
    baby_shark.move_eat(tg_row, tg_col, tg_dis, water)
    baby_shark.is_grow()
    tg_row, tg_col, tg_dis = scan(baby_shark)
print(baby_shark.time)