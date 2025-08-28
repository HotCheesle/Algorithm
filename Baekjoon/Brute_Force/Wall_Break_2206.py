def BFS(st_r, st_c, distance, dis_map): 
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
                    dis_map[row][col] = dis
    return rear

R, C = map(int, input().split())
maze = list(list(input()) for _ in range(R))
d_map = list(list(0 for _ in range(C)) for _ in range(R))
d_map[0][0] = 1000001
queue = [(0, 0, 0) for _ in range(1000001)]
visited = set()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
length = BFS(0, 0, 1000001, d_map)
# 예외1 막힌 길로 뚫었는데 그쪽이 큰 숫자라 shrink가 크게 일어난것으로 착각함 그러면 뚫을때 마다 확인? -> 해결
# 예외2 코너를 돌아가는것 (3방향)을 탐지해야 함 이전에는 직선만 탐지했었다...

if d_map[R-1][C-1] != 0: 
    rev_d_map = list(list(0 for _ in range(C)) for _ in range(R))
    rev_d_map[R-1][C-1] = 1000001
    visited.clear()
    length = BFS(R-1, C-1, 1000001, rev_d_map)
    min_dis = d_map[R-1][C-1] % 1000000
    for idx in range(length):
        row, col, distance = queue[idx] 
        for r, c in zip(dr, dc): 
            if 0 <= row+r < R and 0 <= col+c < C and d_map[row+r][col+c] == 0: 
                w_row, w_col = row+r, col+c
                for y, x in zip(dr, dc): 
                    if row == w_row+y and col == w_col+x: # 되돌아가는거 방지
                        continue
                    if 0 <= w_row+y < R and 0 <= w_col+x < C and d_map[w_row+y][w_col+x] != 0:
                        dis = d_map[w_row+y][w_col+x] % 1000000 + distance % 1000000 + 1
                        if min_dis > dis: 
                            min_dis = dis
    print(min_dis)
else: 
    min_dis = None
    d_map[R-1][C-1] = 2000001
    queue = [(0, 0, 0) for _ in range(1000001)]
    visited.clear()
    length = BFS(R-1, C-1, 2000001, d_map)
    for idx in range(length):
        row, col, distance = queue[idx] 
        for r, c in zip(dr, dc): 
            if 0 <= row+r < R and 0 <= col+c < C and d_map[row+r][col+c] == 0: 
                w_row, w_col = row+r, col+c
                for y, x in zip(dr, dc): 
                    if 0 <= w_row+y < R and 0 <= w_col+x < C and d_map[w_row+y][w_col+x] // 1000000 == 1:
                        dis = d_map[w_row+y][w_col+x] % 1000000 + distance % 1000000 + 1
                        if min_dis is None: 
                            min_dis = dis
                        elif min_dis > dis: 
                            min_dis = dis
    if min_dis: 
        print(min_dis)
    else: 
        print(-1)