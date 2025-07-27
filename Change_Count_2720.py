T = int(input())

coins = [25, 10, 5, 1]

for t in range(T): 
    change = int(input())
    coin_cnt = [0, 0, 0, 0]
    idx = 0
    for coin in coins: 
        coin_cnt[idx] = change // coin
        change -= coin_cnt[idx] * coin
        idx += 1
    for c in coin_cnt: 
        print(c, end=' ')
    print()