from collections import deque

N, D = map(int, input().split())
short_cuts = []
for _ in range(N): 
    st, ed, length = map(int, input().split())
    short_cuts.append((st, ed, length))
short_cuts.sort(key=lambda sc: sc[1])
short_cuts = deque(short_cuts)
dp = [10000 for _ in range(D+1)]
dp[0] = 0
for idx in range(1, D+1): 
    while short_cuts and short_cuts[0][1] == idx: 
        dp[idx] = min(dp[short_cuts[0][0]] + short_cuts[0][2], 
                    dp[idx-1] + 1, dp[idx])
        short_cuts.popleft()
        if not short_cuts or short_cuts[0][1] != idx: break
    else: 
        dp[idx] = dp[idx-1] + 1
print(dp[D])