def get_idx(length, M, p, st, cnt): 
    if cnt == M: 
        remain_list.append(p)
        return
    for idx in range(st, length): 
        if idx in p: continue
        get_idx(length, M, p+[idx], idx+1, cnt+1)

def get_chkien_len(ck, index, ho): 
    min_tot = 9999
    for idx in index: 
        tot = 0
        for h in ho: 
            min_dist = 99
            for i in idx: 
                dist = abs(h[0] - ck[i][0]) + abs(h[1] - ck[i][1])
                min_dist = min(min_dist, dist)
            tot += min_dist
        min_tot = min(min_tot, tot)
    return min_tot

N, M = map(int, input().split())
chicken_city = list(list(map(int, input().split()))for _ in range(N))
chicken_list, house_list = [], []
for r in range(N): 
    for c in range(N): 
        if chicken_city[r][c] == 1: 
            house_list.append((r, c))
        elif chicken_city[r][c] == 2: 
            chicken_list.append((r, c))

remain_list = []
get_idx(len(chicken_list), M, [], 0, 0)
print(get_chkien_len(chicken_list, remain_list, house_list))