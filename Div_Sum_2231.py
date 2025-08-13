N = int(input())
num = 1
while num < N: 
    de_sum = 0
    str_num = str(num)
    for n in str_num: 
        de_sum += int(n)
    if num + de_sum == N: 
        print(num)
        break
    else: 
        num += 1
else: 
    print(0)