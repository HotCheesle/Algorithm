from math import sqrt
brown, yellow = 18, 6

# 2w + 2h - 4 == brown
# (w-2) * (h-2) == wh - 2(w + h) + 4 == yellow
# brown + yellow = wh (w >= h) w는 항상 sqrt(brown + yellow) 보다 큼

for w in range(int(sqrt(brown + yellow)), ((brown + yellow) // 3) + 1): 
    h = (brown + yellow) / w
    if h.is_integer() and w >= h and w + w + h + h - 4 == brown: 
        print([w, int(h)])