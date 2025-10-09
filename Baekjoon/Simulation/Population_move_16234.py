class World: 
    def __init__(self, N, L, R, maps) -> None:
        self.N = N
        self.L = L
        self.R = R
        self.days = 0
        self.maps = maps

    def union(self): 
        unions = {i:{i} for i in range(self.N**2)}
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
        for idx in range(self.N**2): 
            row, col = idx//self.N, idx%self.N
            for r, c in zip(dr, dc): 
                nrow, ncol = row+r, col+c
                if 0 <= nrow < self.N and 0 <= ncol < self.N: 
                    dif = abs(self.maps[row][col] - self.maps[nrow][ncol])
                    if self.L <= dif <= self.R: 
                        aroot = self.get_root(unions, idx)
                        broot = self.get_root(unions, nrow*self.N + ncol)
                        if aroot == broot: continue
                        unions = self.make_union(unions, aroot, broot)
        if self.pop_move(unions): 
            self.days += 1
            return True
        else: 
            return False

    def pop_move(self, unions): 
        if len(unions) == self.N**2: return False
        for value in unions.values(): 
            tot, cnt = 0, len(value)
            if cnt == 1: continue
            for idx in value: 
                row, col = idx//self.N, idx%self.N
                tot += self.maps[row][col]
            for idx in value: 
                row, col = idx//self.N, idx%self.N
                self.maps[row][col] = tot//cnt
        return True

    def get_root(self, unions, find): 
        head = unions.get(find)
        if head: 
            return find
        else: 
            for key, value in unions.items(): 
                if find in value: 
                    return key
                
    def make_union(self, unions, a, b): 
        unions[a] = unions[a].union(unions[b])
        unions.pop(b)
        return unions

N, L, R = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(N))

world = World(N, L, R, maps)
move = True
while move: 
    move = world.union()
print(world.days)