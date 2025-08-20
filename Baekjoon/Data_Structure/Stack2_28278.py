import sys

def my_push(num): 
    global stack_idx
    stack[stack_idx] = num
    stack_idx += 1

def my_pop(): 
    global stack_idx
    if stack_idx == 0: 
        return -1
    num = stack[stack_idx-1]
    stack_idx -= 1
    return num

N = int(input())
stack_idx = 0
stack = [0 for _ in range(10**6)]
for _ in range(N): 
    inpt = list(map(int, sys.stdin.readline().split()))
    if len(inpt) == 2: 
        my_push(inpt[1])
    else: 
        if inpt[0] == 2: 
            print(my_pop())
        elif inpt[0] == 3: 
            print(stack_idx)
        elif inpt[0] == 4: 
            if stack_idx == 0: 
                print('1')
            else: 
                print('0')
        elif inpt[0] == 5: 
            if stack_idx == 0: 
                print('-1')
            else: 
                print(stack[stack_idx-1])