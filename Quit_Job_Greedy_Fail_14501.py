n = int(input())
schedule = list(list(0 for _ in range(n)) for _ in range(2))

def get_real_gain(idx): 
    real_gain = 0
    if ratio[0][idx] == -1: 
        return real_gain
    for d in range(schedule[0][idx]): # 선택으로 인해 상담동안 보는 손해
        if d == 0: 
            real_gain += schedule[1][idx]
        else: 
            real_gain -= schedule[1][idx+d]
    for i in range(idx): # 선택으로 인해 막히는 선택지까지 손해
        if schedule[0][i] > idx - i: 
            sub = 0
            for j in range(1, schedule[0][i]): 
                if ratio[0][i+j] == 0: sub += 1
            real_gain -= int(schedule[1][i] * (sub/(schedule[0][i]-1)))
    return real_gain

for i in range(n): 
    schedule[0][i], schedule[1][i] = map(int, input().split())
    if schedule[0][i] > (n - i): 
        schedule[0][i] = 0 # [0]은 상담 일수
        schedule[1][i] = 0 # [1]은 상담 이윤

ratio = list(list(0 for _ in range(n)) for _ in range(2))
for i in range(n): 
    if schedule[0][i] == 0: 
        ratio[0][i] = -1 # [0]은 선택여부 -1: don't care, 0: 선택가능, 1: 선택
    ratio[1][i] = get_real_gain(i)

# 여기서부터 ratio[0]에 0이 없을때 까지 반복
while 0 in ratio[0]: 
    max_idx = 0
    max_ratio = -999999
    for i in range(n): # 최대 이윤 탐색
        if max_ratio < ratio[1][i] and ratio[0][i] == 0: 
            max_ratio = ratio[1][i]
            max_idx = i
    ratio[0][max_idx] = 1 # 가장 순수익이 많은 날 선택
    
    for i in range(1, schedule[0][max_idx]): # 선택으로 인해 막히는 날 제외
        if ratio[0][max_idx+i] == 0: 
            ratio[0][max_idx+i] = -1
            schedule[0][max_idx+i] = 0
            schedule[1][i] = 0

    for i in range(max_idx): # 선택 불가능 날 제외
        for d in range(schedule[0][i]): 
            if ratio[0][i+d] == 1: 
                ratio[0][i] = -1
                schedule[0][i] = 0
                schedule[1][i] = 0
    
    schedule[0][max_idx] = 0 # 선택한 날은 계산에서 제외

    for i in range(n): # 순수익 재계산
        ratio[1][i] = get_real_gain(i)

tot = 0
for i in range(n): 
    if ratio[0][i] == 1: 
        tot += schedule[1][i]
print(tot)