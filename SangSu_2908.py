string = list(input().split())
num = ['', '']
for i in range(2): 
    for s in reversed(string[i]): 
        num[i] += s

if int(num[0]) < int(num[1]): 
    print(num[1])
else: 
    print(num[0])