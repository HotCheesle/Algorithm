mod_list = [0 for _ in range(42)]

for _ in range(10): 
    n = int(input())
    mod_list[n % 42] += 1

cnt = 0
for m in mod_list: 
    if m != 0: 
        cnt += 1

print(cnt)