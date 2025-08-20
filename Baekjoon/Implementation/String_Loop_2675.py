T = int(input())
for t in range(T): 
    rep, string = input().split()
    newstr = ''
    for s in string: 
        for r in range(int(rep)): 
            newstr += s
    print(newstr)