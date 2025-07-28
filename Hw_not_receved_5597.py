ck_list = [0 for _ in range(30)]

for _ in range(28): 
    n = int(input())
    ck_list[n-1] = 1

for i in range(30): 
    if ck_list[i] == 0: 
        print(i+1)