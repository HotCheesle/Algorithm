n = int(input())
schedule = list(list(0 for _ in range(n)) for _ in range(2))

for i in range(n): 
    schedule[0][i], schedule[1][i] = map(int, input().split())
    if schedule[0][i] > (n - i): 
        schedule[0][i] = 0 # [0]은 상담일수
        schedule[1][i] = 0 # [1]은 상담 이윤

ratio = list(list(0 for _ in range(n)) for _ in range(2))
for i in range(n): 
    if schedule[0][i] == 0: 
        ratio[0][i] = -1 # [0]은 선택여부 -1: don't care, 0: 선택가능, 1: 선택
    real_gain = 0
    for d in range(schedule[0][i]): # 여기에 선택으로 인해 막히는 선택지까지 손해로 봐야함
        if d == 0: 
            real_gain += schedule[1][i]
        else: 
            real_gain -= schedule[1][i+d]
    ratio[1][i] = real_gain

# 여기서부터 ratio[0]에 0이 없을때 까지 반복
while 0 in ratio[0]: 
    max_idx = 0
    max_ratio = ratio[1][0]
    for i in range(n): 
        if max_ratio < ratio[1][i]: 
            max_ratio = ratio[1][i]
            max_idx = i
    schedule[0][max_idx] = 0
    ratio[0][max_idx] = 1 # 가장 순수익이 많은 날 선택

    for i in range(n): # 선택 불가능 날 제외
        for d in range(schedule[0][i]): 
            if ratio[0][i+d] == 1: 
                ratio[0][i] = -1
                schedule[0][i] = 0
                schedule[1][i] = 0

    for i in range(n): # 순수익 재계산
        real_gain = 0
        for d in range(schedule[0][i]): 
            if d == 0: 
                real_gain += schedule[1][i]
            else: 
                real_gain -= schedule[1][i+d]
        ratio[1][i] = real_gain

tot = 0
for i in range(n): 
    if ratio[0][i] == 1: 
        tot += schedule[1][i]
print(tot)