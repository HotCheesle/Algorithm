import sys

N = int(sys.stdin.readline().rstrip())
sample = round(N*0.62)
max_len = 0
max_second = 0
if N <= 20: 
    for i in range(1, N+1):
        lst = list([N])
        num = i
        idx = 2
        while(num >= 0): 
            lst.append(num)
            num = lst[idx-2] - lst[idx-1]
            idx = idx + 1
        if max_len < len(lst): 
            max_len = len(lst)
            maxed_lst = lst.copy()
    print(max_len)
    for i in maxed_lst: 
        print(i, end=" ")
else: 
    for i in range(-round(N*0.05), round(N*0.05)): 
        lst = list([N])
        num = sample + i
        idx = 2
        while(num >= 0): 
            lst.append(num)
            num = lst[idx-2] - lst[idx-1]
            idx = idx + 1
        if max_len < len(lst): 
            max_len = len(lst)
            maxed_lst = lst.copy()
    print(max_len)
    for i in maxed_lst: 
        print(i, end=" ")