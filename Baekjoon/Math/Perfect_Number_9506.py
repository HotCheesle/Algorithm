n = None
while True: 
    n = int(input())
    if n == -1: break
    div_list = []
    for i in range(1, n // 2 + 1): 
        if n % i == 0: 
            div_list.append(i)
    tot = 0
    for num in div_list: 
        tot += num
    if n == tot: 
        print(f'{n} = ', end='')
        for num in div_list[:-1]: 
            print(f'{num} + ', end='')
        print(str(div_list[-1]))
    else: 
        print(f'{n} is NOT perfect.')