N = int(input())
candidate = []
ticket_cnt = 0

if N == 1: 
    print('0')
else: 
    for _ in range(N): 
        candidate.append(int(input()))

    def my_max(): 
        max_idx = 1
        for i in range(1, N): 
            if candidate[max_idx] < candidate[i]: 
                max_idx = i
        return max_idx

    while candidate[0] <= candidate[my_max()]: 
        candidate[0] += 1
        candidate[my_max()] -= 1
        ticket_cnt += 1

    print(ticket_cnt)