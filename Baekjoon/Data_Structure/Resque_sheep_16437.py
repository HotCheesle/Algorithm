import sys

def count_sheep(): 
    stack = [1]
    top = 0
    visited = set()
    while stack: 
        island = stack[top]
        if not contry[island][2]: 
            parent = contry[island][1]
            while parent != 0 and contry[island][0] < 0: 
                island = contry[island][1]
                parent = contry[island][1]
            while parent != 0 and contry[island][0] > 0: 
                contry[parent][0] += contry[island][0]
                contry[island][0] = 0
                island = parent
                parent = contry[island][1]
            stack.pop()
            top -= 1
            continue
        for son in contry[island][2]: 
            if son not in visited: 
                visited.add(son)
                stack.append(son)
                top += 1
                break
        else: 
            stack.pop()
            top -= 1

N = int(input())
contry = {i: [0, 0, set()] for i in range(1, N+1)} # 증감, 부모, 자식
for num in range(2, N+1): 
    kind, count, lead_to = sys.stdin.readline().split()
    if kind == 'W': 
        contry[num][0] = int(count) * (-1)
    else: 
        contry[num][0] = int(count)
    contry[num][1] = int(lead_to)
    contry[int(lead_to)][2].add(num)
count_sheep()
print(contry[1][0])