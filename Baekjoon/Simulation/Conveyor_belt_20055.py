from collections import deque

class Conveyor: 
    def __init__(self, N, dur, K):
        self.N = N
        self.K = K
        self.belt = deque(dur)
        self.robots = deque([])
        self.cycle = 0

    def role_belt(self): 
        self.belt.rotate(1)
        for i in range(len(self.robots)): 
            self.robots[i] += 1
        if len(self.robots) and self.robots[0] == self.N: 
            self.robots.popleft()
        for i in range(len(self.robots)): 
            pos = self.robots[i]
            if self.belt[pos] != 0 and pos + 1 not in self.robots: 
                self.robots[i] += 1
                self.belt[pos] -= 1
        if len(self.robots) and self.robots[0] == self.N: 
            self.robots.popleft()
        if self.belt[0] != 0: 
            self.robots.append(1)
            self.belt[0] -= 1
        self.cycle += 1
        return self.belt.count(0)
    
    def get_cycle(self): 
        return self.cycle

N, K = map(int, input().split())
belt = list(map(int, input().split()))
conveyor = Conveyor(N, belt, K)
broken = 0
while broken < K: 
    broken = conveyor.role_belt()
print(conveyor.get_cycle())