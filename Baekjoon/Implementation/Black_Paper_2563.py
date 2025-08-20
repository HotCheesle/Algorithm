canbus = list([0]*100 for _ in range(100))

n = int(input())
papers = list(list(map(int, input().split())) for _ in range(n))

area = 0
for paper in papers: 
    for y in range(10): 
        for x in range(10): 
            if canbus[paper[1]+y][paper[0]+x] == 0:
                area += 1
                canbus[paper[1]+y][paper[0]+x] = 1

print(area)