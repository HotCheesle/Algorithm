def check(row, col, N): 
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for r, c in zip(dr, dc): 
        for ofs in range(1, 5): 
            if 0 <= row+(r*ofs) < N and 0 <= col+(c*ofs) < N: 
                if bord[row+(r*ofs)][col+(c*ofs)] != 'o': 
                    break
            else: 
                break
        else: 
            return True
    return False

T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    bord = list(list(input()) for _ in range(N))
    is_found = False
    for row in range(N): 
        for col in range(N): 
            if bord[row][col] == 'o': 
                if check(row, col, N): 
                    print(f'#{tc} YES')
                    is_found = True
                    break
        if is_found: break
    if is_found: continue
    print(f'#{tc} NO')    