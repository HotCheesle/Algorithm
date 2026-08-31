money = [1, 2, 3, 1]

if len(money) == 3: 
    return max(money)
dp = [(0, 0) for _ in range(len(money))]
dp[0], dp[1] = (money[0], 1), (money[1], 0)
for i in range(2, len(money)): 
    if i == 2: 
        if dp[0][0] + money[i] > dp[1][0]: 
            dp[2] = (dp[0][0], 1)
        else: 
            dp[2] = (dp[1][0], 0)
    elif i == len(money)-1: 
        pass
    else: 
        if dp[i-3][0] + money[i] > 
        dp[i] = max(dp[i-3] + money[i], dp[i-2] + money[i], dp[i-1])

