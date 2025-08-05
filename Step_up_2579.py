n = int(input())
stairs = []
for _ in range(n): 
    stairs.append(int(input()))

step = [0 for _ in range(n-3)]
step.append(stairs[n-1] + stairs[n-3]) # n-2번째에서 도착지점으로 뛴 값
step.append(stairs[n-1] + stairs[n-2]) # n-1번째에서 도착지점으로 뛴 값
step.append(stairs[n-1]) # 도착지점은 반드시 밟아야 함
double_step = False

def best_step(idx): 
    global double_step
    one_max = stairs[idx] + step[idx+1] # 바로 이전에서 한칸 내려옴 이 경우 이전값은 두칸 점프해서 내려온 상태
    two_max = stairs[idx] + step[idx+2] # 두칸 이전에서 점프해서 내려옴'
    if double_step: one_max -= stairs[idx+1] # 이전 값이 한칸 이미 한칸 내려온 상태일 경우 취소하고 두칸 내려온 것으로 간주
    if one_max > two_max: 
        step[idx] = one_max
        double_step = True
    else: 
        step[idx] = two_max
        double_step = False


for i in range(n-4, -1, -1): 
    best_step(i)

print(step[0])