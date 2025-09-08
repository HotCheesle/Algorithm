from heapq import heappush

def DFS_bt(row, col, visited, prelock):
    leaf = True 
    locked = prelock.copy()
    for r, c in zip(dr, dc): 
        nrow, ncol = row+r, col+c
        if 0 <= nrow < R and 0 <= ncol < C and (nrow, ncol) not in locked: 
            if board[nrow][ncol] not in visited: 
                visited.add(board[nrow][ncol])
                leaf = False
                DFS_bt(nrow, ncol, visited, locked)
                visited.remove(board[nrow][ncol])
        locked.add((nrow, ncol))
    if leaf: 
        heappush(max_heap,-len(visited))

R, C = map(int, input().split())
board = list(input() for _ in range(R))
visited = set(board[0][0])
lock = set()
max_heap = []
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
DFS_bt(0, 0, visited, lock)
print(max_heap[0]*(-1))