N, M = map(int, input().split())
sets = list(range(N+1))

def find_root(current): 
    if current == sets[current]: 
        return current
    else: 
        sets[current] = find_root(sets[current])
        return sets[current]
    
def union_set(a, b): 
    aroot = find_root(a)
    broot = find_root(b)
    if aroot == broot: return
    else: 
        sets[broot] = aroot
        return 
    
def is_contain(a, b): 
    aroot = find_root(a)
    broot = find_root(b)
    if aroot==broot: return True
    else: return False

for _ in range(M): 
    comm, a, b = map(int, input().split())
    if comm == 0: 
        union_set(a, b)
    else: 
        if is_contain(a, b): print('YES')
        else: print('NO')