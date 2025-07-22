import sys

n = int(sys.stdin.readline())
papers = [[0]*n]
area = [0]*n

for i in range(n): 
    papers[i] = list(map(int, sys.stdin.readline().split()))

