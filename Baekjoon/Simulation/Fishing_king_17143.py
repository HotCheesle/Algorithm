class Sea: 
    def __init__(self, R, C, shark_list) -> None:
        self.R = R
        self.C = C
        self.shark_list = shark_list
        self.fishing_king_pos = 0

    def one_sec(self): 
        self.fishing_king_pos += 1
        self.sea = list(list([] for _ in range(self.C)) for _ in range(self.R))
        positions = set()
        check_list = set()
        for idx in self.shark_list: 
            if self.shark_list[idx]: 
                self.shark_list[idx].move(self.R, self.C)
                pos = self.shark_list[idx].get_pos()
                if pos not in positions: 
                    positions.add(pos)
                else: 
                    check_list.add(pos)
                self.sea[pos[0]][pos[1]].append(idx)
        

    
class Shark: 
    def __init__(self, r, c, s, d, z) -> None:
        self.row = r
        self.col = c
        self.size = s
        self.speed = d
        self.dir = z

    def move(self, R, C): 
        if self.dir == 1: 
            self.row -= self.speed
            if self.row < 0: 
                self.row *= (-1)
                self.dir = 2
        elif self.dir == 2: 
            self.row += self.speed
            if self.row >= R: 
                self.row = R - self.row%R - 1
                self.dir = 1
        elif self.dir == 3: 
            self.col += self.speed
            if self.col >= C: 
                self.col = C - self.col%C - 1
                self.dir = 4
        else: 
            self.col -= self.speed
            if self.col < 0: 
                self.col *= (-1)
                self.dir = 3
    
    def get_pos(self): 
        return (self.row, self.col)