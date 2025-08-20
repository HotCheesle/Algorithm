T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    bord = list(list(map(int, input().split())) for _ in range(N))
    for r in range(N): 
        if 2 in bord[r]: 
            for c in range(N): 
                if bord[r][c] == 2: 
                    row, col = r, c
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    for dr, dc in zip(dr, dc): 
        dis = 1
        while -1 < row + (dr * dis) < N and -1 < col + (dc * dis) < N: 
            if bord[row+dr*dis][col+dc*dis] == 1: break
            else: 
                bord[row+dr*dis][col+dc*dis] = 2
            dis += 1
    cnt = 0
    for r in range(N): 
        for c in range(N): 
            if bord[r][c] == 0: 
                cnt += 1
    print(f'#{tc} {cnt}')