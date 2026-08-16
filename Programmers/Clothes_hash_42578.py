clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

c_dict = dict()
for c in clothes: 
    if (c_dict.get(c[1])): 
        c_dict[c[1]].append(c[0])
    else: 
        c_dict[c[1]] = [c[0]]
print(c_dict)

answer = 1
for cnt in c_dict.items(): 
    answer *= (len(cnt[1]) + 1)
answer -= 1
print(answer)