import sys

def start_bingo(bingo, call):
    call_cnt = 0
    bingo_cnt = 0 
    while True:
        for i in range(5): 
            for j in range(5): 
                if bingo[i][j] == call[call_cnt]: 
                    bingo[i][j] = 0
                    call_cnt += 1
                    bingo_cnt = bingo_test(bingo)
                    if bingo_cnt >= 3: return call_cnt


def bingo_test(bingo): 
    bin_cnt = 0
    u_bin = 0
    d_bin = 0
    for i in range(5): 
        v_bin = 0
        h_bin = 0
        for j in range(5): 
            if bingo[i][j] == 0: h_bin += 1
            if bingo[j][i] == 0: v_bin += 1
        if v_bin == 5: bin_cnt += 1
        if h_bin == 5: bin_cnt += 1
        if bingo[i][i] == 0: d_bin += 1
        if bingo[4-i][i] == 0: u_bin += 1
    if u_bin == 5: bin_cnt += 1
    if d_bin == 5: bin_cnt += 1

    return bin_cnt

        

bingo = list(list(map(int, sys.stdin.readline().split()))for _ in range(5))
call = list()
for _ in range(5): 
    call = call + list(map(int, sys.stdin.readline().split()))

call_cnt = start_bingo(bingo, call)
print(call_cnt)