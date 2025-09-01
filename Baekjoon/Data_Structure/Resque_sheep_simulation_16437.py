import sys

def count_sheep(): 
    stack = [1]
    top = 0
    visited = set()
    while stack: 
        island = stack[top]
        if not country[island][2]: 
            parent = country[island][1]
            while parent != 0 and country[island][0] < 0: 
                island = country[island][1]
                parent = country[island][1]
            while parent != 0: 
                if country[island][0] <= 0 : 
                    island = parent
                    parent = country[island][1]
                    continue
                country[parent][0] += country[island][0]
                country[island][0] = 0
                island = parent
                parent = country[island][1]
            stack.pop()
            top -= 1
            continue
        for son in country[island][2]: 
            if son not in visited: 
                visited.add(son)
                stack.append(son)
                top += 1
                break
        else: 
            stack.pop()
            top -= 1

N = int(input())
country = {i: [0, 0, set()] for i in range(1, N+1)} # 증감, 부모, 자식
for num in range(2, N+1): 
    kind, count, lead_to = sys.stdin.readline().split()
    if kind == 'W': 
        country[num][0] = int(count) * (-1)
    else: 
        country[num][0] = int(count)
    country[num][1] = int(lead_to)
    country[int(lead_to)][2].add(num)
count_sheep()
print(country[1][0])