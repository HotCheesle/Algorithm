T = int(input())
for tc in range(T): 
    stack = []
    string = input()
    for c in string: 
        if c == '(': 
            stack.append(c)
        else: 
            try: 
                stack.pop()
            except: 
                print('NO')
                break
    else: 
        if len(stack) == 0: 
            print('YES')
        else: 
            print('NO')