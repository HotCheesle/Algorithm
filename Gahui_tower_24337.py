N, a, b = map(int, input().split())
if a + b > N + 1: 
    print(-1)
else: 
    buildings = list(1 for _ in range(N))
    idx = N-2
    for h in range(2, b+1): 
        buildings[idx] = h
        idx -= 1
    if a > b: 
        idx += 1
        for h in range(a, 1, -1): 
            buildings[idx] = h
            idx -= 1
    else: 
        for h in range(a-1, 1, -1): 
            buildings[idx] = h
            idx -= 1
    print(*buildings)