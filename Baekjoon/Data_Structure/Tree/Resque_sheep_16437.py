import sys
sys.setrecursionlimit(123457)

def count_sheep(island): 
    for son in country[island][1]: 
        country[island][0] += count_sheep(son)
    if country[island][0] > 0: 
        return country[island][0]
    else: 
        return 0

N = int(input())
country = {i: [0, set()] for i in range(1, N+1)} # 증감, 자식
for num in range(2, N+1): 
    kind, count, lead_to = sys.stdin.readline().split()
    if kind == 'W': 
        country[num][0] = int(count) * (-1)
    else: 
        country[num][0] = int(count)
    country[int(lead_to)][1].add(num)
sheep = count_sheep(1)
print(sheep)