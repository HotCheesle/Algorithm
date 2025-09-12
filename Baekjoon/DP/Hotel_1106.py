C, N = map(int, input().split())
cytis = []
max_customer = 0
for _ in range(N): 
    cost, customer = map(int, input().split())
    max_customer = max(max_customer, customer)
    cytis.append((cost, customer))
cost, customer = 0, 0
dp = [10**9 for _ in range(C+max_customer)]
dp[0] = 0
for c in range(1, C+max_customer): 
    for cyti in cytis: 
        ref = c - cyti[1]
        if ref >= 0: 
            dp[c] = min(dp[c], dp[ref]+cyti[0])
min_cost = min(dp[C:])
print(min_cost)