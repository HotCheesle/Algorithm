T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    balloons = list(list(map(int, input().split())) for _ in range(N))

    row_sum, col_sum = [], []
    for rc in range(N): 
        r_sum, c_sum = 0, 0
        for idx in range(N): 
            r_sum += balloons[rc][idx]
            c_sum += balloons[idx][rc]
        row_sum.append(r_sum)
        col_sum.append(c_sum)
    max_pang = 0
    for r in range(N): 
        for c in range(N): 
            pang = row_sum[r]+col_sum[c]-balloons[r][c]
            if max_pang < pang: 
                max_pang = pang
    print(f'#{tc} {max_pang}')