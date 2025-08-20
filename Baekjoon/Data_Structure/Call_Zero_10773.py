N = int(input())
stack = []
for _ in range(N): 
    inpt = int(input())
    if inpt == 0: 
        stack.pop()
    else: 
        stack.append(inpt)

print(sum(stack))