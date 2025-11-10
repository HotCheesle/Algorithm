from heapq import heappop, heappush

M, N = map(int, input().split())
mapping = list(list(map(int, input().split())) for _ in range(M))

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

pqueue = []
dp = list(list(0 for _ in range(N)) for _ in range(M))
dp[0][0] = 1
for r in range(M): 
    for c in range(N): 
        if r == 0 and c == 0: continue
        heappush(pqueue, (-mapping[r][c], r, c))

while pqueue: 
    rh, row, col = heappop(pqueue)
    for r, c in zip(dr, dc): 
        nr, nc = row+r, col+c
        if 0 <= nr < M and 0 <= nc < N and -rh < mapping[nr][nc]: 
            dp[row][col] += dp[nr][nc]
    if row == M-1 and col == N-1: break

print(dp[M-1][N-1])