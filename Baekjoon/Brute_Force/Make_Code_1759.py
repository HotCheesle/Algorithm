def get_code(code, selidx, pass_cnt): 
    if pass_cnt > C - L: return
    if len(code) == L: 
        if get_v(code): 
            print(''.join(code))
            return
        else: 
            return
    new_code = code.copy()
    new_code.append(char_list[selidx])
    get_code(new_code, selidx+1, pass_cnt)
    new_code.pop()
    get_code(new_code, selidx+1, pass_cnt+1)

def get_v(code): 
    con, vow = 0, 0
    for c in code: 
        if c in vowel: 
            vow += 1
        else: 
            con += 1
    if vow >= 1 and con >= 2: 
        return True
    else: 
        return False

L, C = map(int, input().split())
char_list = list(input().split())
char_list.sort()
vowel = ('a', 'e', 'i', 'o', 'u')
get_code([], 0, 0)