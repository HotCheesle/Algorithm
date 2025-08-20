width, height = map(int,input().split())
n = int(input())
stores = list(list(map(int, input().split())) for _ in range(n))
guard = list(map(int, input().split()))

def ch_to_coord(store, width, height): 
    if store[0] == 1: 
        return [store[1], height]
    elif store[0] == 2: 
        return [store[1], 0]
    elif store[0] == 3: 
        return [0, height - store[1]]
    else: 
        return [width, height - store[1]]

if guard[0] == 1: 
    opposit = 2
elif guard[0] == 2: 
    opposit = 1
elif guard[0] == 3: 
    opposit = 4
else: 
    opposit = 3
guard_c = ch_to_coord(guard, width, height)

tot = 0
for st in stores: 
    st_c = ch_to_coord(st, width, height)
    if st[0] == opposit and opposit < 3:
        dis = min(height + st_c[0] + guard_c[0], height + (2*width) - st_c[0] - guard_c[0])
        tot += dis
    elif st[0] == opposit:  
        dis = min(width + st_c[1] + guard_c[1], width + (2*height) - st_c[1] - guard_c[1])
        tot += dis
    else: 
        dis = abs(guard_c[0] - st_c[0]) + abs(guard_c[1] - st_c[1])
        tot += dis

print(tot)