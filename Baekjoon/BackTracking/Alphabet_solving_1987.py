# from heapq import heappush
import sys
sys.setrecursionlimit(200000)

def DFS_bt(row, col, visited, cnt):
    global max_len
    leaf = True 
    # for r, c in zip(dr, dc): 
    for i in range(4): 
        nrow, ncol = row+dr[i], col+dc[i]
        if 0 <= nrow < R and 0 <= ncol < C and board[nrow][ncol] not in visited: 
            visited.add(board[nrow][ncol])
            leaf = False
            DFS_bt(nrow, ncol, visited, cnt+1)
            visited.remove(board[nrow][ncol])
    if leaf: 
        # heappush(max_heap,-len(visited))
        max_len = max(max_len, cnt)

R, C = map(int, input().split())
board = list(input() for _ in range(R))
visited = set(board[0][0])
# max_heap = []
max_len = 0
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
DFS_bt(0, 0, visited, 1)
# print(max_heap[0]*(-1))
print(max_len)