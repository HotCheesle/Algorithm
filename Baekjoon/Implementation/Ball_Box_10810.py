n, m = map(int, input().split())
box = [0 for _ in range(n)]

for _ in range(m): 
    st, ed, num = map(int, input().split())
    for i in range(st-1, ed): 
        box[i] = num
        
for b in box: 
    print(b, end=" ")
    