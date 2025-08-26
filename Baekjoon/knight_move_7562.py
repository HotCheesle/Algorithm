from collections import deque

T = int(input())
for tc in range(1, T+1): 
    I = int(input())
    cur_x, cur_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    dif_x, dif_y = abs(cur_x - goal_x), abs(cur_y - goal_y)
    cnt = 0
    dr, dc = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    queue = deque([])
    while dif_x + dif_y < 10: 
        if dif_x > dif_y: 
            dif_x = abs(dif_x - 2)
            dif_y = abs(dif_y - 1)
        else: 
            dif_x = abs(dif_x - 1)
            dif_y = abs(dif_y - 2)
    
    cur_x, cur_y = 0, 0
    goal_x, goal_y = dif_x, dif_y
    queue = deque([])
    

    print(cnt)