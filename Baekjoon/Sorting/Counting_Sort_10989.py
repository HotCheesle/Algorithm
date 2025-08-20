import sys

count = [0 for _ in range(10001)]
N = int(input())
for _ in range(N): 
    num = int(sys.stdin.readline())
    count[num] += 1
for i in range(1, 10001): 
    for _ in range(count[i]): 
        print(i)