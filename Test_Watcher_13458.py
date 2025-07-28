n = int(input())
test_rooms = list(map(int, input().split()))
direc, sub_direc = map(int, input().split())
need_direc = [1 for _ in range(n)]

for i in range(n): 
    test_rooms[i] -= direc
    if test_rooms[i] <= 0: continue
    need_direc[i] += test_rooms[i] // sub_direc
    if test_rooms[i] % sub_direc: 
        need_direc[i] += 1

tot = 0
for d in need_direc: 
    tot += d
print(tot, end='')