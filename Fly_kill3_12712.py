def kill_count(row, col, width, N): 
    tot_plus, tot_x = flys[row][col], flys[row][col]
    for ofs in range(1, width): 
        if row+ofs < N: 
            tot_plus += flys[row+ofs][col]
            if col+ofs < N: 
                tot_x += flys[row+ofs][col+ofs]
            if col-ofs >= 0: 
                tot_x += flys[row+ofs][col-ofs]
        if row-ofs >= 0: 
            tot_plus += flys[row-ofs][col]
            if col+ofs < N: 
                tot_x += flys[row-ofs][col+ofs]
            if col-ofs >= 0: 
                tot_x += flys[row-ofs][col-ofs]
        if col+ofs < N: 
            tot_plus += flys[row][col+ofs]
        if col-ofs >= 0: 
            tot_plus += flys[row][col-ofs]
    if tot_plus < tot_x: 
        return tot_x
    else: 
        return tot_plus


T = int(input())
for tc in range(1, T+1): 
    N, M = map(int, input().split())
    flys = list(list(map(int, input().split())) for _ in range(N))

    max_kill = 0
    for row in range(N): 
        for col in range(N): 
            kill = kill_count(row, col, M, N)
            if max_kill < kill: 
                max_kill = kill
    print(f'#{tc} {max_kill}')
