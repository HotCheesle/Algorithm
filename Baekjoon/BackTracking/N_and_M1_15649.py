def back_track(N, M, p, cnt): 
    if cnt == M: 
        p_list.append(p)
        return
    for num in range(1, N+1):
        if num in p: continue 
        back_track(N, M, p+[num], cnt+1)


N, M = map(int, input().split())
p_list = []
back_track(N, M, [], 0)
for p in p_list: 
    print(*p)