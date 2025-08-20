n1, n2 = map(int, input().split())

div_list = []
for i in range(1, n1 + 1): 
    if n1 % i == 0: 
        div_list.append(i)
try: 
    print(div_list[n2-1])
except: 
    print(0)