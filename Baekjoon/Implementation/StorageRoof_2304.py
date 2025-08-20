import sys

N = int(sys.stdin.readline())
pillar = list(list(map(int, sys.stdin.readline().split()))for _ in range(N))

pillar.sort()
top = max(p[1]for p in pillar)
for i in range(N): 
    if pillar[i][1] == top:
        top_p = pillar[i]
        top_idx = i
        break

area = 0
H = 0
for i in range(top_idx): 
    width = pillar[i+1][0] - pillar[i][0]
    if H < pillar[i][1]: H = pillar[i][1]
    area = area + (width * H)

H = 0
for i in range(N-1, top_idx, -1): 
    width = pillar[i][0] - pillar[i-1][0]
    if H < pillar[i][1]: H = pillar[i][1]
    area = area + (width * H)

area = area + top

print(area)