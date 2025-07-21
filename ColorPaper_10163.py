import sys

n = int(sys.stdin.readline())
plain = list(list(0 for _ in range(1001)) for _ in range(1001))

for i in range(1, n+1): 
    paper = list(map(int, sys.stdin.readline().split()))
    for j in range(paper[1], paper[1] + paper[3]): 
        for k in range(paper[0], paper[0] + paper[2]): 
            plain[j][k] = i
            
for i in range(1, n+1): 
    cnt = 0
    for j in range(1001): 
        for k in range(1001): 
            if plain[j][k] == i: 
                cnt += 1
    print(cnt)