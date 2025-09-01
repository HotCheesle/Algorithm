import sys

def count_sheep(branch): 
    stack = [branch]
    top = 0
    while stack: 
        island = stack[top]
        if len(country[island][1]) == 0: 
            while stack: 
                i


N = int(input())
country = {i: [0, set()] for i in range(1, N+1)} # 증감, 자식
for num in range(2, N+1): 
    kind, count, lead_to = sys.stdin.readline().split()
    if kind == 'W': 
        country[num][0] = int(count) * (-1)
    else: 
        country[num][0] = int(count)
    country[int(lead_to)][2].add(num)
count_sheep()
print(country[1][0])