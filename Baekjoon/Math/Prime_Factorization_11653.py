N = int(input())
if N == 1: 
    pass
else: 
    sub = 2
    while N != 1: 
        while N % sub == 0: 
            N //= sub
            print(sub)
        sub += 1