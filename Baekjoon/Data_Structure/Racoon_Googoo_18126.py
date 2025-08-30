def dijkstra(start, dis_map): 
    now = start
    for _ in range(N-1): 
        for edge in graph[now]: 
            if not not_confirm[edge[0]]: 
                continue
            if dis_map[edge[0]] == -1: 
                dis_map[edge[0]] = dis_map[now] + edge[1]
            elif dis_map[now] + edge[1] < dis_map[edge[0]]: 
                dis_map[edge[0]] = dis_map[now] + edge[1]
        min_dis, min_idx = 10**18, 0
        for i in range(2, N+1): 
            if not_confirm[i] and dis_map[i] != -1: 
                if min_dis > dis_map[i]: 
                    min_dis = dis_map[i]
                    min_idx = i
        not_confirm[min_idx] = False
        now = min_idx

N = int(input())
dis_map = [0, 0] + [-1 for _ in range(N-1)]
not_confirm = [False, False] +  [True for _ in range(N-1)]
graph = {i: [] for i in range(1, N+1)}

for _ in range(N-1): 
    st, ed, length = map(int, input().split())
    graph[st].append((ed, length))
    graph[ed].append((st, length))

dijkstra(1, dis_map)
print(max(dis_map))