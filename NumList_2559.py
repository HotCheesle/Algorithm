# 시간 복잡도에 대해 더 생각하고 알고리즘을 짜야함
# 기존 Block만큼 더해서 계산 O(N^2) -> 앞을 빼고 뒤를 더하고 O(N)
# 1억번에 약 1초이므로 N^2의 경우 50000^2 -> 약 25초...

import sys

N, Block = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))

max_sum = 0
for i in range(Block): 
    max_sum = max_sum + temp[i]
sum = max_sum

for i in range(N-Block): 
    sum = sum - temp[i]
    sum = sum + temp[i+Block]
    if max_sum < sum: max_sum = sum

print(max_sum)