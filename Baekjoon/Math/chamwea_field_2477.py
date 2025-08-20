N = int(input())
vertical = []
horizontal = []
in_order = []
for _ in range(6): 
    direc, length = map(int, input().split())
    in_order.append(length)
    if direc <= 2: 
        horizontal.append(length)
    else: 
        vertical.append(length)
v_len = max(vertical)
h_len = max(horizontal)

not_use = []
for i in range(6): 
    if in_order[i] == v_len or in_order[i] == h_len: 
        not_use.append(i)
        if i == 0: 
            not_use.append(5)
        else: 
            not_use.append(i-1)
        if i == 5: 
            not_use.append(0)
        else: 
            not_use.append(i+1)

sub_area = 1
for i in range(6): 
    if i not in not_use: 
        sub_area *= in_order[i]

tot_area = v_len * h_len

print((tot_area - sub_area) * N)