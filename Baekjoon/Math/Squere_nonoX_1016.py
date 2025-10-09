from math import ceil, sqrt as sq
start, end = map(int, input().split())

tot = end - start + 1
square = set()
dupl = 0
sqrt = 2
while sqrt**2 <= end: 
    st = ceil(start/(sqrt**2))
    ed = end//(sqrt**2)
    check = max(ceil(sq(st)), 2)
    while check**2 <= ed: 
        if (sqrt**2 * check**2) not in square: 
            square.add(sqrt**2 * check**2)
        else: 
            dupl += 1
        check += 1
    sqrt += 1
print(tot - dupl)