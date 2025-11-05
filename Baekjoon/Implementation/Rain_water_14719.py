class Blocks: 
    def __init__(self, H, W, block):
        self.H = H
        self.W = W
        self.block = list(list(0 for _ in range(self.W)) for _ in range(self.H))
        self.blank = self.H * self.W
        for row in range(self.H): 
            for col in range(self.W): 
                if row < block[col]: 
                    self.block[row][col] = 1
                    self.blank -= 1
        self.blocked = self.H * self.W - self.blank

    def after_raining(self): 
        for r in range(self.H): 
            c = 0
            while c < self.W and self.block[r][c] == 0 : 
                self.block[r][c] = 2
                self.blank -= 1
                c += 1
            c = self.W - 1
            while c > -1 and self.block[r][c] == 0: 
                self.block[r][c] = 2
                self.blank -= 1
                c -= 1
        return self.blank

H, W = map(int, input().split())
block = list(map(int, input().split()))
tow_D_world = Blocks(H, W, block)
print(tow_D_world.after_raining())