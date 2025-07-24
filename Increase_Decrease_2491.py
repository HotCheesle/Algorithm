n = int(input())
num_list = list(map(int, input().split()))

max_sequence = 0
common = 0
if n < 3: 
    print(n) 
else: 
    increase_mod = None
    sequence = 2
    if num_list[0] < num_list[1]: 
        increase_mod = True
    elif num_list[0] > num_list[1]: 
        increase_mod = False
    for i in range(2, n): 
        if increase_mod is None: 
            if num_list[i-1] < num_list[i]: 
                increase_mod = True
                sequence += 1
            elif num_list[i-1] > num_list[i]: 
                increase_mod = False
                sequence += 1
            else: 
                sequence += 1
        elif increase_mod is True: 
            if num_list[i-1] < num_list[i]: 
                sequence += 1
                common = 0
            elif num_list[i-1] == num_list[i]: 
                sequence += 1
                common += 1
            else: 
                increase_mod = False
                if max_sequence < sequence:
                    max_sequence = sequence
                sequence = 2 + common
                common = 0
        else: 
            if num_list[i-1] > num_list[i]: 
                sequence += 1
                common = 0
            elif num_list[i-1] == num_list[i]: 
                sequence += 1
                common += 1
            else: 
                increase_mod = True
                if max_sequence < sequence:
                    max_sequence = sequence
                sequence = 2 + common
                common = 0
    if max_sequence < sequence: 
        max_sequence = sequence
    print(max_sequence)