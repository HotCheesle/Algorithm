import sys

N = int(input())
queue = [0 for _ in range(100001)]
start, end = 0, 0

for n in range(N): 
    comm = tuple(sys.stdin.readline().split())
    if len(comm) == 2: 
        queue[end] = int(comm[1])
        end += 1
    elif comm[0] == 'pop': 
        if start == end: 
            print('-1')
        else: 
            print(queue[start])
            start += 1
    elif comm[0] == 'size': 
        print(end - start)
    elif comm[0] == 'empty': 
        if start == end: 
            print('1')
        else: 
            print('0')
    elif comm[0] == 'front': 
        if start == end: 
            print('-1')
        else: 
            print(queue[start])
    elif comm[0] == 'back': 
        if start == end: 
            print('-1')
        else: 
            print(queue[end-1])