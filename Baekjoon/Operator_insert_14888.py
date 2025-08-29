def brute_force(i, N, num_list): 
    nlst = num_list.copy()
    for idx in range(i, N-1): 
        nlst[i], nlst[idx+1] = nlst[idx+1], nlst[i]
        brute_force(i+1, N, nlst)
        nlst[i], nlst[idx+1] = nlst[idx+1], nlst[i]
        brute_force(i+1, N, nlst)
    op_order.add(tuple(nlst))


N = int(input())
num_list = list(map(int, input().split()))
inpt = list(map(int, input().split()))
op_list = []
op = '+-*/'
for i in range(4): 
    op_list.extend([op[i]] * inpt[i])
op_order = set()
brute_force(0, N-1, op_list)
result_list = []
while op_order:
    order = op_order.pop()
    x1 = num_list[0]
    for i in range(1, N): 
        x2 = num_list[i]
        if order[i-1] == '+': 
            x1 += x2
        elif order[i-1] == '-': 
            x1 -= x2
        elif order[i-1] == '*': 
            x1 *= x2
        elif order[i-1] == '/': 
            x1 //= x2
    result_list.append(x1)
print(result_list)
print(max(result_list))
print(min(result_list))