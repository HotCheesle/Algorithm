def ev_od(num): 
    if int(num) % 2 == 0: 
        return 'E'
    else: 
        return 'O'
    
def zig_zag(num_list, order): 
    cnt = 0
    not_comp = True
    hit_left, hit, hit_right = False, False, False
    while not_comp: 
        not_comp = False
        for idx in range(1, N-1): 
            if num_list[idx-1] == order[(idx-1)%2]:
                hit_left = True
            else: 
                hit_left = False
            if num_list[idx] == order[idx%2]:
                hit = True
            else: 
                hit = False
            if num_list[idx+1] == order[(idx+1)%2]:
                hit_right = True
            else: 
                hit_right = False
            
            if not hit_right and not hit and hit_left: 
                num_list[idx], num_list[idx+1] = num_list[idx+1], num_list[idx]
                cnt += 1
                not_comp = True
            elif not hit_left and not hit and hit_right:
                num_list[idx], num_list[idx-1] = num_list[idx-1], num_list[idx]
                cnt += 1
                not_comp = True
            elif not hit_left and hit_right: 
                num_list[idx-1], num_list[idx+1] = num_list[idx+1], num_list[idx-1]
                cnt += 1
                not_comp = True
    return cnt

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    num_list = list(map(ev_od, input().split()))
    e_cnt = num_list.count('E')
    o_cnt = num_list.count('O')
    if abs(e_cnt - o_cnt) > 1: 
        print(f'#{tc} -1')
        continue
    else: 
        if e_cnt > o_cnt: 
            cnt = zig_zag(num_list.copy(), ['E', 'O'])
        elif e_cnt < o_cnt: 
            cnt = zig_zag(num_list.copy(), ['O', 'E'])
        else: 
            cnt = min(zig_zag(num_list.copy(), ['E', 'O']), zig_zag(num_list.copy(), ['O', 'E']))

        print(f'#{tc} {cnt}')
