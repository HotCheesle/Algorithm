from collections import deque
from copy import deepcopy as dcopy
import sys

class Tree(): 
    def __init__(self, N) -> None:
        self.root = Island(1, '', 0, None)
        for isl in range(2, N+1): 
            self.root.sons.add(Island(isl, '', 0, None))

    def connect_island(self, island, kind, count, lead_to): 
        par = self.DFS(lead_to)
        me = self.DFS(island)
        self.root.sons.remove(me)
        par.sons.add(me)
        me.parent = par
        me.kind = kind
        me.count = count

    def DFS(self, find): 
        if self.root.island == find: 
            return self.root
        top = 0
        stack = deque([self.root])
        visited = set()
        while stack: 
            vertex = stack[top]
            if vertex.island == find: 
                return vertex
            for son in vertex.sons: 
                if son not in visited: 
                    visited.add(son)
                    stack.append(son)
                    top += 1
                    break
            else: 
                stack.pop()
                top -= 1
        return None
    
    def count_sheep(self): 
        stack = deque([(self.root, {'W': 0, 'S': 0})])
        visited = set()
        top = 0
        escape = 0
        while stack: 
            vertex = stack[top]
            if not vertex[0].sons: 
                wolf = vertex[1]['W']
                sheep = vertex[1]['S']
                if sheep - wolf > 0: 
                    escape += sheep - wolf
            for son in vertex[0].sons: 
                if son not in visited: 
                    visited.add(son)
                    update = dcopy(vertex[1])
                    update[son.kind] += son.count
                    stack.append((son, update))
                    top += 1
                    break
            else: 
                stack.pop()
                top -= 1
        return escape
            

class Island(): 
    def __init__(self, island, kind, count, lead_to) -> None:
        self.kind = kind
        self.count = count
        self.parent = lead_to
        self.sons = set()
        self.island = island


N = int(input())
contry = Tree(N)
for num in range(2, N+1): 
    kinds, counts, connect = sys.stdin.readline().split()
    contry.connect_island(num, kinds, int(counts), int(connect))
escape = contry.count_sheep()
print(escape)