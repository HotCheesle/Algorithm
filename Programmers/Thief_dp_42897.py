money = [1, 2, 3, 1]

if len(money) == 3: 
    print(max(money))
dp_f = [0 for _ in range(len(money)-1)]
dp_s = [0 for _ in range(len(money)-1)]
dp_f[0], dp_f[1], dp_s[0], dp_s[1] = money[0], money[1], money[1], money[2]
for i in range(2, len(money)-1): 
    if i == 2: 
        if dp_f[0] + money[i] >= dp_f[1]: 
            dp_f[2] = dp_f[0] + money[i]
        else: 
            dp_f[2] = dp_f[1]
        if dp_s[0] + money[i+1] >= dp_s[1]: 
            dp_s[2] = dp_s[0] + money[i+1]
        else: 
            dp_s[2] = dp_s[1]
    else: 
        ppp_f = dp_f[i-3] + money[i]
        pp_f =  dp_f[i-2] + money[i]
        p_f = dp_f[i-1]

        ppp_s = dp_s[i-3] + money[i+1]
        pp_s = dp_s[i-2] + money[i+1]
        p_s = dp_s[i-1]

        dp_f[i] = max(ppp_f, pp_f, p_f)
        dp_s[i] = max(ppp_s, pp_s, p_s)

print(max(dp_f[-1], dp_s[-1]))