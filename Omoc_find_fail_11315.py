T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    bord = list(list(input()) for _ in range(N))
    is_found = False
    for rc in range(N): 
        r_cnt, c_cnt = 0, 0
        for i in range(N): 
            if bord[rc][i] == 'o': 
                r_cnt += 1
            else: 
                if r_cnt >= 5: 
                    print(f'#{tc} YES')
                    is_found = True
                    r_cnt = 0
                    break
                else: 
                    r_cnt = 0
            if bord[i][rc] == 'o': 
                c_cnt += 1
            else: 
                if c_cnt >= 5: 
                    print(f'#{tc} YES')
                    is_found = True
                    c_cnt = 0
                    break
                else: 
                    c_cnt = 0
        if r_cnt >= 5 or c_cnt >= 5: 
            print(f'#{tc} YES')
            is_found = True
            break
        if is_found: break
    if is_found: continue

    for r in range(5-N, N-4): 
        rd_cnt = 0
        for i in range(N): 
            if 0 <= r+i < N: 
                if bord[r+i][i] == 'o': 
                    rd_cnt += 1
                else: 
                    if rd_cnt >= 5: 
                        print(f'#{tc} YES')
                        is_found = True
                        rd_cnt = 0
                        break
                    else: 
                        rd_cnt = 0
            else:
                continue
        if rd_cnt >= 5: 
            print(f'#{tc} YES')
            is_found = True
            break
        if is_found: break
    if is_found: continue
    
    for r in range(4, (2*N)-5): 
        ru_cnt = 0
        for i in range(N): 
            if 0 <= r-i < N:  
                if bord[r-i][i] == 'o': 
                    ru_cnt += 1
                else: 
                    if ru_cnt >= 5: 
                        print(f'#{tc} YES')
                        is_found = True
                        ru_cnt = 0
                        break
                    else: 
                        ru_cnt = 0
            else: 
                continue
        if ru_cnt >= 5: 
            print(f'#{tc} YES')
            is_found = True
            break
        if is_found: break
    if is_found: continue

    print(f'#{tc} NO')