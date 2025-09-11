import sys
sys.setrecursionlimit(200000)

R, C = map(int, input().split())

table = [list(input()) for _ in range(R)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, visited_alpha):

    max_count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < R and 0 <= ny < C and table[nx][ny] not in visited_alpha):
            visited_alpha.add(table[nx][ny])
            count = 1 + dfs(nx, ny, visited_alpha)
            max_count = max(max_count, count)

            visited_alpha.remove(table[nx][ny])

    return max_count

start_alpha = table[0][0]
visited = {start_alpha}

result = dfs(0, 0, visited)
print(result)