apart = list(list(i for i in range(1, 15)) for _ in range(15))

for floor in range(1, 15): 
    for ho in range(1, 14): 
        apart[floor][ho] = apart[floor-1][ho] + apart[floor][ho-1]

T = int(input())
for t in range(T): 
    fl = int(input())
    ho = int(input())
    print(apart[fl][ho-1])