T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    tree_list = list(map(int, input().split()))
    small_list = list(map(lambda t: max(tree_list)-t, tree_list))
    day = 1
    while max(small_list) != 0: 
        even, odd = 0, 0
        for s in small_list: 
            if s == 0: continue
            if s % 2 == 0: 
                even += 1
            else: 
                odd += 1

        if day % 2 == 0: 
            for i in range(N): 
                if small_list[i] > 1: 
                    small_list[i] -= 2
                    break
            day += 1
        else: 
            if (even + odd) == 1: 
                for i in range(N): 
                    if small_list[i] > 0 and small_list[i] != 2: 
                        small_list[i] -= 1
                        break
                day += 1
            elif even > odd: 
                if max(small_list) > 2: 
                    for i in range(N): 
                        if small_list[i] > 0 and small_list[i] % 2 == 0: 
                            small_list[i] -= 1
                            break
                else: 
                    for i in range(N): 
                        if small_list[i] == 1: 
                            small_list[i] -= 1
                            break
                day += 1
            elif odd >= even: 
                for i in range(N): 
                    if small_list[i] > 0 and small_list[i] % 2 == 1: 
                        small_list[i] -= 1
                        break
                day += 1
    print(f'#{tc} {day-1}')