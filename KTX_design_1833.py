N = int(input())
adjancy_matrix = list(list(map(int, input().split())) for _ in range(N))
sets = list([i] for i in range(N+1))
tot_sets = N

def union_set(a, b): 
    global tot_sets
    if sets[a] == sets[b]: return
    else: 
        for i in range(1, N+1): 
            if sets[i] == sets[b]: 
                sets[i] = sets[a]
        tot_sets -= 1
        return

tot_cost = 0
for row in range(N-1): 
    for col in range(row+1, N):
        if adjancy_matrix[row][col] < 0: 
            union_set(row, col)
            tot_cost -= adjancy_matrix[row][col]

while tot_sets != 1: 
    