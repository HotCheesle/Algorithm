num_list = []
for _ in range(9): 
    num_list.append(int(input()))

idx = 0
max_num = -1
for i in range(9): 
    if max_num < num_list[i]: 
        max_num = num_list[i]
        idx = i
print(max_num)
print(idx + 1)