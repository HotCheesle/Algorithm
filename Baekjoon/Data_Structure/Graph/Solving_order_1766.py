from heapq import heappop, heappush

class Line: 
    def __init__(self, N):
        self.nodes = list(Node(i) for i in range(N+1))

    def order(self, f, b): 
        self.nodes[f].set_son(b)
        self.nodes[b].set_parent(f)

    def get_head(self): 
        heades = []
        for node in self.nodes: 
            if node.number == 0: continue
            if len(node.parents) == 0: 
                heades.append(node.number)
        
        return heades
    
    def get_order(self): 
        solved = set()
        pqueue = self.get_head()
        while pqueue: 
            node = self.nodes[heappop(pqueue)]
            num = node.number
            if len(node.parents) != 0 or num in solved: continue
            print(num, end=' ')
            solved.add(num)
            for son in node.sons: 
                heappush(pqueue, son)
                self.nodes[son].remove_parent(num)


class Node: 
    def __init__(self, num):
        self.number = num
        self.parents = []
        self.sons = []

    def set_parent(self, idx): 
        self.parents.append(idx)
    
    def set_son(self, idx): 
        self.sons.append(idx)

    def remove_parent(self, idx): 
        self.parents.remove(idx)

N, M = map(int, input().split())
students = Line(N)
for _ in range(M): 
    a, b = map(int, input().split())
    students.order(a, b)
students.get_order()