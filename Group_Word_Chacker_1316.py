T = int(input())

group = None
group_word = 0

for t in range(T): 
    string = input()
    alp_flag = [0 for _ in range(26)]
    for s in string: 
        if alp_flag[ord(s) - 97] == 0: 
            group = s
            alp_flag[ord(s) - 97] = 1
        elif group == s: 
            continue
        else: 
            break
    else: 
        group_word += 1

print(group_word)