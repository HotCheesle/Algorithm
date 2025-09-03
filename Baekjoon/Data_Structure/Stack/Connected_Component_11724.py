from collections import deque
import sys

def DFS(): 
    while stack: 
        v = stack[-1]
        for vertex in graph[v]: 
            if vertex not in visited: 
                visited.append(vertex)
                stack.append(vertex)
                break
        else: 
            stack.pop()

V, E = map(int, input().split())
graph = {i:[] for i in range(1, V+1)}
stack = deque([])
visited = []
for _ in range(E): 
    st, ed = map(int, sys.stdin.readline().split())
    graph[st].append(ed)
    graph[ed].append(st)
root, cnt = 1, 0
while root <= V: 
    if root not in visited: 
        visited.append(root)
        stack.append(root)
        DFS()
        cnt += 1
    root += 1
print(cnt)