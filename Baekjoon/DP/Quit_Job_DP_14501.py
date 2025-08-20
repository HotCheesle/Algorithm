n = int(input())

schedule = list(list(0 for _ in range(n)) for _ in range(2))
max_gains = list(0 for _ in range(n))

def find_best(idx): 
    """ schedule[idx]의 상담을 추가해서 이전 최대 이득과 비교해서
    더 큰 값을 max_gains[idx]에 넣는다.
    """
    try: 
        new_max = schedule[1][idx] + max_gains[idx+schedule[0][idx]]
        max_gains[idx] = max(max_gains[idx+1], new_max)
    except: # IndexError 발생하는 경우는 확인하는 상담만으로 가득 채울때 이다.
        if idx+1 < n: 
            max_gains[idx] = max(max_gains[idx+1], schedule[1][idx]) # 확인하는 상담이 끝까지 다 채울때
        else: 
            max_gains[idx] = schedule[1][idx] # 마지막 1일 경우

for i in range(n): 
    day, cost = map(int, input().split())
    schedule[0][i] = day
    schedule[1][i] = cost
    
for i in range(n): # 퇴사로 인해 상담 못하는 날짜 제외
    if schedule[0][i] > n - i: 
        schedule[0][i] = 0
        schedule[1][i] = 0

for i in range(len(schedule[0])-1, -1, -1): 
    if schedule[0][i] == 0: 
        try: 
            max_gains[i] = max_gains[i+1]
        except: 
            max_gains[i] = 0
        finally: 
            continue
    find_best(i) 

print(max_gains[0])