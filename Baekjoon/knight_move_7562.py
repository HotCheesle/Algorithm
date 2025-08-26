from collections import deque

T = int(input())
for tc in range(1, T+1): 
    I = int(input())
    cur_x, cur_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    cnt = 0
    dr, dc = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    
    queue = deque([(cur_x, cur_y, 0)])
    visited = {(cur_x, cur_y)}
    bottom = min(cur_y, goal_y) - 3
    if bottom < 0: bottom = 0
    top = max(cur_y, goal_y) + 4
    if top > I: top = I
    left = min(cur_x, goal_x) - 3
    if left < 0: left = 0
    right = max(cur_x, goal_x) + 4
    if right > I: right = I
    while queue: 
        cur = queue.popleft()
        if cur[0] == goal_x and cur[1] == goal_y: 
            cnt = cur[2]
            break
        else: 
            for y, x in zip(dr, dc): 
                if left <= cur[0]+x < right and bottom <= cur[1]+y < top:
                    if (cur[0]+x, cur[1]+y) not in visited: 
                        visited.add((cur[0]+x, cur[1]+y))
                        queue.append((cur[0]+x, cur[1]+y, cur[2]+1))

    print(cnt)