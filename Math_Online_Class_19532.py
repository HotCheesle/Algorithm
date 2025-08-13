a, b, c, d, e, f = map(int, input().split())

if (a*e - d*b) != 0:
    x = (c*e - b*f) // (a*e - d*b)
    if b != 0: 
        y = (c - a*x) // b
    elif e != 0: 
        y = (f - d*x) // e
else: 
    y = (d*b - a*e) // (c*d - a*f)
    if a != 0: 
        x = (c - b*y) // a
    elif d != 0: 
        x = (f - e*y) // d
print(f'{x} {y}')