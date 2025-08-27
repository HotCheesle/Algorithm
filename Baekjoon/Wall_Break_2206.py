from collections import deque

def BFS(st_r, st_c, distance): 
    queue[0] = (st_r, st_c, distance)
    visited.add((st_r, st_c))
    front, rear = 0, 1
    while front != rear: 
        cur = queue[front]
        front += 1
        for r, c in zip(dr, dc): 
            row, col, dis = cur[0]+r, cur[1]+c, cur[2]+1
            if 0 <= row < R and 0 <= col < C and (row, col) not in visited: 
                if maze[row][col] == '0': 
                    visited.add((row, col))
                    queue[rear] = (row, col, dis)
                    rear += 1
                    d_map[row][col] = dis
    return rear

R, C = map(int, input().split())
maze = list(list(input()) for _ in range(R))
d_map = list(list(0 for _ in range(C)) for _ in range(R))
d_map[0][0] = 100001
#queue = deque([])
queue = [(0, 0, 0) for _ in range(50000)]
visited = set()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
dr2, dc2 = [-2, 0, 2, 0], [0, 2, 0, -2]

length = BFS(0, 0, 100001)

if d_map[R-1][C-1] != 0: 
    max_shrink = 0
    for idx in range(length):
        row, col, distance = queue[idx] 
        for r, c in zip(dr, dc): 
            if 0 <= row+r < R and 0 <= col+c < C and d_map[row+r][col+c] == 0: 
                if 0 <= row+r*2 < R and 0 <= col+c*2 < C: 
                    shrink = d_map[row+r*2][col+c*2] - d_map[row][col]
                    if max_shrink < shrink: 
                        max_shrink = shrink
    tot_dis = d_map[R-1][C-1] % 100000 - max_shrink + 2
    print(tot_dis)
else: 
    d_map[R-1][C-1] = 200001
    queue.clear()
    visited.clear()
    length = BFS(R-1, C-1, 200001)