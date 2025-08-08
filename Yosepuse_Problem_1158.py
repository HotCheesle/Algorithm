def enq(num): 
    global end
    queue[end] = num
    end += 1
    if end > N: 
        end = 0

def deq():
    global start
    num = queue[start]
    queue[start] = 0
    start += 1
    if start > N: 
        start = 0
    return num

N, K = map(int, input().split())
queue = list(i for i in range(1, N+1))
queue.append(0)
start, end = 0, len(queue)-1
yosepuse = []
for n in range(N-1): 
    for i in range(K-1): 
        temp = deq()
        enq(temp)
    yosepuse.append(str(deq()))
yosepuse.append(str(deq()))

print(f'<{", ".join(yosepuse)}>')