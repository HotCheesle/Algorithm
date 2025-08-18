string = list(input())
cnt = 0
for i in range(1, len(string) + 1): 
    if string[i-1] == 'Y': 
        num = i
        cnt += 1
        while num-1 < len(string): 
            if string[num-1] == 'Y': 
                string[num-1] = 'N'
            else: 
                string[num-1] = 'Y'
            num += i

for off in string: 
    if off != 'N': 
        print('-1')
        break
else: 
    print(cnt)