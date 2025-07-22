import sys

sw_N = int(sys.stdin.readline())
sw_lst = list(map(int, sys.stdin.readline().split()))
stud_N = int(sys.stdin.readline())
stud_lst = list(list(map(int, sys.stdin.readline().split()))
                for _ in range(stud_N))

def switching(num): 
    sw_lst[num-1] = sw_lst[num-1] ^ 1

for stud in stud_lst:
    num = stud[1]
    if stud[0] == 1: 
        while sw_N >= num: 
            switching(num)
            num = num + stud[1]
    else: 
        switching(num)
        for i in range(1, sw_N//2): 
            left = num - i
            right = num + i
            if left-1 < 0 or right > sw_N: break
            if sw_lst[left-1] != sw_lst[right-1]: break
            switching(left)
            switching(right)
            
print_cnt = 0
for i in range(sw_N): 
    if print_cnt >= 20: 
        print("")
        print_cnt = 0
    if print_cnt != 0: print(" ", end="")
    print(sw_lst[i], end="")
    print_cnt = print_cnt + 1