import sys

n = int(sys.stdin.readline())
plain = list([0]*1001 for _ in range(1001))
area = [0]*n
hide = [0]*n

for i in range(1, n+1): 
    paper = list(map(int, sys.stdin.readline().split()))
    area[i-1] = paper[2] * paper[3]
    for j in range(paper[1], paper[1] + paper[3]): 
        for k in range(paper[0], paper[0] + paper[2]): 
            if plain[j][k] != 0: 
                hide[plain[j][k] - 1] += 1
            plain[j][k] = i
            
for i in range(n): 
    print(area[i] - hide[i])