n = int(input())
stairs = []
for _ in range(n): 
    stairs.append(int(input()))

step = [0 for _ in range(n)]

def best_step(idx): 
    step[idx] = max(stairs[idx] + step[idx+2], stairs[idx] + stairs[idx+1] + step[idx+3])

step[n-1] = stairs[n-1]
step[n-2] = stairs[n-1] + stairs[n-2]
step[n-3] = max(stairs[n-1] + stairs[n-2], stairs[n-1] + stairs[n-3])
for i in range(n-4, -1, -1): 
    best_step(i)

print(step[0])