n, computers = 4, [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]

def find_root(network, com): 
    if network[com] == com: 
        return com
    network[com] = find_root(network, network[com])
    return network[com]

network = [i for i in range(n)]
for com in range(n): 
    for port in range(com+1, n): 
        if computers[com][port]: 
            com_root = find_root(network, com)
            port_root = find_root(network, port)
            network[port_root] = com_root

net_cnt = 0
for i in range(n): 
    if network[i] == i: 
        net_cnt += 1

print(net_cnt)