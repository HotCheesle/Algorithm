from heapq import heappush, heappop

n, costs = 4, [[0,1,1],[0,2,5],[1,0,3],[1,3,8],[2,3,1]]

connect: list[set[int]] = []
bridges = []
total_cost = 0

for c in costs: 
    heappush(bridges, (c[2], c[0], c[1]))

while not connect or len(connect[0]) != n: 
    b = heappop(bridges)
    st_group, ed_group = None, None
    for i in range(len(connect)): 
        if b[1] in connect[i]: 
            st_group = i
        if b[2] in connect[i]: 
            ed_group = i
    if st_group is None and ed_group is None: 
        connect.append({b[1], b[2]})
        total_cost += b[0]
    elif st_group is None or ed_group is None: 
        if ed_group is None: 
            connect[st_group].add(b[2])
            total_cost += b[0]
        else: 
            connect[ed_group].add(b[1])
            total_cost += b[0]
    else: 
        if st_group == ed_group: 
            continue
        else: 
            if st_group < ed_group: 
                connect[st_group].update(connect[ed_group])
                connect[ed_group].clear()
            else: 
                connect[ed_group].update(connect[st_group])
                connect[st_group].clear()
            total_cost += b[0]
