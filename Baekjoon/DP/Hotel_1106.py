import math
C, N = map(int, input().split())
cytis = []
for _ in range(N): 
    cost, customer = map(int, input().split())
    cytis.append((cost, customer))
cost, customer = 0, 0
while customer < C: 
    remain = C - customer
    cost_list = list(map(lambda c: int(math.ceil(remain/c[1]))*c[0], cytis))
    cheap_city = cost_list.index(min(cost_list))
    cost += cytis[cheap_city][0]
    customer += cytis[cheap_city][1]
print(cost)