n = int(input())

schedule = list(list(0 for _ in range(n)) for _ in range(2))

for i in range(n): 
    day, cost = map(int, input().split())
    schedule[0][i] = day
    schedule[1][i] = cost
    
for i in range(n): 
    if schedule[0][i] > n - i: 
        schedule[0][i] = 0
        schedule[1][i] = 0

