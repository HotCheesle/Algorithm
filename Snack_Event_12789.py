N = int(input())
num_list = list(map(int, input().split()))
stack = []
order = 1
idx = 0
top = -1
while order != N+1: 
    if top != -1: 
        if stack[top] == order: 
            stack.pop()
            top -= 1
            order += 1
            continue
        if idx == N and stack[top] != order: 
            print('Sad')
            break
    if idx < N: 
        if num_list[idx] != order: 
            stack.append(num_list[idx])
            top += 1
            idx += 1
        elif num_list[idx] == order: 
            idx += 1
            order += 1
    
else: 
    print('Nice')