deci, num_sys = map(int, input().split())

digit = 1
ch_num = 1
if deci < 2: 
    print(deci)
else: 
    while ch_num <= deci: 
        ch_num *= num_sys
        digit += 1
    else: 
        digit -= 1
        ch_num //= num_sys
    for _ in range(digit): 
        num = deci // ch_num
        if num < 10: 
            print(num, end='')
        else: 
            print(chr(num + 55), end='')
        deci -= (num * ch_num)
        ch_num //= num_sys
    print()