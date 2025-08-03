n = int(input())
stairs = []
for _ in range(n): 
    stairs.append(int(input()))

step = [stairs[n-1] + stairs[n-2] for _ in range(n+1)]

def best_step(idx): 
    step[idx] = max(stairs[idx+1]+step[idx+3], stairs[idx]+step[idx+2])

for i in range(n-3, -1, -1): 
    best_step(i)

print(step[0])