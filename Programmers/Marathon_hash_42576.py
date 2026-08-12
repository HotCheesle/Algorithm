participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


p_list = dict()
for p in participant: 
    if (p_list.get(p)): 
        p_list[p] += 1
    else: 
        p_list[p] = 1
print(p_list)
for c in completion: 
    if (p_list.get(c)): 
        p_list[c] -= 1
        if (p_list[c] == 0): 
            p_list.pop(c)
print(p_list)

answer = p_list.popitem()[0]
print(answer)