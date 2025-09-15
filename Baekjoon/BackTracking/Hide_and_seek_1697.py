from collections import deque

def BFS(N, K): 
    queue = deque([(N, 0)])
    visited = set()
    while queue: 
        now = queue.popleft()
        if now[0] == K: 
            return now[1]
        if now[0] in visited: continue
        if now[0] < K: 
            queue.append((now[0]*2, now[1]+1))
            queue.append((now[0]+1, now[1]+1))
        queue.append((now[0]-1, now[1]+1))
        visited.add(now[0])

N, K = map(int, input().split())
if N == K: 
    print(0)
elif K < N: 
    print(N-K)
else: 
    min_time = BFS(N, K)
    print(min_time)