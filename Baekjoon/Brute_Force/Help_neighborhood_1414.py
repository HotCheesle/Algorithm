from heapq import heappush, heappop
N = int(input())
def lan_len(char): 
    if char.isnumeric(): 
        return 0
    elif char.isupper(): 
        return ord(char)-ord('A')+27
    else: 
        return ord(char)-ord('a')+1

adjacency_char = list(input() for _ in range(N))
adjacency_int = list(list(0 for _ in range(N)) for _ in range(N))
tot_length = 0
for row in range(N): 
    for col in range(N): 
        length = lan_len(adjacency_char[row][col])
        adjacency_int[row][col] = length
        tot_length += length

for row in range(N): 
    for col in range(row+1, N): 
        if adjacency_int[row][col] == 0 or adjacency_int[col][row] == 0: continue
        if adjacency_int[row][col] < adjacency_int[col][row]: 
            adjacency_int[col][row] = adjacency_int[row][col]
        else : 
            adjacency_int[row][col] = adjacency_int[col][row]

pqueue = []
visited = {0, }
for i in range(N): 
    if adjacency_int[0][i] != 0 and i not in visited: 
        heappush(pqueue, (adjacency_int[0][i], i))

need_lan = 0
while len(visited) != N and pqueue: 
    l, cur = heappop(pqueue)
    need_lan += l
    visited.add(cur)
    for i in range(N): 
        if adjacency_int[cur][i] != 0 and i not in visited: 
            heappush(pqueue, (adjacency_int[cur][i], i))

if len(visited) == N: 
    print(tot_length - need_lan)
else: 
    print(-1)