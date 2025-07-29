prime_num_list = [i for i in range(2, 1001)]
for p in prime_num_list: 
    rm = p * 2
    while rm < 1001: 
        try: 
            prime_num_list.remove(rm)
        except: 
            rm += p
            continue
        
n = int(input())
num_list = list(map(int, input().split()))

prime_cnt = 0
for num in num_list: 
    if num in prime_num_list: 
        prime_cnt += 1
print(prime_cnt)