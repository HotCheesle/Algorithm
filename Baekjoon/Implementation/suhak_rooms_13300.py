import sys

N, rm = map(int, sys.stdin.readline().split())
stud = list(list([0, 0, 0, 0, 0, 0])for _ in range(2))
for i in range(N): 
    gen, gr = map(int, sys.stdin.readline().split())
    stud[gen][gr-1] = stud[gen][gr-1] + 1

need_rm = 0
for gend in range(2): 
    for gra in range(6): 
        need_rm = need_rm + stud[gend][gra] // rm
        if stud[gend][gra] % rm != 0: need_rm = need_rm + 1
        
print(str(need_rm))