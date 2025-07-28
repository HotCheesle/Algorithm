n, m = map(int, input().split())
box = [i for i in range(1, n+1)]

def swap(s1, s2): 
    global box
    temp = box[s1 - 1]
    box[s1 - 1] = box[s2 - 1]
    box[s2 - 1] = temp
    
for _ in range(m): 
    a, b = map(int, input().split())
    swap(a, b)

for b in box: 
    print(b, end=" ")
