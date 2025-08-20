n = int(input())

spot = 4
sub = 0
area = 1
for i in range(n): 
    spot += area * 5 - sub
    area *= 4
    if i == 0: 
        sub += 4
    else: 
        sub = 4**i*4 + sub*2

print(spot)