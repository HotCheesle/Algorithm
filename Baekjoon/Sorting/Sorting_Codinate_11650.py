N = int(input())
sorting = {}
for _ in range(N): 
    x, y = map(int, input().split())
    if sorting.get(x) == None: 
        sorting[x] = [y]
    else: 
        sorting[x].append(y)

for i in range(-100000, 100001): 
    if sorting.get(i) != None: 
        sort_y = sorted(sorting.get(i))
        for y in sort_y: 
            print(f'{i} {y}')