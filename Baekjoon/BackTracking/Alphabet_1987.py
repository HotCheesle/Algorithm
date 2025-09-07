from heapq import heappush

def DFS_bt(row, col, visited):
    leaf = True 
    for r, c in zip(dr, dc): 
        nrow, ncol = row+r, col+c
        if 0 <= nrow < R and 0 <= ncol < C and board[nrow][ncol] not in visited: 
            visited.add(board[nrow][ncol])
            leaf = False
            DFS_bt(nrow, ncol, visited)
            visited.remove(board[nrow][ncol])
    if leaf: 
        heappush(max_heap,-len(visited))


R, C = map(int, input().split())
board = list(input() for _ in range(R))
visited = set(board[0][0])
max_heap = []
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
DFS_bt(0, 0, visited)
print(max_heap[0]*(-1))
