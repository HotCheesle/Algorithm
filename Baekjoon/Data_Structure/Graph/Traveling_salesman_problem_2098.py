from copy import deepcopy as dcopy
from collections import deque

def BFS(start): 
    queue = deque([(start, 0, [False for _ in range(N)])]) # 현재도시, 비용, visited
    cycle = []
    while queue: 
        cur = queue.popleft()
        if cur[2]: 
            if cur[2][start] and False not in cur[2]: # 모든 도시를 순회하고
                cycle.append(cur[1])               # 가장 마지막에 출발지로 돌아오면
                continue
            elif cur[2][start] and False in cur[2]: # 모든 도시를 순회하지 않고 
                continue                            # 출발지로 돌아오면 무시
        for idx in range(N): # 갈 수 있는 도시 탐색하면서 방문하지 않은 곳을 감
            visited = dcopy(cur[2]) # 독립적인 visited 생성
            if adjacency_matrix[cur[0]][idx] != 0 and not visited[idx]: 
                visited[idx] |= True
                queue.append((idx, cur[1] + adjacency_matrix[cur[0]][idx], visited))
    return min(cycle)

N = int(input())
adjacency_matrix = list(list(map(int, input().split())) for _ in range(N))
minimum = 10**7
for city in range(N): 
    less = BFS(city)
    minimum = min(less, minimum)

print(minimum)