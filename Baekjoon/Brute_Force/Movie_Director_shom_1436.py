N = int(input())
title = 666
if N == 1: 
    print(title)
else: 
    cnt = 1
    while cnt != N: 
        title += 1
        if str(title).find('666') != -1: 
            cnt += 1
    print(title)
