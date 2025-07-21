import sys

def opsit(dice, down_num): 
    five, six = False, False
    if down_num == 5: 
        five = True
    elif down_num == 6: 
        six = True
    up_num = dice[ch_idx(dice.index(down_num))]
    if up_num == 5: 
        five = True
    elif up_num == 6:
        six = True
    if five and six: 
        max_n = 4
    elif six: 
        max_n = 5
    else: 
        max_n = 6
    return up_num, max_n

def ch_idx(idx): 
    if idx == 0: 
        return 5
    elif idx == 5: 
        return 0
    elif idx < 3: 
        return idx + 2
    else: return idx - 2

N = int(sys.stdin.readline())
dice = list(list(map(int, sys.stdin.readline().split()))for _ in range(N))

max_sum = 0
for i in range(6):
    sum = 0
    n = dice[0][i]
    for d in dice:
        n, max_n = opsit(d, n)
        sum = sum + max_n
    if max_sum < sum: max_sum = sum
    six_cnt = 0

print(max_sum)