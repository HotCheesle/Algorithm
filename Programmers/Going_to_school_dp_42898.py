m, n, puddles = 3, 3, [[2, 1]]

road = list(list(0 for _ in range(m)) for _ in range(n))
road[0][0] = 1

for r in range(n): 
    for c in range(m): 
        if [c+1, r+1] in puddles: 
            continue
        if r-1 >= 0: 
            road[r][c] += road[r-1][c]
        if c-1 >= 0: 
            road[r][c] += road[r][c-1]

print(road[-1][-1] % 1000000007)