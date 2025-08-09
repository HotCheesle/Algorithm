T = int(input())
for tc in range(1, T+1): 
    N = int(input())
    init_list = list(map(int, input().split()))
    final_list = list(map(int, input().split()))
    is_flip = 0
    cnt = 0
    for i in range(N): 
        if init_list[i] ^ is_flip != final_list[i]: 
            is_flip ^= 1
            cnt += 1
    print(f'#{tc} {cnt}')