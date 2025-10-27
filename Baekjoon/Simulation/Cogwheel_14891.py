from collections import deque

class Plain: 
    def __init__(self):
        self.gears = [None] * 4
    
    def set_gear(self, idx, mag): 
        self.gears[idx] = Gear(mag)
    
    def is_cuppled(self, a, b): 
        if self.gears[a].get_right() == self.gears[b].get_left(): 
            return False
        else: 
            return True
        
    def get_score(self): 
        score = 0
        for i in range(4): 
            if self.gears[i].get_top() == '1': 
                score += 2 ** i
        return score

class Gear: 
    def __init__(self, mag):
        self.gear = deque(mag)
    
    def get_left(self): 
        return self.gear[6]
    
    def get_right(self): 
        return self.gear[2]
    
    def get_top(self): 
        return self.gear[0]
    
    def turn(self, dir): 
        if dir == 1: 
            self.gear.rotate(1)
        else: 
            self.gear.rotate(-1)

def turn_gear(): 
    global plain, num, dir
    turn_list = [0] * 4
    turn_list[num-1] = dir
    if num != 1: 
        ck_a = num - 1
        for _ in range(3): 
            rs = plain.is_cuppled(ck_a-1, ck_a)
            if not rs: break
            turn_list[ck_a-1] = turn_list[ck_a] * (-1)
            ck_a -= 1
            if ck_a <= 0: break
    if num != 4: 
        ck_b = num + 1
        for _ in range(3): 
            rs = plain.is_cuppled(ck_b-2, ck_b-1)
            if not rs: break
            turn_list[ck_b-1] = turn_list[ck_b-2] * (-1)
            ck_b += 1
            if ck_b >= 5: break
    for i in range(4): 
        if turn_list[i]: 
            plain.gears[i].turn(turn_list[i])

plain = Plain()
for idx in range(4): 
    plain.set_gear(idx, list(input()))
K = int(input())
for _ in range(K): 
    num, dir = map(int, input().split())
    turn_gear()
print(plain.get_score())