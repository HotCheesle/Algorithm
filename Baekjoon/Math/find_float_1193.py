n = int(input())

step = 1
num = 1
while num < n: 
    num += 4*step
    step += 1
else: 
    if step != 1: 
        step -= 1
        num -= 4*step

up = step
down = step
dif = n - num
if dif < step: 
    up -= dif
    down += dif
elif dif < step*3: 
    dif -= step
    up = 1 + dif
    down = 2*down - dif
else: 
    dif -= step*3
    up = up*2 + 1 - dif
    down = 1 + dif
print(f'{up}/{down}')