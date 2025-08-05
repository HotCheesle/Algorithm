n = int(input())
stairs = []
for _ in range(n): 
    stairs.append(int(input()))

def best_step(idx): 
    one_step = stairs[idx-1] + stairs[idx] + step[idx-3] # 두칸 후 한칸 연속으로 올라오는 경우
    two_step = stairs[idx] + step[idx-2] # 두칸 점프로 올라오는 경우
    step[idx] = max(one_step, two_step)

if n < 3: 
    print(sum(stairs))
else: 
    step = [0 for _ in range(n)]
    step[0] = stairs[0] # 첫번째 계단
    step[1] = stairs[0] + stairs[1] # 첫번째 + 두번째 계단
    step[2] = stairs[2] + max(stairs[0], stairs[1]) # 세번째 계단은 확정, 첫번째와 두번째 중 큰 계단을 밟음

    for i in range(3, n): 
        best_step(i)

    print(step[n-1])