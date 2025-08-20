import sys

def shoot(a_s, b_s): 
    for i in range(3, -1, -1): 
        if a_s[i] == b_s[i]: 
            continue
        elif a_s[i] > b_s[i]: return 'A'
        else: return 'B'
    
    return 'D'

n = int(sys.stdin.readline())
for _ in range(n): 
    a_card = list(map(int, sys.stdin.readline().split()))
    b_card = list(map(int, sys.stdin.readline().split()))
    
    a_shape = [0]*4
    b_shape = [0]*4
    
    for a in a_card[1:]: 
        a_shape[a-1] += 1
    for b in b_card[1:]: 
        b_shape[b-1] += 1
    
    print(shoot(a_shape, b_shape))