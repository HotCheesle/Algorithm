def char_to_int(char): 
    c = ord(char) - 65
    if c < 15: 
        return (c // 3) + 3
    elif c < 19: 
        return 8
    elif c < 22: 
        return 9
    else: 
        return 10
    
string = input()
tot = 0
for s in string: 
    tot += char_to_int(s)
print(tot)