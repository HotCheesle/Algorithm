import sys

w, h = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

w_mv = t % (w*2)
h_mv = t % (h*2)

if w_mv > w - x: 
    w_mv -= w - x
    if w_mv > w: 
        w_mv -= w
        t_x = w_mv
    else: t_x = w - w_mv
else: t_x = x + w_mv

if h_mv > h - y: 
    h_mv -= h - y
    if h_mv > h: 
        h_mv -= h
        t_y = h_mv
    else: t_y = h - h_mv
else: t_y = y + h_mv

print(str(t_x) + " " + str(t_y))