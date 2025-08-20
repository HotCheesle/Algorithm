import sys

def round_one(c, r, x, y, n, s_n): 
    if n == s_n: return x, y
    for _ in range(r-1): 
        y += 1
        s_n += 1
        if s_n == n: return x, y
    for _ in range(c-1): 
        x += 1
        s_n += 1
        if s_n == n: return x, y
    for _ in range(r-1): 
        y -= 1
        s_n += 1
        if s_n == n: return x, y
    for _ in range(c-2): 
        x -= 1
        s_n += 1
        if s_n == n: return x, y

c, r = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

if n > c*r: print("0")
else:
    seat_num = 1
    x, y = 1, 1
    while True: 
        seat_num += ((c+r)*2) - 4
        if seat_num > n or (c < 3 or r < 3): 
            seat_num -= ((c+r)*2) - 4
            break
        c -= 2
        r -= 2
        x += 1
        y += 1
    xx, yy = round_one(c, r, x, y, n, seat_num)
    print(str(xx) + " " + str(yy))
    