from collections import deque
import sys

T = int(input())
for tc in range(T): 
    V, E = map(int, input().split())
    graph = {i: set() for i in range(1, V+1)}
    for _ in range(E): 
        st, ed = map(int, sys.stdin.readline().split())
        graph[st].add(ed)
        graph[ed].add(st)
    b_set1, b_set2 = set([1]), set()
    cnt = 0
    visited = set()
    queue = deque([[1]])
    while len(visited) != V: 
        for v in queue.popleft(): 
            if v in visited: continue
            if cnt % 2 == 0: 
                b_set2 = b_set2.union(graph[v])
                queue.append(graph[v])
                visited.add(v)
            else: 
                b_set1 = b_set1.union(graph[v])
                queue.append(graph[v])
                visited.add(v)
        cnt += 1
        if b_set1.intersection(b_set2): 
            print('NO')
            break
    else: 
        print('YES')
