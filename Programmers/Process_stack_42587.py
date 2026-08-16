from collections import deque

priorities, location = [2, 1, 3, 2], 2

# is_run = [0 for _ in range(len(priorities))]

q = deque(zip(priorities, range(len(priorities))))
run = 1

process = q.popleft()
while True: 
    if not q: 
        print(run)
    if process[0] >= max(q, key=lambda x: x[0])[0]: 
        if process[1] == location: 
            print(run)
        else: 
            process = q.popleft()
            run += 1
    else: 
        q.append(process)
        process = q.popleft()
