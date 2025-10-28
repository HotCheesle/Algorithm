from heapq import heappush, heappop

N = int(input())
table = list(list(map(int, input().split())) for _ in range(N))
pqueue = []
for i in range(N): 
    heappush(pqueue, (table[N-1][i]*(-1), N-1, i))

for _ in range(N-1): 
    num, row, col = heappop(pqueue)
    heappush(pqueue, (table[row-1][col]*(-1), row-1, col))

num, row, col = heappop(pqueue)
print(num*(-1))