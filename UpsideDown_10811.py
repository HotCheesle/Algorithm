n, m = map(int, input().split())
bucket_list = [i for i in range(1, n+1)]

def reverce(st, ed): 
    temp_list = []
    for i in range(st-1, ed): 
        temp_list.append(bucket_list[i])
    for i in range(ed - st + 1): 
        bucket_list[ed-i-1] = temp_list[i]
        
for _ in range(m): 
    s, e = map(int, input().split())
    reverce(s, e)

for b in bucket_list: 
    print(b, end=" ")