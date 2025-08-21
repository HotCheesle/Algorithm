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
            self.up[6], self.right[0], self.down[2], self.left[4] = self.left[4], self.up[6], self.right[0], self.down[2]
            self.up[5], self.right[7], self.down[1], self.left[3] = self.left[3], self.up[5], self.right[7], self.down[1]
            self.up[4], self.right[6], self.down[0], self.left[2] = self.left[2], self.up[4], self.right[6], self.down[0]
        else: 
            self.front.rotate(-2)
            self.up[6], self.right[0], self.down[2], self.left[4] = self.right[0], self.down[2], self.left[4], self.up[6]
            self.up[5], self.right[7], self.down[1], self.left[3] = self.right[7], self.down[1], self.left[3], self.up[5]
            self.up[4], self.right[6], self.down[0], self.left[2] = self.right[6], self.down[0], self.left[2], self.up[4]
    def back_turn(self, direction): 
        if direction == '+': 
            self.back.rotate(2)
            self.up[2], self.left[0], self.down[6], self.right[4] = self.right[4], self.up[2], self.left[0], self.down[6]
            self.up[1], self.left[7], self.down[5], self.right[3] = self.right[3], self.up[1], self.left[7], self.down[5]
            self.up[0], self.left[6], self.down[4], self.right[2] = self.right[2], self.up[0], self.left[6], self.down[4]
        else: 
            self.back.rotate(-2)
            self.up[2], self.left[0], self.down[6], self.right[4] = self.left[0], self.down[6], self.right[4], self.up[2]
            self.up[1], self.left[7], self.down[5], self.right[3] = self.left[7], self.down[5], self.right[3], self.up[1]
            self.up[0], self.left[6], self.down[4], self.right[2] = self.left[6], self.down[4], self.right[2], self.up[0]
    def left_turn(self, direction): 
        if direction == '+': 
            self.left.rotate(2)
            self.up[0], self.front[0], self.down[0], self.back[4] = self.back[4], self.up[0], self.front[0], self.down[0]
            self.up[7], self.front[7], self.down[7], self.back[3] = self.back[3], self.up[7], self.front[7], self.down[7]
            self.up[6], self.front[6], self.down[6], self.back[2] = self.back[2], self.up[6], self.front[6], self.down[6]
        else: 
            self.left.rotate(-2)
            self.up[0], self.front[0], self.down[0], self.back[4] = self.front[0], self.down[0], self.back[4], self.up[0]
            self.up[7], self.front[7], self.down[7], self.back[3] = self.front[7], self.down[7], self.back[3], self.up[7]
            self.up[6], self.front[6], self.down[6], self.back[2] = self.front[6], self.down[6], self.back[2], self.up[6]
    def right_turn(self, direction): 
        if direction == '+': 
            self.right.rotate(2)
            self.up[4], self.back[0], self.down[4], self.front[4] = self.front[4], self.up[4], self.back[0], self.down[4]
            self.up[3], self.back[7], self.down[3], self.front[3] = self.front[3], self.up[3], self.back[7], self.down[3]
            self.up[2], self.back[6], self.down[2], self.front[2] = self.front[2], self.up[2], self.back[6], self.down[2]
        else: 
            self.right.rotate(-2)
            self.up[4], self.back[0], self.down[4], self.front[4] = self.back[0], self.down[4], self.front[4], self.up[4]
            self.up[3], self.back[7], self.down[3], self.front[3] = self.back[7], self.down[3], self.front[3], self.up[3]
            self.up[2], self.back[6], self.down[2], self.front[2] = self.back[6], self.down[2], self.front[2], self.up[2]
    def down_turn(self, direction): 
        if direction == '+': 
            self.down.rotate(2)
            self.front[6], self.right[6], self.back[6], self.left[6] = self.left[6], self.front[6], self.right[6], self.back[6]
            self.front[5], self.right[5], self.back[5], self.left[5] = self.left[5], self.front[5], self.right[5], self.back[5]
            self.front[4], self.right[4], self.back[4], self.left[4] = self.left[4], self.front[4], self.right[4], self.back[4]
        else: 
            self.down.rotate(-2)
            self.front[6], self.right[6], self.back[6], self.left[6] = self.right[6], self.back[6], self.left[6], self.front[6]
            self.front[5], self.right[5], self.back[5], self.left[5] = self.right[5], self.back[5], self.left[5], self.front[5]
            self.front[4], self.right[4], self.back[4], self.left[4] = self.right[4], self.back[4], self.left[4], self.front[4]
    def show_up(self): 
        for i in range(3): 
            print(self.up[i], end='')
        print()
        print(self.up[7], end='')
        print('w', end='')
        print(self.up[3])
        for i in range(6, 3, -1): 
            print(self.up[i], end='')
        print()

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    cube = Cube()
    turn_list = list(input().split())
    for turn in turn_list: 
        if turn[0] == 'U': 
            cube.up_turn(turn[1])
        elif turn[0] == 'D': 
            cube.down_turn(turn[1])
        elif turn[0] == 'F': 
            cube.front_turn(turn[1])
        elif turn[0] == 'B': 
            cube.back_turn(turn[1])
        elif turn[0] == 'L': 
            cube.left_turn(turn[1])
        elif turn[0] == 'R': 
            cube.right_turn(turn[1])
    cube.show_up()