from collections import deque

N = int(input())
queue = deque(list(enumerate(map(int, input().split()), start=1)))
while queue: 
    num = queue.popleft()
    if num[1] > 0: 
        queue.rotate(-(num[1]-1))
    else: 
        queue.rotate(-num[1])
    print(num[0], end=' ')
print()