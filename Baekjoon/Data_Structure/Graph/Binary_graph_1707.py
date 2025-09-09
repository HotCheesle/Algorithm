from collections import deque
import sys

T = int(input())
for tc in range(T): 
    V, E = map(int, input().split())
    graph = {i: set() for i in range(1, V+1)}
    edged_vertex = set()
    for _ in range(E): 
        st, ed = map(int, sys.stdin.readline().split())
        graph[st].add(ed)
        graph[ed].add(st)
        edged_vertex.add(st)
        edged_vertex.add(ed)
    b_set1, b_set2 = set([st]), set()
    edged_v = len(edged_vertex)
    visited = set()
    queue = deque([([st], 0)])
    while len(visited) != edged_v: 
        if not queue: 
            not_visited = edged_vertex.difference(visited)
            nst = not_visited.pop()
            queue.append(([nst], 0))
        now = queue.popleft()
        for v in now[0]: 
            if v in visited: continue
            if now[1] == 0: 
                b_set2 = b_set2.union(graph[v])
                visited.add(v)
                queue.append((graph[v], 1))
            else: 
                b_set1 = b_set1.union(graph[v])
                visited.add(v)
                queue.append((graph[v], 0))
        if b_set1.intersection(b_set2): 
            print('NO')
            break
    else: 
        print('YES')
