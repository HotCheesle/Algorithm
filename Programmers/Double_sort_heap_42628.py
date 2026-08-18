from heapq import heappush, heappop

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

min_heap = []
max_heap = []
deleted_id = set()
id = 1

for str in operations:
    op, val = str.split()
    val = int(val)
    if op == 'I': 
        heappush(min_heap, (val, id))
        heappush(max_heap, (val*-1, id))
        id += 1
    else: 
        if not min_heap: 
            continue
        if val == 1:
            while max_heap and (max_heap[0][1]) in deleted_id: 
                heappop(max_heap)
            if not max_heap: 
                continue
            deleted_id.add(heappop(max_heap)[1])
        else: 
            while min_heap and (min_heap[0][1]) in deleted_id: 
                heappop(min_heap)
            if not min_heap: 
                continue
            deleted_id.add(heappop(min_heap)[1]) 

while max_heap and (max_heap[0][1]) in deleted_id: 
    heappop(max_heap)
while min_heap and (min_heap[0][1]) in deleted_id: 
    heappop(min_heap)

if min_heap: 
    print(f"[{heappop(max_heap)[0]*-1},{heappop(min_heap)[0]}]")
else: 
    print("[0,0]")