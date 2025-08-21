from collections import deque

class Cube: 
    def __init__(self):
        self.up = deque(list('w' for _ in range(8)))     # 인덱스 0~7은 큐브에서 다음과 같다
        self.down = deque(list('y' for _ in range(8)))   # [0, 1, 2]
        self.front = deque(list('r' for _ in range(8)))  # [7,  , 3]
        self.back = deque(list('o' for _ in range(8)))   # [6, 5, 4]
        self.left = deque(list('g' for _ in range(8)))
        self.right = deque(list('b' for _ in range(8)))
    
    def up_turn(self, direction): 
        if direction == '+': 
            self.up.rotate(2)
            self.front[0], self.left[0], self.back[0], self.right[0] = self.right[0], self.front[0], self.left[0], self.back[0]
            self.front[1], self.left[1], self.back[1], self.right[1] = self.right[1], self.front[1], self.left[1], self.back[1]
            self.front[2], self.left[2], self.back[2], self.right[2] = self.right[2], self.front[2], self.left[2], self.back[2]
        else: 
            self.up.rotate(-2)
            self.front[0], self.left[0], self.back[0], self.right[0] = self.left[0], self.back[0], self.right[0], self.front[0]
            self.front[1], self.left[1], self.back[1], self.right[1] = self.left[1], self.back[1], self.right[1], self.front[1]
            self.front[2], self.left[2], self.back[2], self.right[2] = self.left[2], self.back[2], self.right[2], self.front[2]
    def front_turn(self, direction): 
        if direction == '+': 
            self.front.rotate(2)
            self.up[6], self.right[0], self.down[2], self.left[4] = self.right[0], self.down[2], self.left[4], self.up[6]
            self.up[5], self.right[7], self.down[1], self.left[3] = self.right[7], self.down[1], self.left[3], self.up[5]
            self.up[4], self.right[6], self.down[0], self.left[2] = self.right[6], self.down[0], self.left[2], self.up[4]
        else: 
            self.front.rotate(-2)
            self.up[6], self.right[0], self.down[2], self.left[4] = self.left[4], self.up[6], self.right[0], self.down[2]
            self.up[5], self.right[7], self.down[1], self.left[3] = self.left[3], self.up[5], self.right[7], self.down[1]
            self.up[4], self.right[6], self.down[0], self.left[2] = self.left[2], self.up[4], self.right[6], self.down[0]
    def back_turn(self, direction): 
        if direction == '+': 
            self.back.rotate(2)
            self.up[2], self.left[0], self.down[6], self.right[4] = self.right[4], self.up[2], self.left[0], self.down[6]
            self.up[1], self.left[7], self.down[5], self.right[3] = self.right[3], self.up[1], self.left[7], self.down[5]
            self.up[0], self.left[6], self.down[4], self.right[2] = self.right[2], self.up[0], self.left[6], self.down[4]
        else: 
            


cube = Cube()
cube.up_turn('+')
print(cube.front)