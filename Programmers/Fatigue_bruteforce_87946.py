k, dungeons = 80, [[80, 20], [50, 40], [30, 10]]

idx = {i for i in range(len(dungeons))}

answer = 0

def enter_dungeons(k: int, dungeons: list[list[int]], left_idx: set[int]): 
    done = True
    cnt = 0
    for i in left_idx: 
        if (k >= dungeons[i][0]): 
            done = False
            left_idx.remove(i)
            cnt = max(cnt, enter_dungeons(k - dungeons[i][1], dungeons, left_idx))
            left_idx.add(i)
    if done: 
        return len(dungeons) - len(left_idx)
    return cnt

print(enter_dungeons(k, dungeons, idx))