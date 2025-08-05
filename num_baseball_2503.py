numbers = {str(i) + str(j) + str(k) 
           for i in range(1, 10) 
           for j in range(1, 10) 
           for k in range(1, 10) 
           if i != j and j != k and i != k}
rm_list = []

def num_baseball(possible, call):
    strike, ball = 0, 0
    for i in range(3): 
        if possible[i] == call[i]: 
            strike += 1
        elif call[i] in possible:
            ball += 1

    return str(strike), str(ball) 

n = int(input())
for i in range(n): 
    call_num, *count = input().split()
    call_num = list(call_num)
    for nums in numbers: 
        possi_num = list(nums)
        result_count = num_baseball(possi_num, call_num)
        if count != list(result_count): 
            rm_list.append(nums)
    for rm in rm_list: 
        numbers.discard(rm)
    rm_list.clear()

print(len(numbers))